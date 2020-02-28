let theta;

// function getData(amount) {
//   var a;
//   switch (amount) {
//   case "15":
//     a = 15;
//     break;
//   case "30":
//     a = 30;
//     break;
//   case "45":
//     a = 45;
//     break;
//   case "60":
//     a = 60;
//     break;
//   default:
//     a = 15
//   }
// }

var a = 15;

function setup() {
  createCanvas(710, 400);
}

function draw() {
  background(0);
  stroke(255);
  // Let's pick an angle 0 to 90 degrees based on the mouse position
  // var a = 30;
  // Convert it to radians
  theta = radians(a);
  // Start the tree from the bottom of the screen
  translate(width/2,height);
  // Draw a line 120 pixels
  line(0,0,0,-120);
  // Move to the end of that line
  translate(0,-120);
  // Start the recursive branching!
  branch(120);

}

function branch(h) {
    // Each branch will be 2/3rds the size of the previous one
    h *= 0.66;
  
    // All recursive functions must have an exit condition!!!!
    // Here, ours is when the length of the branch is 2 pixels or less
    if (h > 2) {
      push();    // Save the current state of transformation (i.e. where are we now)
      rotate(theta);   // Rotate by theta
      line(0, 0, 0, -h);  // Draw the branch
      translate(0, -h); // Move to the end of the branch
      branch(h);       // Ok, now call myself to draw two new branches!!
      pop();     // Whenever we get back here, we "pop" in order to restore the previous matrix state
  
      // Repeat the same thing, only branch off to the "left" this time!
      push();
      rotate(-theta);
      line(0, 0, 0, -h);
      translate(0, -h);
      branch(h);
      pop();
    }
  }

  function mousePressed() {
    if (a < 60) {
      a+=15;
    }
    else {
      a = 15;
    }
    redraw();
  }