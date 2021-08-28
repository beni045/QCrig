#include "elapsedMillis.h" //for compression and weight
#include "HX711.h" //for compression and weight
#include "Adafruit_VL53L0X.h" //for time of flight sensors
#define calibration_factor -22.0       //This value is obtained using the SparkFun_HX711_Calibration sketch
#define DOUT  3                     //SCALE AMPLIFIER PINS
#define CLK  2                      //SCALE AMPLIFIER PINS
#define LOX1_ADDRESS 0x30 //address for time of flight sensor 1
#define LOX2_ADDRESS 0x31 //address for time of flight sensor 2
#define SHT_LOX1 7 //set time of flight sensor 1 pin to shutdown
#define SHT_LOX2 8 //set time of flight sensor 2 pin to shutdown
#define stepsPerRevolution 200 //steps per revolution of stepper motor
#define rotation_dist_conv 0.031746   // conversion factor for distance = nRotations * rotation_dist_conv

// LA defs
#define RPWM 5          //LA MOVEMENT PINS   
#define LPWM 6          //LA MOVEMENT PINS
#define Speed 255
#define strokeLength 2.0   
#define probe_radius 19/2  //probe diameter is 1.9cm = 19mm --> radius = 19/2

HX711 scale;
elapsedMillis timeElapsed;

//LA VARIABLES
int sensorPin = A0;       //LA FEEDBACK PINS
int sensorVal;
//int Speed=255;
//float strokeLength = 2.0;         
float extensionLength;
int maxAnalogReading;
int minAnalogReading;
//float probe_radius = 19/2;  //probe diameter is 1.9cm = 19mm --> radius = 19/2
float area_probe = 3.141 * probe_radius * probe_radius;

//Arch variables
int dirPin = 9; //direction pin
int stepPin = 10; //step pin
int limitSwitch1 = 11; //start position switch

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(2000);
   
  pinMode(RPWM, OUTPUT);
  pinMode(LPWM, OUTPUT);
  pinMode(sensorPin, INPUT);
 
  //reset LA by full retraction
  moveToLimit(1);

  //TARES SCALE TO BEGIN READING UPON FIRST LOOP EXECUTION
  tare_Scale();
  
  pinMode(dirPin, OUTPUT);
  pinMode(stepPin, OUTPUT);
  pinMode(limitSwitch1, INPUT);
  pinMode(SHT_LOX1, OUTPUT);
  pinMode(SHT_LOX2, OUTPUT);


  moveToReset();

}




void loop() {

    if (Serial.available() > 0) {
    String command = Serial.readStringUntil(';');

    if (command == "TARE"){
      //Serial.println("Tare");
      tare_Scale();
    }
       
    else if (command == "WEIGHT"){
      float weight = get_weight();
      Serial.print(weight);
    }
    else if (command == "COMPRESSION"){
      float compression = get_compression();
      Serial.print(compression);
    }
    else if (command == "ARCH"){
      float dist_x = Serial.readStringUntil(';').toInt();
      // tof_num -> 1 for left 2 for right
      int tof_num = Serial.readStringUntil(';').toInt();
      int arch = get_arch(dist_x, tof_num);
      Serial.print(arch);
    }
    else {
      Serial.print("COMMAND_ERROR: " + command);
    }
  }
  else {
    delay(100);
  }
}
   
void driveActuator(int Direction){
  switch(Direction){
    case 1:       //extension
      analogWrite(RPWM, Speed);
      analogWrite(LPWM, 0);
      break;
   
    case 0:       //stopping
      analogWrite(RPWM, 0);
      analogWrite(LPWM, 0);
      break;

    case -1:      //retraction
      analogWrite(RPWM, 0);
      analogWrite(LPWM, Speed);
      break;
  }
}

int moveToLimit(int Direction){
  int prevReading=0;
  int currReading=0;
  do{
    prevReading = currReading;
    driveActuator(Direction);
    timeElapsed = 0;
    while(timeElapsed < 200){ delay(1);}           //keep moving until analog reading remains the same for 200ms
    currReading = analogRead(sensorPin);
  }
  while(prevReading != currReading);
  return currReading;
}


void tare_Scale(){
  scale.begin(DOUT, CLK);
  scale.set_scale(calibration_factor); //This value is obtained by using the SparkFun_HX711_Calibration sketch
  scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0
}

float avg_scale_read(){
  //returns the average of numReading readings
  int numReading = 50;
  float reading[numReading];
  float array_sum = 0;
  float array_average = 0;

  //Readings 50x and stores them into array
  for (int i = 0; i < numReading; i++){
    float reading_temp = scale.get_units();
    reading[i] = reading_temp;
    delay(100);
  }

  //Sums all readings in Array
  for (int inc = 0; inc < numReading; inc++){
    array_sum += reading[inc];
  }

  //Divides the sum by count to find average
  array_average = array_sum / numReading;
  return array_average;
  
}

float get_weight(){
  //make sure LA is fully retracted
  moveToLimit(1);
    
  //begin scale reading and average it
  float average_weight_rd = avg_scale_read();
  delay(100);  
  return average_weight_rd;
}


float get_compression(){
  //make sure LA is fully retracted
  moveToLimit(1);

  //zero the scale
  tare_Scale();
  //fully extend LA to begin compression testing
  moveToLimit(-1);
  //delay to have constant force applied for scale
  delay(500);
  //begin scale reading and take average and convert to Newtons
  float average_comp_rd = avg_scale_read();
  //float compression_force = average_comp_rd * 9.81 / 1000;

  //compression stress returns average readings in terms of N/mm^2
  float compression_stress = average_comp_rd / area_probe;

  //once comp test done retract LA again
  moveToLimit(1);
  
  return compression_stress;
  
}
   
//resets bed to origin. Moves bed until limit switch 1 is closed
void moveToReset(){
  //Serial.println(" Moving to start");
  
  while (digitalRead(limitSwitch1) == HIGH) { //switch is open
    digitalWrite(dirPin, HIGH); //backwards
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(2000);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(2000);
  }


}

 int scan(float dist_x, int tof_num){

  float nRotations = dist_x * rotation_dist_conv;
  moveBed(nRotations);
  int arch_height = 10;
  return arch_height;
 }

//moves bed a specific distance
void moveBed(float nRotations){
  digitalWrite(dirPin, LOW); //forwards
  delay(1000);
  
  for (int i = 0; i < int(nRotations*stepsPerRevolution); i++) {
 
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(1000);
    
  }
}

//arch function use time of flight and bed movement
int get_arch(float dist_x, int tof_num){
  moveToReset(); //reset bed to origin
  int arch_height = scan(dist_x, tof_num); //move bed depending on the size of the shoe
  delay(100);
  moveToReset();
  return arch_height;
}
