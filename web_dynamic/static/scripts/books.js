$(document).ready(function () {

    $(".update-btn").click(function () {
        // Retrieve book details from the clicked book item
        var bookItem = $(this).closest('.book-item');
        var title = bookItem.find('h3').text();
        var author = bookItem.find('.author').text();
        var bookId = bookItem.data('book-id');
        var genre = bookItem.find('.genre').text();
        var synopsis = bookItem.find('.synopsis').text();

        // Populate update form with current book details
        $("#update-book-title").val(title);
        $("#update-book-author").val(author);
        $("#update-book-genre").val(genre);
        $("#update-book-synopsis").val(synopsis);

        // Store book ID for later use
        $("#update-book").data('book-id', bookId);

        // Toggle visibility of update form and hide add book form
        $("#add-book").hide();
        $("#update-book").show();
    });

    // Add functionality to close update form
    $(".update-save-btn").click(function () {
        // Retrieve book ID from the update form data attribute
        var bookId = $("#update-book").data('book-id');
    
        // Retrieve the existing values
        var existingTitle = $("#update-book-title").val();
        var existingAuthor = $("#update-book-author").val();
        var existingGenre = $("#update-book-genre").val();
        var existingSynopsis = $("#update-book-synopsis").val();
        var existingImage = $("#update-book-image")[0].files[0]; // Get the selected file
    
        // Create FormData object to handle file uploads
        var formData = new FormData();
        formData.append('title', existingTitle);
        formData.append('author', existingAuthor);
        formData.append('genre', existingGenre);
        formData.append('synopsis', existingSynopsis);
        formData.append('image', existingImage);
    
        // Make API call to update book information with FormData
        $.ajax({
            type: "PUT",
            url: "http://127.0.0.1:5001/api/v1/books/" + bookId,
            contentType: false, // Set content type to false for FormData
            processData: false, // Disable processing of data for FormData
            data: formData,
            xhrFields: {
                withCredentials: true  // Include credentials
            },
            success: function (response) {
                alert("Book updated successfully");
                window.location.href = "/dashboard";
            },
            error: function (xhr, status, error) {
                var errorMessage = "Error updating book";
    
                if (xhr.responseJSON && xhr.responseJSON.message) {
                    errorMessage += ": " + xhr.responseJSON.message;
                } else {
                    errorMessage += ": " + status + " - " + error;
                }
    
                alert(errorMessage);
            }
        });
    
        $("#update-book").hide();
        $("#add-book").show();
    });

    // Delete button click event
    $(".delete-btn").click(function () {
        // Retrieve book details from the clicked book item
        var bookItem = $(this).closest('.book-item');
        var bookId = bookItem.data('book-id');

        // Confirm deletion with the user
        var confirmDelete = confirm("Are you sure you want to delete this book?");

        if (confirmDelete) {
            // Make API call to delete the book
            $.ajax({
                type: "DELETE",
                url: "http://127.0.0.1:5001/api/v1/books/" + bookId,
                xhrFields: {
                    withCredentials: true  // Include credentials
                },
                success: function (response) {
                    alert("Book deleted successfully");
                    // Optionally, you can remove the deleted book item from the UI
                    bookItem.remove();
                },
                error: function (xhr, status, error) {
                    var errorMessage = "Error deleting book";

                    if (xhr.responseJSON && xhr.responseJSON.message) {
                        errorMessage += ": " + xhr.responseJSON.message;
                    } else {
                        errorMessage += ": " + status + " - " + error;
                    }

                    alert(errorMessage);
                }
            });
        }
    });


    // Add functionality to add a new book
    $(".save-btn").click(function () {

        // Retrieve book ID from the update form data attribute
        var user_id = $("#add-book").data('user-id');
        
       // Retrieve new book details from the add book form
       var newTitle = $("#book-title").val();
       var newAuthor = $("#book-author").val();
       var newGenre = $("#book-genre").val();
       var newSynopsis = $("#book-synopsis").val();
       var newImage = $("#book-image")[0].files[0]; // Get the selected file

       // Create FormData object to handle file uploads
       var formData = new FormData();
       formData.append('title', newTitle);
       formData.append('author', newAuthor);
       formData.append('genre', newGenre);
       formData.append('synopsis', newSynopsis);
       formData.append('image', newImage);

       // Make API call to add a new book
       $.ajax({
           type: "POST",
           url: "http://127.0.0.1:5001/api/v1/users/" + user_id + "/books",
           contentType: false,
           processData: false,
           data: formData,
           xhrFields: {
               withCredentials: true  // Include credentials
           },
           success: function (response) {
               alert("New book added successfully");
               // Optionally, you can redirect or perform any other action after adding a new book
               window.location.href = "/dashboard";
           },
           error: function (xhr, status, error) {
               var errorMessage = "Error adding new book";

               if (xhr.responseJSON && xhr.responseJSON.message) {
                   errorMessage += ": " + xhr.responseJSON.message;
               } else {
                   errorMessage += ": " + status + " - " + error;
               }

               alert(errorMessage);
           }
       });
   });

        // Event handler for input changes in synopsis textarea Add Book
    $("#book-synopsis").on('input', function () {
        addSynopsisCount();
    }); 

    // Event handler for input changes in synopsis textarea Update Book
    $("#update-book-synopsis").on('input', function () {
        updateSynopsisCount();
    });

});


// Function to update the character count
function addSynopsisCount() {
    var maxChars = 125;
    var currentChars = $("#book-synopsis").val().length;
    // Update the content of the span element
    $("#book-synopsis-count").text(currentChars + '/' + maxChars);
    
    if (currentChars > maxChars) {
        // Trim the synopsis text to the allowed length
        $("#book-synopsis").val($("#book-synopsis").val().substring(0, maxChars));
        $("#book-synopsis-count").text(maxChars + '/' + maxChars);
    }
}

// Function to update the character count
function updateSynopsisCount() {
    var maxChars = 125;
    var currentChars = $("#update-book-synopsis").val().length;
    
    // Update the content of the span elemen
    $("#update-book-synopsis-count").text(currentChars + '/' + maxChars); // Corrected ID here
    
    if (currentChars > maxChars) {
        // Trim the synopsis text to the allowed length
        $("#update-book-synopsis").val($("#update-book-synopsis").val().substring(0, maxChars));
        $("#update-book-synopsis-count").text(maxChars + '/' + maxChars); // Corrected ID here
    }
}

