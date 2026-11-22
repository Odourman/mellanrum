#!/usr/bin/env python3
"""Strict subset 6502 two-pass assembler used as a LOCAL byte-check oracle.
NOT a replacement for DASM. CI must build with authentic DASM and compare bytes.
"""
import ast, argparse, pathlib, re, hashlib, sys, operator
OP={
 'lda':{'imm':0xA9,'zp':0xA5,'zpx':0xB5,'abs':0xAD,'absx':0xBD,'absy':0xB9,'indy':0xB1,'indx':0xA1},
 'ldx':{'imm':0xA2,'zp':0xA6,'zpy':0xB6,'abs':0xAE,'absy':0xBE},
 'ldy':{'imm':0xA0,'zp':0xA4,'zpx':0xB4,'abs':0xAC,'absx':0xBC},
 'sta':{'zp':0x85,'zpx':0x95,'abs':0x8D,'absx':0x9D,'absy':0x99,'indx':0x81,'indy':0x91},
 'stx':{'zp':0x86,'zpy':0x96,'abs':0x8E},
 'sty':{'zp':0x84,'zpx':0x94,'abs':0x8C},
 'and':{'imm':0x29,'zp':0x25,'zpx':0x35,'abs':0x2D,'absx':0x3D,'absy':0x39,'indy':0x31},
 'ora':{'imm':0x09,'zp':0x05,'zpx':0x15,'abs':0x0D,'absx':0x1D,'absy':0x19,'indy':0x11},
 'eor':{'imm':0x49,'zp':0x45,'zpx':0x55,'abs':0x4D,'absx':0x5D,'absy':0x59,'indy':0x51},
 'adc':{'imm':0x69,'zp':0x65,'zpx':0x75,'abs':0x6D,'absx':0x7D,'absy':0x79,'indy':0x71},
 'sbc':{'imm':0xE9,'zp':0xE5,'zpx':0xF5,'abs':0xED,'absx':0xFD,'absy':0xF9,'indy':0xF1},
 'cmp':{'imm':0xC9,'zp':0xC5,'zpx':0xD5,'abs':0xCD,'absx':0xDD,'absy':0xD9,'indy':0xD1},
 'cpy':{'imm':0xC0,'zp':0xC4,'abs':0xCC},
 'cpx':{'imm':0xE0,'zp':0xE4,'abs':0xEC},
 'inc':{'zp':0xE6,'zpx':0xF6,'abs':0xEE,'absx':0xFE},
 'dec':{'zp':0xC6,'zpx':0xD6,'abs':0xCE,'absx':0xDE},
 'asl':{'imp':0x0A,'zp':0x06,'zpx':0x16,'abs':0x0E,'absx':0x1E},
 'lsr':{'imp':0x4A,'zp':0x46,'zpx':0x56,'abs':0x4E,'absx':0x5E},
 'ror':{'imp':0x6A,'zp':0x66,'zpx':0x76,'abs':0x6E,'absx':0x7E},
 'rol':{'imp':0x2A,'zp':0x26,'zpx':0x36,'abs':0x2E,'absx':0x3E},
 'jmp':{'abs':0x4C,'ind':0x6C},'jsr':{'abs':0x20},
 'rts':{'imp':0x60},'rti':{'imp':0x40},'sei':{'imp':0x78},'cli':{'imp':0x58},
 'cld':{'imp':0xD8},'sed':{'imp':0xF8},'sec':{'imp':0x38},'clc':{'imp':0x18},
 'tax':{'imp':0xAA},'txa':{'imp':0x8A},'tay':{'imp':0xA8},'tya':{'imp':0x98},
 'txs':{'imp':0x9A},'tsx':{'imp':0xBA},'dex':{'imp':0xCA},'inx':{'imp':0xE8},
 'dey':{'imp':0x88},'iny':{'imp':0xC8},'pha':{'imp':0x48},'pla':{'imp':0x68},
 'nop':{'imp':0xEA},
 'bne':{'rel':0xD0},'beq':{'rel':0xF0},'bcc':{'rel':0x90},'bcs':{'rel':0xB0},
 'bmi':{'rel':0x30},'bpl':{'rel':0x10},'bvc':{'rel':0x50},'bvs':{'rel':0x70},
}
BRANCH={s for s,x in OP.items() if 'rel' in x}

