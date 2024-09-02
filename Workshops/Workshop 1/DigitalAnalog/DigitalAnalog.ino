//* Linh kiện điện tử: đèn LED kết nối với chân D10, nút bấm nối với chân D11.
int button = 11;
boolean buttonState = 0;
int led = 10;

void setup()
{
  pinMode(button, INPUT);
  pinMode(led, OUTPUT );
}

void loop()
{
  buttonState = digitalRead(button);
	if (buttonState == 0){ //nếu nút bấm đang được nhấn
		digitalWrite(led, HIGH);  //thì bật đèn LED
	} else digitalWrite(led, LOW); //nếu không thì tắt đèn
}
//*Kết quả: Đèn luôn sáng và chỉ tắt khi bấm nút.