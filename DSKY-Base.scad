use<dls/dev_boards.scad>;
module dskyBase()
{
difference() {
 union(){
	difference() {
		cube([136, 150, 27]);
		translate([10, 10, 2]){
			cube([110, 130, 29]);}

		translate([4, 10, 2]){
			cube([128, 54, 29]);}
		translate([4, 72, 2]){
			cube([128, 67, 29]);}

		translate([10, 4, 2]){
			cube([116, 142, 29]);}
		 

		
	}
	//middle screw support
	translate([64, 64, 0]){ //center
		cube([8, 8, 27,]);}
	translate([64, 140, 0]){ //upper mid
		cube([8, 9, 27,]);}
	translate([65, 4, 0]){ //lower mid
		cube([6, 6, 27,]);}

	//Arduino support
		translate([10, 146,2]){ //top left corner
			arduinoMounts(3.1,3);
			}
	//Arduino Mockups
	//translate([37,94,4])rotate(180){arduino_mega();}
	//translate([37,112,4])rotate(180)arduino_uno();

 			
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
		//USB
		translate([41.7, 145.9, 5]){
			cube([13.4, 15, 12.2]);}
		//Power
		translate([12.4, 145.9,5]){ 
			cube([11.6, 15, 12.2]);}


	//Arduino Mounts
		translate([10, 146,2]){ //top left corner
			arduinoMounts(3.1,1.3);
			}
}
}


module arduinoMounts(hightIN, radiusIN){
//Arduino support, DC jack is near the origin
		translate([2.9, -15.7, (hightIN/2)-0.5]){ //top left
				cylinder(h=hightIN,r=radiusIN+0.1, center=true, $fn=100);}
		translate([51.2, -16.4, (hightIN/2)-0.5]){ //top right
				cylinder(h=hightIN,r=radiusIN, center=true, $fn=100);}
		translate([8.0, -66.9,(hightIN/2)-0.5]){ //bottom left
				cylinder(h=hightIN,r=radiusIN, center=true, $fn=100);}
		translate([36.0, -66.7, (hightIN/2)-0.5]){ //bottom right
				cylinder(h=hightIN,r=radiusIN, center=true, $fn=100);}
	//mega extension
		translate([3, -97.6, (hightIN/2)-0.5]){ //mega bottom left
				cylinder(h=hightIN,r=radiusIN, center=true, $fn=100);}
		translate([50.6, -91.4, (hightIN/2)-0.5]){ //mega bottom right
				cylinder(h=hightIN,r=radiusIN, center=true, $fn=100);}

}

sHeight = 100;
dskyBase();

 
