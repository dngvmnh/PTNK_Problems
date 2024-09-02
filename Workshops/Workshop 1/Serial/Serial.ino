//* Linh kiện điện tử: quang trở kết nối với chân A1.
void setup()
{
  Serial.begin(9600); //khởi động giao thức Serial truyền nhận dữ liệu với máy tính
}

void loop()
{
  int sensorValue = analogRead(A1); //đọc giá trị cảm biến từ chân A1
  Serial.print("sensor value = ");
  Serial.println(sensorValue); //gửi giá trị đọc từ cảm biến về máy tính, sử dụng Serial Monitor để đọc giá trị
  delay(500);
}
//* Kết quả: đọc được quang trở tín hiệu Arduino trong mỗi 500 miligiây.