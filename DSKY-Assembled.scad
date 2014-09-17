use<DSKY-Base.scad>;
use<DSKY-Mid.scad>;
use<DSKY-Keyframe.scad>;
use<DSKY-TopRiser.scad>;
use<DSKY-TopCover.scad>;

numSBars = 5;
sHeight = 100;

color("silver"){
union(){
translate([0,0,0]) dskyBase();
translate([0,0,60]) dskyMid();
translate([0,0,90]) keyframe();
translate([0,0,120]) topRiser();
translate([0,0,160]) topCover();

translate([175,0,0]) dskyBase();
translate([175,0,27]) dskyMid();
translate([175,0,32]) keyframe(); 
translate([175,0,33.8]) topRiser();

translate([175,0,42.4]) topCover();

translate([13,65,160]) square([115, 76]);
translate([187,65,42.5]) square([115, 76]);
}}

