
float V1;
float R2;
float readvalue;
void setup() 
{ 
  Serial.begin(9600);
}
void loop() 
{
  delay(500);
  readvalue= analogRead(A1);
  V1= (readvalue*3.3)/1023;
  R2= 330*(3.3-V1)/V1;
  Serial.println(R2);
}