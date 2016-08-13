
import processing.serial.*;
Serial myPort;  // Create object from Serial class
float accX, accY, accZ, magX, magY, magZ, gyrX, gyrY,gyrZ;
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
      if (list.length>8)
      {
      button=int(Integer.valueOf(list[9]));
      accX=Float.valueOf(list[0]).floatValue()/25;
      accY=Float.valueOf(list[1]).floatValue()/25;
      accZ=Float.valueOf(list[2]).floatValue()/25;
      
      magX=Float.valueOf(list[3]).floatValue();
      magY=Float.valueOf(list[4]).floatValue();
      magZ=Float.valueOf(list[5]).floatValue();
      
      gyrX=Float.valueOf(list[6]).floatValue();
      gyrY=Float.valueOf(list[7]).floatValue();
      gyrZ=Float.valueOf(list[8]).floatValue();
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
  String portName = Serial.list()[4];
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

void accCube(float accX,float accY,float accZ)
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
  drawAxes();
  stroke(255,255,0);strokeWeight(6);strokeCap(ROUND);
  line(0,0,0,accX*10,0,0);
  line(0,0,0,0,accY*10,0);
  line(0,0,0,0,0,accZ*10);
  popMatrix();
}


void magCube(float x, float y, float z)
{
  pushMatrix();
  translate(width*4/5, height*1/5, 0);
  drawAxes();
  stroke(0,255,255);strokeWeight(6);strokeCap(ROUND);
  float r=sqrt(x*x+z*z);
  float x1=x/r*100;
  float z1=z/r*100;  
  line(0,0,0,x1,0,0);
  line(0,0,0,0,0,z1);
  line(0,0,0,x1,0,z1);
  popMatrix();
}

void gyrCube(float x,float y,float z)
{
  pushMatrix();
  translate(width*1/5, height*1/5, 0);
  drawAxes();
  stroke(0,255,255);strokeWeight(6);strokeCap(ROUND);
  float r=sqrt(x*x+y*y+z*z);
  float x1=x/r*100;
  float z1=z/r*100;  
  line(0,0,0,x,0,0);
  line(0,0,0,0,y,0);
  line(0,0,0,0,0,z);
  popMatrix();

}



void draw() {
  background(0);
  getSensor();
  lights(); 
  
  accCube(accY,accZ,accX);
  magCube(magY,magZ,magX);
  gyrCube(gyrY,gyrZ,gyrX);
}


