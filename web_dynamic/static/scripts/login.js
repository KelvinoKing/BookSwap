// static/script/login.js

$(document).ready(function() {
  // Sign Up Button Click Event
  $(".sign-up-htm .button").click(function() {
    // Retrieve form data
    var firstName = $(".sign-up-htm #user-first-name").val();
    var lastName = $(".sign-up-htm #user-last-name").val();
    var username = $(".sign-up-htm #user-user-name").val();
    var password = $(".sign-up-htm #pass-password").val();
    var repeatPassword = $(".sign-up-htm #pass-repassword").val();
    var email = $(".sign-up-htm #pass-email").val();
    var location = $(".sign-up-htm #user-location").val();

    // Check if passwords match
    if (password !== repeatPassword) {
      alert("Passwords do not match");
      return;
    }

    // Create user object
    var userData = {
      "first_name": firstName,
      "last_name": lastName,
      "user_name": username,
      "password": password,
      "email": email,
      "location": location
    };

    // Make API call to post user information
    $.ajax({
      type: "POST",
      url: "/signup",
      contentType: "application/json",
      data: JSON.stringify(userData),
      xhrFields: {
        withCredentials: true  // Include credentials
    },
      success: function(response) {
        alert("User created successfully");
      },
      error: function(xhr, status, error) {
        var errorMessage = "Error creating user";
      
        if (xhr.responseJSON && xhr.responseJSON.message) {
          errorMessage += ": " + xhr.responseJSON.message;
        } else {
          errorMessage += ": " + status + " - " + error;
        }
      
        alert(errorMessage);
      }
    });
  });

  // Sign In Button Click Event
  $(".sign-in-htm .button").click(function() {
    // Retrieve form data
    var username = $(".sign-in-htm #user").val();
    var password = $(".sign-in-htm #pass").val();

    // Create login object
    var loginData = {
      "user_name": username,
      "password": password
    };

    // Make API call for authentication (You need to implement this endpoint in your API)
    $.ajax({
      type: "POST",
      url: "/signin", // Adjust the URL based on your API endpoint for authentication
      contentType: "application/json",
      data: JSON.stringify(loginData),
      xhrFields: {
        withCredentials: true  // Include credentials
    },
      success: function(response) {
        alert("Login successful");
        // You can redirect or perform additional actions after successful login
         // Redirect to the dashboard
      },
      error: function(xhr, status, error) {
        var errorMessage = "Error loging in";
      
        if (xhr.responseJSON && xhr.responseJSON.message) {
          errorMessage += ": " + xhr.responseJSON.message;
        } else {
          errorMessage += ": " + status + " - " + error;
        }
      
        alert(errorMessage);
      }
    });
  });
});

  