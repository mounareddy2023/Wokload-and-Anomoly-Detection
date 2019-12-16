#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into digital pin 2 on the Arduino
#define ONE_WIRE_BUS 2

// Setup a oneWire instance to communicate with any OneWire device
OneWire oneWire(ONE_WIRE_BUS);  

// Pass oneWire reference to DallasTemperature library
DallasTemperature sensors(&oneWire);


const int xpin = A0;// analog pin of accelerometor sensor                 
const int ypin = A1;// analog pin of accelerometor sensor                 
const int zpin = A2;// analog pin of accelerometor sensor                  
const int trigPin = 7;// digital pin of ultrasonic sensor
const int echoPin = 6;// digital pin of ultrasonic sensor
int Vib_SidePin =9;// digital pin of Vibration sensor placed at side
int Vib_topPin =12;// digital pin of Vibration sensor placed at top
float duration, distance;

void setup() {
               //sensors.begin();  // Start up the library
               pinMode(trigPin, OUTPUT);// ultrasonic sensor
               pinMode(echoPin, INPUT);// ultrasonic sensor
               Serial.begin(9600);// activate sensor (9600 is the baud rate)
             }

void loop() {
  
              long Vib_Side= pulseIn(Vib_SidePin,HIGH);
              long Vib_top= pulseIn(Vib_topPin,HIGH);


// Vibration side              
              Serial.print(",");
              //Serial.print("Vib_Side = ");
              Serial.print(Vib_Side);
              
// Vibration top              
              Serial.print(",");
              //Serial.print("Vib_top = ");
              Serial.print(Vib_top);



// Distance measure  
              Serial.print(",");
              digitalWrite(trigPin, LOW);
              delayMicroseconds(2);
              digitalWrite(trigPin, HIGH);
              delayMicroseconds(10);
              digitalWrite(trigPin, LOW);
              duration = pulseIn(echoPin, HIGH);
              distance = (duration*.0343)/2;
              //Serial.print("Distance: ");
              Serial.print(distance);
                
// Accelometer readings
              Serial.print(",");
              //Serial.print("x = ");
              Serial.print(analogRead(xpin));
              // print a tab between values:
              Serial.print(",");
              //Serial.print("y = ");
              Serial.print(analogRead(ypin));
              // print a tab between values:
              Serial.print(",");
              //Serial.print("z = ");
              Serial.print(analogRead(zpin));
              Serial.println();


              delay(1000);

}
