module frame(){
	translate( [0,0, -1.2/2] )
		cube( size=[15.6,15.6,1.2], center=true );
	translate( [0,0, 5.1/2] ){
		difference(){
			cube( size=[16,16,5.1], center=true );
			cube( size=[15,15,5.1], center=true );
		}
	}
}

module stem(){
	height = 5.1;
	translate([0,0,height/2]){
		difference(){
			cylinder( h=height, r=5.6/2, center=true, $fn=360 );
			cube( size=[1.6,4.4,height+2], center=true );
			cube( size=[4.4,1.6,height+2], center=true );
		}
	}
}

frame();
stem();
