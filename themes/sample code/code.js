// Wait for DOM to load
document.addEventListener("DOMContentLoaded", function(event) {
  // Put the button into a variable
  var e = document.getElementById("myForm");
  var msg = "";
  // Wait for user to click the button
  e.addEventListener( "change", function() {
    // Put the selected value into a variable
    var myColor = this.color.value;
    
    // The "If Else If" statement.
    if (myColor == "Blue") {
      msg = "Just like the sky!";
    } else if (myColor == "Red") {
      msg = "Quite daring!";
    } else if (myColor == "Green") {
      msg = "Like... grass?";
    }   
    
    // Output message
    document.getElementById("msg").innerHTML = msg;
    
  }, false);
});