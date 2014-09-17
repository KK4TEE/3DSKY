module dskyMid(tHeight){
difference() {
 union(){
	difference() {
		cube([136, 150, tHeight]);
		translate([10, 10, 0]){
			cube([110, 130, 29]);}

		translate([4, 10, 0]){
			cube([128, 54, 29]);}
		translate([4, 72, 0]){
			cube([128, 67, 29]);}

		translate([10, 4, 0]){
			cube([116, 142, 29]);}
		 

		
	}
	//middle screw support
	translate([0, 64, 0]){
		cube([130, 2, tHeight]);}
	translate([64, 66, 0]){ //center
		cube([8, 6, tHeight]);}
	translate([64, 140, 0]){ //upper mid
		cube([8, 9, tHeight]);}
	

	difference() {
		//Support Floor
		translate([0, 64, 0]){
				cube([136, 85, 2]);}

		// Status Bar LEDs
		for (numSBars = [1:+1:numSBars+1]) {
			translate([30.5, 66 +(numSBars*14),0]){
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
		}
		for (numSBars = [1:+1:numSBars+1]) {
			translate([23.5, 66 +(numSBars*14),0]){
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
		}
	}

	//7seg + alerts divider
	translate([42, 64, 2]){
			cube([2, 85, tHeight-2]);}
	translate([10, 64, 2]){
			cube([2, 85, tHeight-2]);}
	// Status Bars
	for (numSBars = [1:+1:numSBars+1]) {
		translate([10, 58 +(numSBars*14),2]){
			cube([34, 2, tHeight-2]);}
		}
	//extra support for front wall
		translate([10, 4, 0]){
			cube([116, 6, 2]);}
 		translate([66.5, 4, 0]){
			cube([3, 4, tHeight]);}

	}	
//Screw Holes
		translate([6, 6,0]){
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
		translate([130, 6,0]){
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
		translate([6, 144,0]){
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
		translate([130, 144,0]){
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
		translate([6, 68,0]){
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
		translate([130, 68,0]){
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
		translate([68, 144,0]){
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
		translate([68, 68,0]){
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
		translate([49, 75, 0]){ //left 7seg wire pass
			cube([9, 64, 2,]);}
		translate([118, 75, 0]){ //right 7seg wire pass
			cube([6, 64, 2,]);}
		translate([81, 77, 0]){ //IC cutout
			cube([18, 60, 2]);}
//background LED Cutouts
		translate([90.5, 143,0]){ //top
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
		translate([90.5, 70,0]){  //bottom
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
/*			for (numLEDs = [1:+1:3]) { //surounding
			translate([47, 74 +(numLEDs*16),2]){ //left
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
			translate([128, 74 +(numLEDs*16),2]){//right
				cylinder(h=sHeight,r=2, center=true, $fn=100);}
			}
*/

		//translate([47, 106,0]){ //left
		//		cylinder(h=sHeight,r=2, center=true, $fn=100);}
		//translate([128, 106,0]){//right
		//		cylinder(h=sHeight,r=2, center=true, $fn=100);}
}
}

numSBars = 5;
sHeight = 100;
dskyMid(5);