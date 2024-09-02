//* Linh kiện điện tử: quang trở kết nối với chân A1, đèn LED với chân D10
void setup()
{
  pinMode(10, OUTPUT);
}

void loop()
{
  int analogIn = analogRead(A1); //đọc giá trị của cảm biến từ chân A1
  analogWrite(10, analogIn/4); //sử dụng gía trị của cảm biến để điều khiển đèn LED  
  delay(50);
}
//* Kết quả: đọc được giá trị từ quang trở và dùng để điều khiển đèn LED