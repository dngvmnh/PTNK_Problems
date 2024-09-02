#include <OneWire.h>
#include <DallasTemperature.h>
#define SIG_PIN 10
OneWire oneWire(SIG_PIN);
DallasTemperature ds(&oneWire);
float V1;
float R2;
float readvalue;
void setup() 
{ 
  Serial.begin(9600);
  ds.begin();
}
void loop() 
{
  delay(500);
  readvalue= analogRead(A1);
  V1= (readvalue*3.3)/1023;
  R2= 330*(3.3-V1)/V1;
  ds.requestTemperatures();
  float temp = ds.getTempCByIndex(0);
  Serial.print(temp);
  Serial.print("  ");
  Serial.println(R2);
}