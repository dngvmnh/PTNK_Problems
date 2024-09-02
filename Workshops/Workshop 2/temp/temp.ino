#include <OneWire.h>
#include <DallasTemperature.h>
#define SIG_PIN 10

OneWire oneWire(SIG_PIN);
DallasTemperature ds(&oneWire);
void setup() 
{ 
  Serial.begin(9600);
  ds.begin();
}
void loop() 
{
  delay(500);
  ds.requestTemperatures();
  float temp = ds.getTempCByIndex(0);
  Serial.println(temp);
}