def readlines(path):
 out=[]
 for i,ln in enumerate(path.read_text().splitlines(),1):
  line=ln.split(';',1)[0].strip()
  if not line: continue
  if line.lower().startswith('include '):
   quoted=re.search(r'"([^"]+)"',line)
   assert quoted,(path,i,line)
   target=pathlib.Path(quoted.group(1))
   if not target.exists():target=path.parent/quoted.group(1)
   out+=readlines(target)
  else:out.append((str(path),i,line))
 return out

def calc(expr,labels,missing=False):
 expr=expr.strip().removeprefix('#')
 pref=None
 if expr.startswith(('<','>')):pref=expr[0];expr=expr[1:].strip()
 expr=re.sub(r'\$([0-9a-fA-F]+)',lambda m:'0x'+m.group(1),expr)
 expr=re.sub(r'(?<![\w])%([01]+)',lambda m:'0b'+m.group(1),expr)
 if re.fullmatch('[A-Za-z_][A-Za-z_0-9]*',expr):
  if expr not in labels:
   if missing:return None
   raise KeyError(expr)
  val=labels[expr]
 else:
  def evaluate(node):
   if isinstance(node,ast.Constant) and isinstance(node.value,int):return node.value
   if isinstance(node,ast.Name):
    if node.id not in labels:
     if missing:return None
     raise KeyError(node.id)
    return labels[node.id]
   if isinstance(node,ast.BinOp) and isinstance(node.op,(ast.Add,ast.Sub)):
    a,b=evaluate(node.left),evaluate(node.right)
    if a is None or b is None:return None
    return a+b if isinstance(node.op,ast.Add) else a-b
   raise ValueError(f'Unsafe expression {expr}')
  val=evaluate(ast.parse(expr,mode='eval').body)
 if val is None:return None
 return (val&255 if pref=='<' else (val>>8)&255 if pref=='>' else val)

def decode(mnem,operand,labels):
 ops=OP[mnem]
 if not operand:return 'imp',''
 if mnem in BRANCH:return 'rel',operand
 if operand.startswith('#'):return 'imm',operand[1:]
 if re.fullmatch(r'\(.+\),[Yy]',operand):return 'indy',operand[1:-3]
 if re.fullmatch(r'\(.+,[Xx]\)',operand):return 'indx',operand[1:-3]
 if re.fullmatch(r'\(.+\)',operand):return 'ind',operand[1:-1]
 m=re.fullmatch(r'(.+),\s*([XxYy])',operand)
 suffix=''
 if m:operand,suffix=m.group(1),m.group(2).lower()
 val=calc(operand,labels,missing=True)
 if suffix:
  z='zp'+suffix; a='abs'+suffix
  if val is not None and val<=255 and z in ops:return z,operand
  if a in ops:return a,operand
  raise ValueError(f'mode {mnem} {operand},{suffix}')
 if val is not None and val<=255 and 'zp' in ops:return 'zp',operand
 if 'abs' in ops:return 'abs',operand
 raise ValueError(f'mode {mnem} {operand}')

