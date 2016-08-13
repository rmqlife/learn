
#include "Wire.h"

#include "I2Cdev.h"
#include "ADXL345.h"
#include "HMC5883L.h"
#include "ITG3200.h"

HMC5883L mag;
ITG3200 gyro;
ADXL345 accel;

int16_t results[10];    

// class default I2C address is 0x53
// specific I2C addresses may be passed as a parameter here
// ALT low = 0x53 (default for SparkFun 6DOF board)
// ALT high = 0x1D

#define LED_PIN 13 // (Arduino is 13, Teensy is 6)
#define BUTTON_PIN 8 

void setup() {
    // join I2C bus (I2Cdev library doesn't do this automatically)
    Wire.begin();
    // initialize serial communication
    // (38400 chosen because it works as well at 8MHz as it does at 16MHz, but
    // it's really up to you depending on your project)
    Serial.begin(9600);
    // initialize device
    Serial.println("Initializing I2C devices...");
    accel.initialize();
    // verify connection
    Serial.println("Testing device connections...");
    Serial.println(accel.testConnection() ? "ADXL345 connection successful" : "ADXL345 connection failed");
    // configure LED for output
    pinMode(LED_PIN, OUTPUT);
    mag.initialize();
    gyro.initialize();
    Serial.println("Testing device connections...");
    Serial.println(mag.testConnection() ? "HMC5883L connection successful" : "HMC5883L connection failed");
}

void write2serial(void)
{
  for(int i=0;i<10;i++){
    Serial.print(results[i]);
    Serial.print("#");
  }
  Serial.println();
}

void loop() {
    int16_t ax, ay, az;
    int16_t mx, my, mz;
    int16_t gx, gy, gz;
    // read raw accel measurements from device
    accel.getAcceleration(&ax, &ay, &az);
    mag.getHeading(&mx, &my, &mz);
    gyro.getRotation(&gx, &gy, &gz);
    
    results[0]=ax;
    results[1]=ay;
    results[2]=az;
    
    results[3]=mx;
    results[4]=my;
    results[5]=mz;
    
    results[6]=gx;
    results[7]=gy;
    results[8]=gz;
    
    
    int button=digitalRead(BUTTON_PIN);
    if (button==0) //unpressed
      digitalWrite(LED_PIN,HIGH);
    else
      digitalWrite(LED_PIN,LOW);
    
    results[9]=button;
    write2serial();
    delay(10);
}
