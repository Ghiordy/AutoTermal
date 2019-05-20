/*
 * READING PANEL OF CONTROL
 * 
 * PUSH BUTTONS CONNECTED TO A0 PIN
 */

// defining input signal
int PIN = A0;

// Values in A0 to options
/*  0   < right < 20
 *  140 < up    < 150
 *  340 < down  < 350
 *  510 < left  < 520
 *  730 < selec < 740
 *  none > 1000
 */

void setup() {
  pinMode(PIN,INPUT);
  //Serial1.begin(9600);
  //Serial2.begin(9600);
  //Serial3.begin(9600);
}

void loop() {
  int p = analogRead(PIN);
  delay(250);
  if(p < 20){
    // RIGHT
  }
    else if (p > 140 && p < 150){
      // UP
    }
      else if (p > 340 && p < 350){
        // DOWN
      }
        else if (p > 510 && p < 520){
          // LEFT
        }
          else if (p > 730 && p < 740){
            // SELECT
          }
            else if (p > 1000){
              // NONE
            }
}
