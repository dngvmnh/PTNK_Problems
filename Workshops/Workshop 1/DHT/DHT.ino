#include <DHT.h>

const int DHTPIN = 11; //khởi tạo chân cảm biến DHT là chân 2      
const int DHTTYPE = DHT11; 
DHT dht(DHTPIN, DHTTYPE); 
  
void setup()
{
  Serial.begin(9600);
  dht.begin(); //khởi động cảm biến DHT
}

void loop(){
  float t = dht.readTemperature(); //đọc giá trị nhiệt độ vào biến t
  float h = dht.readHumidity(); //đọc giá trị độ ẩm vào biến h   
  Serial.print("nhiet do ");
  Serial.print(t );
  Serial.println(" *c ");
  Serial.print("do am ");
  Serial.print(h);
  Serial.println(" % ");
  delay(1000);

}