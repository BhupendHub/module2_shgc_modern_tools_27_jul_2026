// Pins mapping for LED hardware
const int RED_LED = 13;
const int YELLOW_LED = 12;
const int GREEN_LED = 8;
const int BLUE_LED = 12;

void _____() {
  // Open Serial interface pipe matching Python's baud rate
  Serial.begin(9600);
  
  // Set pins to output configuration
  pinMode(RED_LED, OUTPUT);
  pinMode(YELLOW_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  
  // Start up animation sequence - Flash once
  turnAllOff();
}

void _____() {
  // Listen continuously for arriving computer command bytes
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();
    
    // Evaluate incoming command configurations
    if (receivedChar == 'R') {
      turnAllOff();
      digitalWrite(RED_LED, HIGH);
    } 
    else if (receivedChar == 'Y') {
      turnAllOff();
      digitalWrite(YELLOW_LED, HIGH);
    } 
    else if (receivedChar == 'G') {
      turnAllOff();
      digitalWrite(GREEN_LED, HIGH);
    } 
    else if (receivedChar == 'B') {
      turnAllOff();
      digitalWrite(BLUE_LED, HIGH);
    }
  }
}

// Helper to keep pin switching loops exceptionally clean
void turnAllOff() {
  digitalWrite(RED_LED, LOW);
  digitalWrite(YELLOW_LED, LOW);
  digitalWrite(GREEN_LED, LOW);
  digitalWrite(BLUE_LED, LOW);
}
