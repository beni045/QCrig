
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(2000);
}
void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil(';');
       
    if (command == "WEIGHT"){
      int weight = get_weight();
      Serial.print(weight);
    }
    else if (command == "COMPRESSION"){
      int compression = get_compression();
      Serial.print(compression);
    }
    else if (command == "ARCH"){
      int x_distance = Serial.readStringUntil(';').toInt();
      int tof_num = Serial.readStringUntil(';').toInt();
      int arch = get_arch(x_distance, tof_num);
      Serial.print(arch);
    }
    else {
      Serial.print("COMMAND_ERROR");
    }
  }
}


int get_weight(){
  delay(5000);
  return 100;
}

int get_arch(int x_distance, int tof_num){
  delay(5000);
  return 20;
}

int get_compression(){
  delay(5000);
  return 50;
}
