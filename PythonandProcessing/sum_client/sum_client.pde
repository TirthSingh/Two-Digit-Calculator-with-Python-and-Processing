import (link unavailable)*;

Client client;

void setup() {
  size(200, 200);
  client = new Client(this, "localhost", 12345);
}

void draw() {
}

void mousePressed() {
  // Send numbers to Python
  int num1 = int(random(1, 100));
  int num2 = int(random(1, 100));
  client.write(num1 + "," + num2);
  
  // Receive result from Python
  if (client.available() > 0) {
    String result = client.readString();
    println("Sum: " + result);
    fill(0);
    textSize(32);
    textAlign(CENTER, CENTER);
    text("Sum: " + result, width/2, height/2);
  }
}
