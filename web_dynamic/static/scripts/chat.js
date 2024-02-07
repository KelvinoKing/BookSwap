$(document).ready(function () {
    // Connect to the Socket.IO server
    var socket = io.connect('http://' + document.domain + ':5000');

    // Event listener for receiving chat messages
    socket.on('my response', function (msg) {
        var receiverUsername = msg.receiver || 'Unknown User'; // Use a default username if not provided
        console.log(msg.sender + ': ' + msg.message); // Log the message to the console

        // Append the message to the chat area only if the receiver is currently selected
        if ($('#chat h2').text().endsWith(receiverUsername)) {
            $('#chat-messages').append('<p><strong>' + msg.sender + ':</strong> ' + msg.message + '</p>');
            messageReceived();
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
        var selectedUser = $('#chat h2').text().replace('Chat with ', ''); // Get the selected user
        var sender = $(this).data('user-name');
        event.preventDefault();

        // Get the message from the input field
        var message = $('#message-input').val();

        // Emit the 'my event' to the server along with the selected user's username
        socket.emit('my event', { 'message': message, 'receiver': selectedUser, 'sender': sender});

        // Clear the input field
        $('#message-input').val('');
    });

    
    $(".requestBtn").click(function () {
       
        window.location.href = '/dashboard';
    });



    // Event listener for user clicks on the user list items
    $('#user-list-container').on('click', 'a', function (event) {
        event.preventDefault();
        var selectedUser = $(this).text();
        startChat(selectedUser);

        // Hide the notification dot when the user is selected
        $(this).find('.notification-dot').hide();
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
function startChat(selectedUser) {
    // Set up the chat interface for the selected user
    $('#chat-messages').empty(); // Clear previous chat messages
    $('#chat').show(); // Show the chat section if hidden
    $('#user-search').hide(); // Hide the user search section
    $('#user-list').hide(); // Hide the user list section

    // Show the chat-related elements
    showChatElements();

    // Update the chat heading
    $('#chat h2').text('Chat with ' + selectedUser);
}

// Function to cancel the current chat and go back to the user list
function cancelChat() {
    $('#chat-messages').empty(); // Clear previous chat messages
    $('#user-search').show(); // Show the user search section
    $('#user-list').show(); // Show the user list section

    // Hide the chat-related elements
    hideChatElements();
}