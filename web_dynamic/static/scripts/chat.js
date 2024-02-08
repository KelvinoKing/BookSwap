var receiver_id = null;
var sender_id = null;

$(document).ready(function () {
    // Connect to the Socket.IO server
    var socket = io.connect('http://' + document.domain + ':5000');

   // Event listener for receiving chat messages
   socket.on('my response', function (msg) {
        var receiverUsername = msg.receiver || 'Unknown User'; // Use a default username if not provided

        // Append the message to the chat area only if the receiver is currently selected
        if ($('#chat h2').text().endsWith(receiverUsername)) {
            $('#chat-messages').append('<p><strong>' + msg.sender + ':</strong> ' + msg.message + '</p>');

        } else {
            // If the receiver is not selected, show a notification dot next to the receiver in the user list
            var receiverListItem = $('#user-list-container li:contains("' + msg.sender + '")');
            receiverListItem.find('.notification-dot').show();

            // Move the sender to the top of the list
            receiverListItem.prependTo('#user-list-container');
        }
    });

    // Event listener for submitting the chat form
    $('#chat-form').submit(function (event) {
        var selectedReceiver = $('#chat h2').text().replace('Chat with ', ''); // Get the selected user
        var sender = $(this).data('user-name');
        event.preventDefault();

        // Get the message from the input field
        var message = $('#message-input').val();

        // Emit the 'my event' to the server along with the selected user's username
        socket.emit('my event',
        { 'message': message,
        'sender': sender,
        'sender_id': sender_id,
        'receiver': selectedReceiver,
        'receiver_id': receiver_id});

        // Clear the input field
        $('#message-input').val('');

        new_chat = {'message': message,
        'sender': sender,
        'sender_id': sender_id,
        'receiver': selectedReceiver,
        'receiver_id': receiver_id}
        // Make an API call to save the chat message to the database
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5001/api/v1/users/" + sender_id + "/chats",
            contentType: "application/json",
            data: JSON.stringify(new_chat),
            xhrFields: {
                withCredentials: true  // Include credentials
            },
            success: function (response) {
                console.log("Chat message saved successfully");
            },
            error: function (xhr, status, error) {
                var errorMessage = "Error saving chat message";

                if (xhr.responseJSON && xhr.responseJSON.message) {
                    errorMessage += ": " + xhr.responseJSON.message;
                } else {
                    errorMessage += ": " + status + " - " + error;
                }

                alert(errorMessage);
            }
        });
    });

    
    $(".requestBtn").click(function () {
       
        window.location.href = '/dashboard';
    });

    
    // Event listener for user clicks on the user list items
    $('#user-list-container').on('click', 'a', function (event) {
        event.preventDefault();
        var selectedReceiver = $(this).text();
        receiver_id = $(this).data('receiver-id');
        sender_id = $(this).data('sender-id');
        startChat(selectedReceiver);

        // Hide the notification dot when the user is selected
        $(this).find('.notification-dot').hide();

        startFetchingChats();
    });

    // Hide the chat elements when the page loads
    hideChatElements();

    // Event listener for the cancel button
    $('#cancel-button').click(function () {
        cancelChat();
    });
});


// Function for searching users dynamically
function searchUsers() {
    var searchInput = document.getElementById('search-input');
    var userListContainer = document.getElementById('user-list-container');
    var filter = searchInput.value.toUpperCase();
    var listItems = userListContainer.getElementsByTagName('li');

    for (var i = 0; i < listItems.length; i++) {
        var userName = listItems[i].getElementsByTagName('a')[0].innerHTML.toUpperCase();
        if (userName.indexOf(filter) > -1) {
            listItems[i].style.display = '';
        } else {
            listItems[i].style.display = 'none';
        }
    }
}


// Function to start a chat with a selected user
// Function to hide the chat-related elements
function hideChatElements() {
    $('#chat-form').hide();
    $('#chat-messages').hide();
    $('#message-input').hide();
    $('#send-button').hide();
    $('#cancel-button').hide();
}

// Function to show the chat-related elements
function showChatElements() {
    $('#chat-messages').show();
    $('#chat-form').show();
    $('#message-input').show();
    $('#send-button').show();
    $('#cancel-button').show();
}

// ... (Other code remains unchanged)

// Function to start a chat with a selected user
function startChat(selectedReceiver) {
    // Set up the chat interface for the selected user
    $('#chat-messages').empty(); // Clear previous chat messages
    $('#chat').show(); // Show the chat section if hidden
    $('#user-search').hide(); // Hide the user search section
    $('#user-list').hide(); // Hide the user list section

    // Show the chat-related elements
    showChatElements();

    // Update the chat heading
    $('#chat h2').text('Chat with ' + selectedReceiver);

    // Fetch chat messages for the selected user from the API
    getchats();
}


// Function to call the chats api
function getchats(){
    // Fetch chat messages for the selected user from the API
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5001/api/v1/chats",
        success: function (response) {

            // Append the fetched messages to the chat area
            $('#chat-messages').empty(); // Clear previous messages

        for (var i = 0; i < response.length; i++) {
            var message = response[i];
            var messageHTML = '<p><strong>' + message.sender + ':</strong> ' + message.message + '</p>';

            // Check if the message is from the selected receiver
            if (message.receiver_id === sender_id && message.sender_id === receiver_id) {
                // Display receiver's message
                messageHTML = '<p><strong>' + message.sender + ':</strong> ' + message.message + '</p>';
                $('#chat-messages').append(messageHTML);
            } else if (message.sender_id === sender_id && message.receiver_id === receiver_id) {
                // Display sender's message
                messageHTML = '<p><strong>' + message.sender + ':</strong> ' + message.message + '</p>';
                $('#chat-messages').append(messageHTML);
            }
        }

            // After appending messages
            var chatContainer = $('#chat-messages');
            chatContainer.scrollTop(chatContainer[0].scrollHeight);
        },
        error: function (xhr, status, error) {
            console.error("Error fetching chat messages:", status, error);
        }
    });
}


// Function to cancel the current chat and go back to the user list
function cancelChat() {
    $('#chat-messages').empty(); // Clear previous chat messages
    $('#user-search').show(); // Show the user search section
    $('#user-list').show(); // Show the user list section
    stopFetchingChats();

    // Hide the chat-related elements
    hideChatElements();
}

// Function to stop fetching chats periodically
function stopFetchingChats() {
    // Clear the interval when needed, for example, when the user navigates away
    var fetchInterval = $(document).data('fetchInterval');
    if (fetchInterval) {
        clearInterval(fetchInterval);
    }
}

// Function to start fetching chats periodically
function startFetchingChats() {
    // Call getchats() initially
    getchats();

    // Set up a setInterval to call getchats() every, for example, 5 seconds
    var fetchInterval = setInterval(getchats, 5000);

    // Store the interval ID to be able to clear it later
    $(document).data('fetchInterval', fetchInterval);
}