//www.elegoo.com

#include <Servo.h>  //servo library
Servo myservo;      // create servo object to control servo

int Echo = A4;  
int Trig = A5; 
int i = 1 ; 
int j = 1 ;

#define ENA 5
#define ENB 6
#define IN1 7
#define IN2 8
#define IN3 9
#define IN4 11
#define carSpeed 150 
int rightDistance = 0, leftDistance = 0, middleDistance = 200;

void forward(){ 
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  Serial.println("Forward");
}

void back() {
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  Serial.println("Back");
}

void left() {
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH); 
  Serial.println("Left");
}

void right() {
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  Serial.println("Right");
}

void stop() {
  digitalWrite(ENA, LOW);
  digitalWrite(ENB, LOW);
  Serial.println("Stop!");
} 

//Ultrasonic distance measurement Sub function
int Distance_test() {
  digitalWrite(Trig, LOW);   
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);  
  delayMicroseconds(20);
  digitalWrite(Trig, LOW);   
  float Fdistance = pulseIn(Echo, HIGH);  
  Fdistance= Fdistance / 58;       
  return (int)Fdistance;
}  

void setup() { 
  myservo.attach(3,700,2400);  // attach servo on pin 3 to servo object
  Serial.begin(9600);     
  pinMode(Echo, INPUT);    
  pinMode(Trig, OUTPUT);  
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  while(middleDistance >= 40)
  {
  myservo.write(90);
  delay(150);
  myservo.write(0);
  delay(150);
  rightDistance = Distance_test();
  myservo.write(90);
  delay(150);
  myservo.write(180);
  delay(150);
  leftDistance = Distance_test();
  myservo.write(90);
  loop() ;
  }
} 

void loop() { 
   if(rightDistance <= 40 && rightDistance < leftDistance)
  {
    stop() ; 
    delay(500);
    left();
    delay(360);
    while(rightDistance <= 40)
    {
      if(rightDistance > 40)
      {
      stop();
      delay(500);
      right();
      }
    break;
    }
  }   
 else if(leftDistance <= 40 && leftDistance < rightDistance)
 {
    stop() ; 
    delay(500);
    right();
    delay(360);
    while(leftDistance <= 40) 
    {
    if(leftDistance > 40)
    {
      stop();
      delay(500);
      left(); 
    }
    break;
    }
 }
 else if(leftDistance == rightDistance) 
        {
          right();
          delay(360) ; 
        }
 else{
  forward();
 }
  
    myservo.write(90);  //setservo position according to scaled value
    delay(500); 
    middleDistance = Distance_test();

    if(middleDistance <= 50) {     
      stop();
      delay(500);                         
      myservo.write(10);          
      delay(1000);      
      rightDistance = Distance_test();
      
      delay(500);
      myservo.write(90);              
      delay(1000);                                                  
      myservo.write(180);              
      delay(1000); 
      leftDistance = Distance_test();
      
      delay(500);
      myservo.write(90);              
      delay(1000);
      if(rightDistance > leftDistance) {
        back();
        delay(100);
        right();
      }
      else if(rightDistance < leftDistance) {
        back();
        delay(100);
        left();
      }
      else if((rightDistance <= 40) || (leftDistance <= 40)) {
        back();
        delay(100);
      }
      else {
        forward();
      }
    }  
    else {
        forward();
    }   
    middleDistance = 200 ;                   
}
