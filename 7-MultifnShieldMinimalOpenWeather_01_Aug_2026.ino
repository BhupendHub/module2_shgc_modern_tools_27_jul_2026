#include <DIYables_MultiFuncShield.h>
int previous = 0, value = 0, nLed = 0;
float temp;
void setup() {
  MFS.begin();
  Serial.begin(9600);
  MFS.display.print("TecD");
}

void loop() {
  MFS.loop();

  if (Serial.available() > 0) {
    String incomingData = Serial.readStringUntil('\n');
    incomingData.trim();
    // Only proceed if there is an actual number left to parse (ignores empty newlines)
    if (incomingData.length() > 0) {
      // Convert the clean string into a float
      temp = incomingData.toFloat();
      // Read the incoming float until a newline character is received
      value = (int)temp;
    }
    if (value != previous) {
      MFS.display.print(value);
      MFS.allLedsOn();
        previous = value;
      MFS.buzzer.beep(80, 80);

    } else {

      MFS.allLedsOff();
      MFS.buzzer.stop();
    }
  }
}