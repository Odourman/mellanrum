"""Canonical candidate room data for MELLANRUM V5; maps to be raster-verified."""
from engine import Room
PATTERNS={
'A':('#####','#....','#.T..','#.T..','#..T.','#....','#....','#####'),
'B':('#####','#....','#.T..','#..T.','#T...','#.T..','#....','#####'),
'C':('#####','#....','#.TT.','#....','#.T..','#..T.','#....','#####'),
'D':('#####','#..T.','#....','#.TT.','#..T.','#....','#....','#####'),
'E':('#####','#....','#.T..','#..TT','#.T..','#.T..','#....','#####'),
}
DATA=[
# number, act, type, owl=(x,y,d), stone, exit, stone initial, name, note
('I-01',1,'A',(1,3,0),(4,3),(8,3),0,'Den första gläntan','Speglat ingrepp. Ugglan hittar en egen väg.'),
('I-02',1,'B',(1,2,0),(4,4),(8,2),0,'Det finns två stammar','FIRE förändrar samma form på båda sidor.'),
('I-03',1,'C',(1,4,0),(4,3),(8,4),1,'Stenen säger vänster','Stenens polaritet ändrar ugglans riktning.'),
('I-04',1,'D',(1,3,0),(4,2),(8,3),0,'En trädstam två sanningar','Samma visuella element får motsatta följder.'),
('I-05',1,'E',(1,3,0),(4,2),(8,3),1,'Den andra sidan','Symmetrin är en regel, inte ett löfte om trygghet.'),
('II-01',2,'A',(1,3,0),(4,3),(8,3),0,'Gårdagens dörr','Ändringarna kommer tillbaka efter tre steg.'),
('II-02',2,'B',(1,2,0),(4,4),(8,2),1,'Den långsamma stenen','Stenen växlar minnesfördröjning.'),
('II-03',2,'C',(1,4,0),(4,3),(8,4),0,'En handling som väntar','Två fördröjda händelser kan samexistera.'),
('II-04',2,'D',(1,3,0),(4,2),(8,3),1,'Stenen är ett protokoll','Avvisade handlingar är synliga, inte tysta buggar.'),
('II-05',2,'E',(1,3,0),(4,2),(8,3),0,'Skogen minns fel','Världen återtar ett gammalt tillstånd.'),
('III-01',3,'A',(1,3,0),(4,3),(8,3),0,'Trädet är ett hål','Kollisionen inverteras när skogen vänder.'),
('III-02',3,'B',(1,2,0),(4,4),(8,2),1,'Det tomma är fullt','Samma bild blir ett annat hinder.'),
('III-03',3,'C',(1,4,0),(4,3),(8,4),0,'En uggla är en klocka','Ljud och fas kan förskjutas i förhållande till rörelsen.'),
('III-04',3,'D',(1,3,0),(4,2),(8,3),1,'Stenen förnekar trädet','Stenen styr fasperioden, men inte ugglans vilja.'),
('III-05',3,'E',(1,3,0),(4,2),(8,3),0,'Det sista trädet','Alla tidigare regler sammanfaller.'),
]
ROOMS=[]
for ident,act,pattern,owl,stone,exit,pol,title,description in DATA:
    ROOMS.append(Room(ident,act,title,PATTERNS[pattern],owl,stone,exit,pol,description,description))
    ROOMS[-1].validate()
