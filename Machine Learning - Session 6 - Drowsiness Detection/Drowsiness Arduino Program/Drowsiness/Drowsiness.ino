#define python Serial// Assign python variable as Serial 
#define buz 7 //buz pin number
String IncomingData = "";//variable for receiving data

void setup() {
  // put your setup code here, to run once:
  python.begin(115200);//serial communication between python and microcontroller
  python.println("Ready");//transmit data to python and check it's connected perfectly
  
  pinMode(buz, OUTPUT);//declare buzzer as output
  digitalWrite(buz, LOW);// initially turn off buzzer


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
     
      digitalWrite(buz, HIGH);
    }

    IncomingData = "";
  }
}
