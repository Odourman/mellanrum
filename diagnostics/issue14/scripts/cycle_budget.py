#!/usr/bin/env python3
"""Issue #14 scanline *static* timing from sourced 6502 opcodes, no false native trace.
All three 9B sprite tables and the 14B SpriteRowIndex remain on one page, so
LDA (zp),Y does not add the optional page-cross penalty in this test build.
"""
import json,re,sys
from pathlib import Path
base=Path(__file__).resolve().parents[1]
source=(base/'rom/src/main.asm').read_text()
data=(base/'rom/src/data.inc').read_text()
assert '        cpx #1' in source and '        beq StemLastFast' in source
assert '        lda (pfPtr),y' in source
m=re.search(r'^Stem13:\n(.+?)^StemLastFast:',source,re.M|re.S)
assert m
loop=m.group(1)
nops=loop.count('        nop\n')
assert nops==14
# cycles after previous STA WSYNC releases CPU at start of next scanline
before_first=4+5+3+5+3
pre_wait=2+2
post_wait=5+3+2+3
normal=before_first+pre_wait+nops*2+post_wait
first_a=before_first
second_b=before_first+pre_wait+nops*2+5+3
last_fast=before_first+2+3+(3+2+2+3+5+3+2+3+3)
# Last row takes branch straight to footer; no jmp NextRow.
alloc={'normal_stem_loop_min_max':normal,'GRP0_first':12,'GRP1_first':first_a,'GRP1_second':second_b,'WSYNC_next_iteration_at_or_before':normal+3,'last_blank_row_next_row_first_WSYNC_no_later_than':last_fast,'margin_to_76':76-normal-3,'P1_first_origin_target_colorclocks':71,'P1_second_origin_target_colorclocks':135,'NUSIZ1_value':4,'P1_second_copy_distance_colorclocks':64,'last_BLANK_row_suppresses_second_write':True,'extra_DIAGNOSTIC_only_WSYNC_in_overscan':True}
assert normal+3<=76, alloc
(base/'build/cycle_budget.json').write_text(json.dumps(alloc,indent=2)+'\n')
print(json.dumps(alloc));sys.exit(0)
