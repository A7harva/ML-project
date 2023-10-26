#define python Serial// Assign python variable as Serial 
#define m1 6//motor pin number
#define m2 7
String IncomingData = "";//variable for receiving data

void setup() {
  // put your setup code here, to run once:
  python.begin(115200);//serial communication between python and microcontroller
  python.println("Ready");//transmit data to python and check it's connected perfectly

  pinMode(m1, OUTPUT);//declare motor pin as output
  pinMode(m2, OUTPUT);
  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);// initially turn off motor


}
void loop() {
  // put your main code here, to run repeatedly:
  while (python.available())//check if there is any incoming data is available or not if it's available
  {
    IncomingData = python.readString();//read the incoming data

    delayMicroseconds(5);
  }
  if (IncomingData.length() > 0) {//if incoming data byte is greater than zero

    if (IncomingData == "1") {//if received is equal to one show the display and alert via buzzer

      digitalWrite(m1, HIGH);
      digitalWrite(m2, LOW);
      delay(3000);
      digitalWrite(m1, LOW);
      digitalWrite(m2, LOW);
    }

    IncomingData = "";
  }
}
