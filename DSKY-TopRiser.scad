use<DSKY-Mid.scad>;

module topRiser()
{
	difference() {
		translate([0,0,-5]) dskyMid(thickness+5);
		translate([0,0,-5]) cube([136, 150, thickness]); 
		translate([2, 15,0]) cube([132, 40, thickness]); 
	//extra support for front wall
 		translate([66.5, 4, 0]){
			cube([3, 4, 7]);}

		}
}

thickness = 9.8;
numSBars = 5;
topRiser();