#include <DIYables_MultiFuncSh__________.h>

// Your message surrounded by 4 padding spaces on each side
Str____ message = "  I LouE IoT  ";
Str____ message2="  BHUPENDRA  ";
char *msg[] = { "I", "LOuE", "SHGC" };
int messageLength = message.length();
int messageLength2=message2.length();
int currentIndex = 0;
int count = 0, sequence = 0;
unsigned long lastScrollTime = 0;
const int scrollSpeed = 500;  // Time in milliseconds between text shifts
uint8_t step = 0;
unsigned long lastUpdate = 0;
void setup() {
  MFS.begin();
}

void loop() {
  MF__.loop();  // Must be called constantly to update the hardware display
  
  /* if (millis() - lastUpdate >= 3000) {
     lastUpdate = millis();
     MFS.display.print(msg[step]);
     step=(step+1)%3;
  }*/
  // for (step = 0; step < 3; step++) {
  if (millis() - lastUpdate >= 1000) {
    lastUpdate = millis();
    MFS.buzz___r.beep(80);
    if (sequence == 0) {
      MFS.display.print(msg[step]);
      step++;
      if (step == 3) {
        sequence = 1;
        step = 0;
      }
    } else if (sequence == 1) {
      // Pull a 4-character window out of our larger string message

      String displayWindow = message.substring(currentIndex, currentIndex + 4);
      // Print that specific 4-character window to the 4-digit display
      MFS.dis____.print(displayWindow.c_str());

      // Advance the frame marker
      currentIndex++;

      // Reset when the text has fully scrolled past the screen
      if (currentIndex > messageLength - 4) {
        currentIndex = 0;
        //sequence=0;//
        sequence = 2;
      }
      //delay(500);
    }  //
    else if (sequence == 2) {
      // Pull a 4-character window out of our larger string message

      String displayWindow = message2.substring(currentIndex, currentIndex + 4);
      // Print that specific 4-character window to the 4-digit display
      MFS.display.print(displayWindow.c_str());

      // Advance the frame marker
      curr___Index++;

      // Reset when the text has fully scrolled past the screen
      if (currentIndex > messageLength2 - 4) {
        currentIndex = 0;
        sequence = 0;
      }
      //delay(500);
    } 
  }
}
  /*
#include <DIYables_MultiFuncShield.h>
uint8_t step = 0;
unsigned long lastUpdate = 0;
char *msg[] = { "I", "LOuE", "SHGC" };
void setup() {
  MFS.begin();
}

void loop() {
  MFS.loop();

  if (millis() - lastUpdate >= 3000) {
    lastUpdate = millis();

    // 1. Display "I   "
    MFS.display.print(msg[step]);
    step = (step + 1) % 3;
    //delay(1000);

    // 2. Display "LouE" (Best representation of LOVE)
    //MFS.display.print("LouE");
    //delay(1000);

    // 3. Display "you"
    //MFS.display.print("SHGC");
    //delay(1000);

    // 4. Clear screen before restarting loop
    //MFS.display.clear();
    //delay(500);
  }
}
*/