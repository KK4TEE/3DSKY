module keyframe()
{
	difference() {
		cube([136, 150, 1.8]);

		//Keyboard
		translate([27, 6, 0]){
			keyrow(5, 3);}
		translate([8, 15, 0]){
			keyrow(1, 2);}
		translate([119, 15, 0]){
			keyrow(1, 2);}
			 
		// Status Bars
		for (numSBars = [1:+1:numSBars]) {
			translate([12, 60 +(numSBars*2)+ (numSBars*12),0]){
				cube([30, 12, 1.8]);}
		}

		//7seg Displays
			translate([59, 77,0]){
				cube([61, 63, 20]);}
			//translate([58, 80,0]){
				//cube([82, 60, 20]);}

		//Screw Holes
		translate([6, 6,0]){
				cylinder(h=4,r=2, center=true, $fn=100);}
		translate([130, 6,0]){
				cylinder(h=4,r=2, center=true, $fn=100);}
		translate([6, 144,0]){
				cylinder(h=4,r=2, center=true, $fn=100);}
		translate([130, 144,0]){
				cylinder(h=4,r=2, center=true, $fn=100);}
		translate([6, 68,0]){
				cylinder(h=4,r=2, center=true, $fn=100);}
		translate([130, 68,0]){
				cylinder(h=4,r=2, center=true, $fn=100);}
		translate([68, 68,0]){
				cylinder(h=4,r=2, center=true, $fn=100);}
		translate([68, 144,0]){
				cylinder(h=4,r=2, center=true, $fn=100);}
		}
}

module keycap(x,y){
//The true key is 14mm, but I had to enlarge the 
//cut due to the tolerances of my 3d printer
	keyDepth = 5;
	translate([x-7.0, y-7.0, 0] ){
		union(r = 0){
            linear_extrude(height = keyDepth){
                square( size = [14.0,14.0], r = 0.2 );
            }

            translate( [1.0, -0.8, 0] ){
                cube( size = [3.5,15.6,keyDepth], r = 0 );
            }

            translate( [9.5, -0.8, 0] ){
                cube( size = [3.5,15.6,keyDepth], r = 0 );
            }

        }
	}
}

module keyrow(numx, numy){
	for (numy = [1:+1:numy]) {
		for (numx = [1:+1:numx]) {
			keycap((4.25*numx)+(14*(numx-1)), 4.25*numy + (14*(numy-1))+7.0);
		}
	}
}
numSBars = 5;
keyframe();