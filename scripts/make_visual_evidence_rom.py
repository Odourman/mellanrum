#!/usr/bin/env python3
"""Construct transparently instrumented 6507 emulator-only ROM for observing an exact room/tick.

Product ROM never includes these instructions. DEBUG image uses unchanged product
RenderPlay, phase, TIA colors, shadow, and collision geometry. Its Reset stanza
sets a V5.1 source room and Presence beat before execution begins.

The instrumented binary is NOT a substitute for frame-exact product ROM replay.
"""
import argparse,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--room',type=int,required=True);p.add_argument('--beat',type=int,required=True);p.add_argument('--output',required=True)
a=p.parse_args();assert 0<=a.room<=14;assert 0<=a.beat<=7
s=(ROOT/'rom/src/main.asm').read_text()
key='        sta ENABL\n\nFrame:'
assert s.count(key)==1
inject=f'''        sta ENABL
        ; EMULATOR EVIDENCE VARIANT: only the Reset start state is instrumented.
        ; TIA/video, owl, collision, collision map and Presence code are unmodified.
        lda #{a.room}
        sta room
        lda #1
        sta mode
        jsr LoadRoom
        lda #{a.beat}
        sta beat
        jsr UpdatePresence
        lda #0
        sta introFrames
        sta soundStep
        lda #$FE             ; hold room/tick in image-capture window (< 4 s)
        sta beatFrames

Frame:'''
s=s.replace(key,inject,1)
out=pathlib.Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(s)
print(f'EVIDENCE_VARIANT room={a.room} beat={a.beat} product ASM untouched; variant={out}')
