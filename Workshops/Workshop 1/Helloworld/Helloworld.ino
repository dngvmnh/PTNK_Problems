//* Linh kiện điện tử: đèn LED kết nối với chân D10, nút bấm nối với chân D11.
int ledPin = 10; //khai báo biến ledPin = 10 (sử dụng chân D10 để điều khiển đèn LED thông qua biến ledPin)

void setup() 
{
  pinMode(ledPin, OUTPUT );//khởi động việc sử dụng chân ledPin (chân D10)  
}

void loop() 
{
  digitalWrite(ledPin, HIGH ); //bật đèn LED
  delay(1000); //dừng 1 giây = duy trì bật đèn LED 1 giây 
  digitalWrite(ledPin, LOW ); //tắt đèn LED
  delay(1000); //dừng 1 giây = duy trì tắt đèn LED 1 giây 
}
//chương trình lặp lại liên tục