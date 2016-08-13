
import processing.serial.*;
Serial myPort;  // Create object from Serial class
float accX, accY, accZ;
int button=0;
int boxSize=100;


void getSensor()
{
  int lf = 10;    // Linefeed in ASCII
  String myString = null;
  if ( myPort.available() > 0) {  // If data is available,
    myString = myPort.readStringUntil(lf);
    if (myString != null) {
      String[] list = split(myString, '#');
//      print(list);
      if (list.length>4)
      {
      button=int(Float.valueOf(list[0]).floatValue());
      accX=Float.valueOf(list[1]).floatValue();
      accY=Float.valueOf(list[2]).floatValue();
      accZ=Float.valueOf(list[3]).floatValue();
      }
    }
  }
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


void setup() {
  size(960,640,P3D);
  background(0);
  String portName = Serial.list()[3];
  drawAxes();
  print(Serial.list());
  myPort = new Serial(this, portName, 9600);
}


void rotate_from_X(float x,float y, float z)
{
  float r=sqrt(x*x+y*y+z*z);
  rotateZ(atan2(y,x));
  rotateY(-asin(z/r));
//  line(0,0,0,r,0,0);
}

void cubeVector(float accX,float accY,float accZ)
{
  pushMatrix();
  translate(width/2, height/2, 0);
  float r=sqrt(accY*accY+accX*accX+accZ*accZ);
  strokeWeight(3);
  stroke(200,200,200);
  strokeWeight(10);
  rotate_from_X(accX,accY,accZ);
  line(0,0,0,boxSize,0,0);
  if (button>0)
      noFill();
  else
      fill(0,0,255,100);
  box(boxSize*2);
  popMatrix();
  
  
  pushMatrix();
  translate(width/2, height/2, 0);
  strokeWeight(3);
  stroke(255,255,0);
  line(0,0,0,accX*10,accY*10,accZ*10);
  popMatrix();
  
  pushMatrix();
  translate(width*4/5, height*4/5, 0);
  stroke(255,255,0);
  strokeWeight(6);
  strokeCap(ROUND);
  line(0,0,0,accX*10,0,0);
  line(0,0,0,0,accY*10,0);
  line(0,0,0,0,0,accZ*10);
  popMatrix();
}



void draw() {
  background(0);
  getSensor();
  lights(); 
  
  pushMatrix();
  translate(width*4/5, height*4/5, 0);
  drawAxes();
  popMatrix();
  
  cubeVector(accY,accZ,accX);

}


