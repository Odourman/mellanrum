#!/usr/bin/env python3
"""Offline reversible RLE experiment for the exact 45 x 256 LAB score streams."""
import re, json, hashlib
from pathlib import Path

root=Path(__file__).resolve().parents[3]/'package/BASELINE/LAB_BEST_SOURCE/rom/f6'
all_streams=[]; banks=[]
for b in range(3):
    src=(root/f'bank{b}_score.asm').read_text()
    labels=list(re.finditer(r'(?m)^(Act\d+Room\d+Voice\d+):\s*$',src))
    rows=[]
    for i,m in enumerate(labels):
        end=labels[i+1].start() if i+1<len(labels) else src.index('        ORG $FF00',m.end())
        vals=[]
        for line in re.findall(r'(?m)^\s*dc\.b\s+([^;\n]+)',src[m.end():end]):
            vals.extend(int(x,16) for x in re.findall(r'\$([0-9A-Fa-f]{2})',line))
        assert len(vals)==256,(m.group(1),len(vals))
        runs=[]
        for v in vals:
            if runs and runs[-1][1]==v and runs[-1][0]<255:runs[-1]=(runs[-1][0]+1,v)
            else:runs.append((1,v))
        packed=bytes(x for n,v in runs for x in (n,v))
        decoded=bytes(v for n,v in zip(packed[::2],packed[1::2]) for _ in range(n))
        assert decoded==bytes(vals)
        rec={'name':m.group(1),'raw_bytes':256,'rle_bytes':len(packed),'runs':len(runs),
             'raw_sha256':hashlib.sha256(bytes(vals)).hexdigest(),
             'decoded_sha256':hashlib.sha256(decoded).hexdigest()}
        rows.append(rec);all_streams.append(rec)
    banks.append({'bank':b,'streams':len(rows),'raw_bytes':sum(x['raw_bytes'] for x in rows),
                  'rle_bytes':sum(x['rle_bytes'] for x in rows),'runs':sum(x['runs'] for x in rows)})
res={'method':'RLE run-count/value pairs, max run 255, per stream, no cross-stream dictionary',
     'roundtrip':'PASS','streams_checked':len(all_streams),'decoded_bytes_checked':len(all_streams)*256,
     'banks':banks,'raw_total':sum(x['raw_bytes'] for x in all_streams),
     'rle_total':sum(x['rle_bytes'] for x in all_streams),
     'storage_delta':sum(x['raw_bytes']-x['rle_bytes'] for x in all_streams),
     'decoder_ROM_RAM_CPU':'NOT_BUILT; offline size is not runtime net capacity', 'stream_manifest':all_streams}
out=Path(__file__).resolve().parent/'R2_RLE_OFFLINE_RESULT.json'
out.write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:res[k] for k in ('roundtrip','streams_checked','decoded_bytes_checked','banks','raw_total','rle_total','storage_delta')}))
