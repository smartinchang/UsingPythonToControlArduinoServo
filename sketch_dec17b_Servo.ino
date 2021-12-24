#include <Servo.h>
Servo myServo;
int servoAngle = 0;
int incomingByte = 0;
String received = "";

void setup() {
  Serial.begin(9600);
  myServo.attach(3);
  myServo.write(0);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 97) {
      Serial.print("I received: ");
      Serial.println(received);
      servoAngle = received.toInt();
      myServo.write(servoAngle);
      received = "";
    } else {
      received.concat(char(incomingByte));
    }
  }
}
