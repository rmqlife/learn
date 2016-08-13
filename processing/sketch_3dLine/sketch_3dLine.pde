  
void setup() {
  size(960,640,P3D);
  background(0);

}

void drawAxes()
{
  strokeWeight(3);
  int axelength=100;
  stroke(255,0,0);
  line(-axelength,0,0,axelength,0,0);
  stroke(0,255,0);
  line(0,-axelength,0,0,axelength,0);
  stroke(0,0,255);
  line(0,0,-axelength,0,0,axelength);
}

void sameLine(float x,float y, float z)
{
  stroke(255,255,0);
  float r=sqrt(x*x+y*y+z*z);
//  rotateY(-acos(sqrt(x*x+y*y)/r) );
//  rotateZ(+acos(x/sqrt(x*x+y*y)));
  rotateZ(atan2(y,x));
  rotateY(-asin(z/r));

  line(0,0,0,r,0,0);

}

float dz=0;
void draw() {
  background(0);
  lights(); 
  
  pushMatrix();
  translate(mouseX, mouseY, 0);
  drawAxes();
  
//  dz=dz+0.01;
//  rotateZ(dz);
   
  stroke(200,200,200);
  float x=30,y=-50,z=30;
  
  float r=sqrt(x*x+y*y+z*z);

  line(0,0,0,x,y,z);
  
  sameLine(x,y,z);  
  
  popMatrix();

}
