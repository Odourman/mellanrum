#!/usr/bin/env python3
"""Bespoke 6502 instruction-level DEVELOPMENT tracer, NOT a certified TIA/Stella emulator.
Runs the 4K ROM and checks input register effects, VSYNC/VBLANK and WSYNC cadence.
"""
import pathlib,sys,collections
sys.path.insert(0,str(pathlib.Path(__file__).parent))
from assemble_check import OP
DEC={v:(k,mode) for k,mp in OP.items() for mode,v in mp.items()}
FLAGS={'C':1,'Z':2,'I':4,'D':8,'B':16,'U':32,'V':64,'N':128}
BASE_CYC={
 'imm':2,'zp':3,'zpx':4,'zpy':4,'abs':4,'absx':4,'absy':4,'indx':6,'indy':5,'ind':5,'rel':2,'imp':2,
}
class CPU:
 def __init__(self,rom,syms):
  self.mem=bytearray(65536);self.mem[0xF000:0x10000]=rom
  self.syms=syms;self.a=0;self.x=0;self.y=0;self.sp=0xff;self.p=0x24;self.pc=rom[-4]|(rom[-3]<<8)
  self.time=0;self.wsync_count=0;self.wsync_missed=0;self.wsync_by_region=collections.Counter();self.frame_samples=[]
  self.lastwsync=None;self.regwrites=collections.Counter();self.input_swcha=0xff;self.input_swchb=0xff;self.input_fire=False;self.timerdeadline=0
  self.start_pc=self.syms['Frame'];self.old_frame_time=None;self.frames=0;self.max_stack=0xff;self.max_gap=0
  self.max_cost_by_region={};self.audio_seen=set();self.wsync_gaps=collections.Counter();self.wsync_errors=collections.Counter();self.inst_pc=None
 def read(self,addr):
  addr &=0xffff
  if addr in (0x280,):return self.input_swcha
  if addr in (0x282,):return self.input_swchb
  if addr==0x0c:return 0x00 if self.input_fire else 0x80
  if addr==0x284:return max(0,min(255,(self.timerdeadline-self.time+63)//64))
  if 0x0100<=addr<0x0200:return self.mem[addr-0x0100]
  return self.mem[addr]
 def write(self,addr,val):
  addr &=0xffff;val&=255
  if 0x0100<=addr<0x0200:self.mem[addr-0x0100]=val;return
  if addr==0x296:self.timerdeadline=self.time+val*64;return
  if addr<=0x2d:
   self.regwrites[addr]+=1
   if addr==0x02:
    if self.lastwsync is not None:
     gap=self.time-self.lastwsync
     if gap>self.max_gap:self.max_gap=gap
     self.wsync_gaps[(self.inst_pc,gap)]+=1
     if gap>76:self.wsync_missed+=1;self.wsync_errors[self.inst_pc]+=1
    self.wsync_count+=1
    self.time+=(-self.time)%76 or 76
    self.lastwsync=self.time
   if addr in (0x19,0x1a):self.audio_seen.add((addr,val))
   self.mem[addr]=val
   return
  self.mem[addr]=val
 def pus(self,val):
  self.write(0x100+self.sp,val);self.sp=(self.sp-1)&255
  if self.sp<self.max_stack:self.max_stack=self.sp
 def pop(self):
  self.sp=(self.sp+1)&255;return self.read(0x100+self.sp)
 def flag(self,flag):return bool(self.p&FLAGS[flag])
 def setflag(self,flag,yes):
  if yes:self.p|=FLAGS[flag]
  else:self.p&=255^FLAGS[flag]
 def nz(self,val):
  self.setflag('Z',(val&255)==0);self.setflag('N',bool(val&128));return val&255
 def word(self):
  lo=self.read(self.pc);hi=self.read(self.pc+1);self.pc+=2;return lo|(hi<<8)
 def step(self):
  if self.pc==self.start_pc:
   if self.old_frame_time is not None:
    self.frame_samples.append((self.time-self.old_frame_time,self.wsync_count,self.wsync_missed))
   self.frames+=1;self.old_frame_time=self.time
  at=self.pc;self.inst_pc=at;opcode=self.read(self.pc);self.pc=(self.pc+1)&65535
  if opcode not in DEC:raise RuntimeError(f'unsupported opcode {opcode:02X} at {at:04X}, cycle={self.time}')
  m,mode=DEC[opcode]
  if mode=='imp':addr=None;val=None
  elif mode=='imm':val=self.read(self.pc);self.pc+=1;addr=None
  elif mode=='rel':val=self.read(self.pc);self.pc+=1;val=(val if val<128 else val-256);addr=None
  elif mode in ('zp','zpx','zpy','indx','indy'):
   z=self.read(self.pc);self.pc+=1
   if mode=='zpx':addr=(z+self.x)&255
   elif mode=='zpy':addr=(z+self.y)&255
   elif mode=='indx':
    z=(z+self.x)&255;addr=self.read(z)|(self.read((z+1)&255)<<8)
   elif mode=='indy':addr=(self.read(z)|(self.read((z+1)&255)<<8))+self.y
   else:addr=z
   val=self.read(addr)
  elif mode in ('abs','absx','absy','ind'):
   addr=self.word()
   if mode=='absx':addr=(addr+self.x)&65535
   if mode=='absy':addr=(addr+self.y)&65535
   if mode=='ind':addr=self.read(addr)|(self.read((addr+1)&65535)<<8)
   val=self.read(addr)
  else:raise AssertionError((m,mode))
  cycles=BASE_CYC[mode]
  if m in ('lda','ldx','ldy'):
   setattr(self,{'lda':'a','ldx':'x','ldy':'y'}[m],self.nz(val))
   if mode in ('absx','absy','indy'):cycles+=1 # max bound (page cross overestimated)
  elif m in ('sta','stx','sty'):
   if m=='sta':v=self.a
   elif m=='stx':v=self.x
   else:v=self.y
   if mode in ('absx','absy'):cycles=5
   self.time+=cycles;self.write(addr,v);return
  elif m in ('and','ora','eor','adc','sbc'):
   if m=='and':self.a=self.nz(self.a&val)
   if m=='ora':self.a=self.nz(self.a|val)
   if m=='eor':self.a=self.nz(self.a^val)
   if m in ('adc','sbc'):
    if m=='adc':v=self.a+val+(1 if self.flag('C') else 0);c=v>255;overflow=bool((~(self.a^val)&(self.a^v)&128))
    else:v=self.a+(val^255)+(1 if self.flag('C') else 0);c=v>255;overflow=bool(((self.a^v)&(self.a^val)&128))
    self.a=self.nz(v);self.setflag('C',c);self.setflag('V',overflow)
  elif m in ('cmp','cpx','cpy'):
   v=getattr(self,{'cmp':'a','cpx':'x','cpy':'y'}[m]);r=v-val;self.nz(r);self.setflag('C',v>=val)
  elif m in ('inc','dec'):
   r=(val+(1 if m=='inc' else -1))&255;self.nz(r);self.time+=cycles+(2 if mode=='zp' else 3);self.write(addr,r);return
  elif m in ('asl','lsr','rol','ror'):
   v=self.a if mode=='imp' else val;old_c=self.flag('C');newc=(bool(v&128) if m in ('asl','rol') else bool(v&1))
   if m=='asl':r=(v<<1)&255
   elif m=='lsr':r=v>>1
   elif m=='rol':r=((v<<1)|(1 if old_c else 0))&255
   else:r=(v>>1)|(0x80 if old_c else 0)
   self.setflag('C',newc);self.nz(r)
   if mode=='imp':self.a=r
   else:self.time+=cycles+2;self.write(addr,r);return
  elif m=='clc':self.setflag('C',False)
  elif m=='sec':self.setflag('C',True)
  elif m=='sei':self.setflag('I',True)
  elif m=='cli':self.setflag('I',False)
  elif m=='cld':self.setflag('D',False)
  elif m=='sed':self.setflag('D',True)
  elif m=='tax':self.x=self.nz(self.a)
  elif m=='txa':self.a=self.nz(self.x)
  elif m=='tay':self.y=self.nz(self.a)
  elif m=='tya':self.a=self.nz(self.y)
  elif m=='txs':self.sp=self.x
  elif m=='tsx':self.x=self.nz(self.sp)
  elif m=='dex':self.x=self.nz(self.x-1)
  elif m=='inx':self.x=self.nz(self.x+1)
  elif m=='dey':self.y=self.nz(self.y-1)
  elif m=='iny':self.y=self.nz(self.y+1)
  elif m=='pha':self.pus(self.a);cycles=3
  elif m=='pla':self.a=self.nz(self.pop());cycles=4
  elif m=='jmp':self.pc=addr;cycles=3
  elif m=='jsr':
   ret=(self.pc-1)&65535;self.pus(ret>>8);self.pus(ret&255);self.pc=addr;cycles=6
  elif m=='rts':self.pc=(self.pop()|(self.pop()<<8))+1;cycles=6
  elif m in ('bne','beq','bcc','bcs','bmi','bpl','bvc','bvs'):
   take={'bne':lambda:not self.flag('Z'),'beq':lambda:self.flag('Z'),
    'bcc':lambda:not self.flag('C'),'bcs':lambda:self.flag('C'),
    'bmi':lambda:self.flag('N'),'bpl':lambda:not self.flag('N'),
    'bvc':lambda:not self.flag('V'),'bvs':lambda:self.flag('V')}[m]()
   if take:
    dest=(self.pc+val)&65535;cycles+=1+((dest>>8)!=(self.pc>>8));self.pc=dest
  elif m in ('nop','rti'):pass
  else:raise RuntimeError((m,at))
  self.time+=cycles
 def run_to_frame(self,n,instr_cap=7000000):
  cap=0
  while self.frames<n:
   self.step();cap+=1
   if cap>=instr_cap:raise RuntimeError(f'instruction limit reached, pc {self.pc:04X}, frame {self.frames}, time {self.time}')
  return self
 def ram(self,name):return self.read(self.syms[name])

def load(romfile='build/mellanrum_ntsc.bin',symfile='build/mellanrum_ntsc.sym'):
 s={k:int(v.replace('$',''),16) for k,v in (ln.strip().split(' = ') for ln in pathlib.Path(symfile).read_text().splitlines())}
 return CPU(pathlib.Path(romfile).read_bytes(),s)

if __name__=='__main__':
 cpu=load();cpu.run_to_frame(120)
 print('Frames',cpu.frames,'cycles',cpu.time,'wsync',cpu.wsync_count,'outlier gaps',cpu.wsync_missed,'max gap',cpu.max_gap,'min SP',hex(cpu.max_stack))
 print('cycle/scanline frame length first',cpu.frame_samples[:15])
 print('mode',cpu.ram('mode'),'owl',cpu.ram('owlX'),cpu.ram('owlY'),'room',cpu.ram('room'),'b',cpu.ram('beat'))
 print('audio states',sorted(cpu.audio_seen))
