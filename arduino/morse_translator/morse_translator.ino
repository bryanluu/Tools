/*
 * Written by Bryan Luu for fun
 * Encodes Latin Serial Input to Morse LED transmission
 */
 
#define MORSE_CHARACTERS 36 // number of alphanumeric characters
#define UNIT_PULSE_TIME 250 // pulse time of a unit (dot) in milliseconds
#define INVALID_CHARACTER(c) ("[" + String(c) + "]") // what to show if character is invalid

const char * dict[MORSE_CHARACTERS];

const char * encode(char c);
void dot();
void dash();
int transmit(const char * code);

void setup() {
  // Numerics [0-9]
  dict[0] = "-----";
  dict[1] = ".----";
  dict[2] = "..---";
  dict[3] = "...--";
  dict[4] = "....-";
  dict[5] = ".....";
  dict[6] = "-....";
  dict[7] = "--...";
  dict[8] = "---..";
  dict[9] = "----.";
  // Alphabet [A-Z]
  dict[10] = ".-";
  dict[11] = "-...";
  dict[12] = "-.-.";
  dict[13] = "-..";
  dict[14] = ".";
  dict[15] = "..-.";
  dict[16] = "--.";
  dict[17] = "....";
  dict[18] = "..";
  dict[19] = ".---";
  dict[20] = "-.-";
  dict[21] = ".-..";
  dict[22] = "--";
  dict[23] = "-.";
  dict[24] = "---";
  dict[25] = ".--.";
  dict[26] = "--.-";
  dict[27] = ".-.";
  dict[28] = "...";
  dict[29] = "-";
  dict[30] = "..-";
  dict[31] = "...-";
  dict[32] = ".--";
  dict[33] = "-..-";
  dict[34] = "-.--";
  dict[35] = "--..";
  // Initialize the Serial port
  Serial.begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
}

char c = 0; // the current character under consideration
char * r = NULL; // the translation result

void loop() {
  if (Serial.available() > 0)
  {
    String line = Serial.readStringUntil('\n');
    Serial.println("Message: " + line);
    Serial.print("Code: ");
    for (byte i = 0; i < line.length(); i++)
    {
      c = line.charAt(i);
      if (c == ' ')
      {
        Serial.print("|");
        delay(7 * UNIT_PULSE_TIME);
      } else {
        r = (char *) encode(c);
        if (r != NULL)
        {
          Serial.print(r);
          transmit(r);
          delay(3 * UNIT_PULSE_TIME);
        } else {
          Serial.print(INVALID_CHARACTER(c));
        }
        if (i < line.length() - 1)
          Serial.print(",");
        else
          Serial.println();
      }
    }
  }
}

/*
 * Translates the given alphanumeric character into a Morse sequence
 */
const char * encode(char c)
{
  if ((c >= '0') && (c <= '9'))
  {
    return dict[c - '0'];
  }
  else if ((c >= 'A') && (c <= 'Z'))
  {
    return dict[c - 'A' + 10];
  }
  else if ((c >= 'a') && (c <= 'z'))
  {
    return dict[c - 'a' + 10];
  }
  else
  {
    return NULL;
  }
}

/*
 * Transmits the given Morse sequence via the LED with the correct sequence of dots and dashes
 */
int transmit(const char * code)
{
  byte len = strlen(code);
  for(int i = 0; i < len; i++)
  {
    if(code[i] == '.')
      dot();
    else if(code[i] == '-')
      dash();
    else
      return -1; // error out!
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
    if(i < len - 1)
      delay(UNIT_PULSE_TIME);
  }
  return 0;
}

void dot()
{
  digitalWrite(LED_BUILTIN, HIGH);    // turn the LED on by making the voltage HIGH
  delay(UNIT_PULSE_TIME);
}

void dash()
{
  digitalWrite(LED_BUILTIN, HIGH);    // turn the LED on by making the voltage HIGH
  delay(3 * UNIT_PULSE_TIME);
}