def assemble(path, outfile, symfile=None, listing=None):
 lines=readlines(path)
 labels={}; steps=[]
 for p in range(5):
  labels2=labels.copy();pc=0;steps=[]
  for src,line,s in lines:
   meta=(src,line,s)
   eq=re.match(r'^([A-Za-z_]\w*)\s*=\s*(.+)$',s)
   if eq:
    labels2[eq.group(1)]=calc(eq.group(2),labels2);continue
   if ':' in s and re.match(r'^[A-Za-z_]\w*:',s):
    name,s=s.split(':',1);s=s.strip();labels2[name]=pc
    if not s:continue
   else:
    maybe=re.match(r'^([A-Za-z_]\w+)\s+(ds|dc\.b|dc\.w)\s+(.+)$',s,re.I)
    if maybe and maybe.group(1).lower() not in OP:
     name,directive,operand=maybe.groups();labels2[name]=pc;s=f'{directive} {operand}'
   parts=s.split(None,1)
   command=parts[0].lower();operand=parts[1].strip() if len(parts)>1 else ''
   if command in ('processor','seg','seg.u'):continue
   if command=='org':
    pc=calc(operand,labels2);continue
   if command=='ds':
    pc+=calc(operand,labels2);continue
   if command in ('dc.b','dc.w'):
    count=len(operand.split(','));n=count*(1 if command=='dc.b' else 2)
    steps.append((pc,n,command,operand,meta));pc+=n;continue
   if command not in OP:raise ValueError(f'Unknown op {command} at {meta}')
   mode,expr=decode(command,operand,labels2)
   n=1 if mode=='imp' else (3 if mode in ('abs','absx','absy','ind') else 2)
   steps.append((pc,n,command,(mode,expr),meta));pc+=n
  if labels2==labels:break
  labels=labels2
 else:raise RuntimeError('Labels failed to stabilize')
 mem=bytearray([0xFF]*4096);used=set();fail=[];listing_lines=[]
 for pc,n,command,operand,meta in steps:
  if pc<0xF000 or pc+n>0x10000:raise ValueError(f'ROM overrun {pc:x} n{n}: {meta}')
  if command=='dc.b': data=[calc(x,labels)&255 for x in operand.split(',')]
  elif command=='dc.w':
   data=[]
   for x in operand.split(','):
    v=calc(x,labels);data.extend((v&255,(v>>8)&255))
  else:
   mode,expr=operand;data=[OP[command][mode]]
   if mode=='rel':
    target=calc(expr,labels);off=target-(pc+2)
    if not(-128<=off<=127):fail.append((pc,meta,off,expr));off&=255
    data.append(off&255)
   elif mode!='imp':
    v=calc(expr,labels)
    if mode in ('imm','zp','zpx','zpy','indx','indy'):
     if not 0<=v<=255:raise ValueError(f'8-bit overflow {v} at {meta}')
     data.append(v)
    else:data.extend((v&255,(v>>8)&255))
  assert len(data)==n,(pc,meta,data,n)
  for i,byte in enumerate(data):
   addr=pc+i
   if addr in used:raise ValueError(f'ROM overlap {addr:04X} ({meta})')
   used.add(addr);mem[addr-0xF000]=byte
  listing_lines.append(f'{pc:04X} '+''.join(f'{b:02X} ' for b in data).ljust(11)+' '.join(str(v) for v in meta[1:]))
 if fail:
  for pc,meta,off,expr in fail:print(f'BRANCH OUT OF RANGE at {pc:04X}, offset={off}, target={expr}, {meta[0]}:{meta[1]}',file=sys.stderr)
  raise ValueError(f'{len(fail)} relative branches outside -128..127')
 # Reset vectors at last 4 bytes.
 assert mem[-4:]==bytes([labels['Reset']&255,(labels['Reset']>>8)&255]*2)
 outfile.parent.mkdir(parents=True,exist_ok=True)
 outfile.write_bytes(mem)
 if symfile:symfile.write_text('\n'.join(f'{name} = ${addr:04X}' for name,addr in sorted(labels.items()))+'\n')
 if listing:listing.write_text('\n'.join(listing_lines)+'\n')
 print('LOCAL_ASSEMBLER_PASS',len(mem),'bytes','occupied',len(used),'free',4096-len(used),'last-code',f'{max(v for v in used if v<0xFFFC):04X}','sha256',hashlib.sha256(mem).hexdigest())
 return labels

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('src');ap.add_argument('-o','--out',default='build/mellanrum_ntsc.bin');args=ap.parse_args()
 p=pathlib.Path(args.out);assemble(pathlib.Path(args.src),p,p.with_suffix('.sym'),p.with_suffix('.lst'))
