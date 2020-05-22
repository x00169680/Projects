function validation()
{
    var x = document.getElementById("name").value;
    var y = document.getElementById("email").value;
    var z = document.getElementById("message").value;
  
  if (x == null || x == "")
  {
  alert("Name must be filled out");
  return false;
  }
  
  else if (y == null || y == "")
  {
  alert("Valid email must be filled out");
  return false;
  }
  
  else if (z == null || z == "")
  {
  alert("Please enter a message");
  return false;
  }
  
  else
  {
  alert("You have submitted the following information: " + "name:  " + x + ", " + "email:  " + y + " and " + "message:  " + z + ".");
  return true;
  }
}

 





  