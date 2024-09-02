//* Linh kiện điện tử: đèn LED kết nối với chân D10.
int ledPin = 10;

void setup() 
{
  pinMode(ledPin, OUTPUT );
  Serial.begin(9600);
}

void loop() 
{
  while (Serial.available()){
     char signal = Serial.read();
     if (signal == '1'){
       digitalWrite(ledPin, HIGH);
       if (signal =='2' ){
         analogWrite(ledPin,100);
       }
     } else if (signal == '0'){
       digitalWrite(ledPin, LOW);
     }
  }
  delay(30);
}