$(document).ready(function () {
    // Connect to the Socket.IO server
    var socket = io.connect('http://' + document.domain + ':5000');

    // Event listener for receiving chat messages
    socket.on('my response', function (msg) {
        var username = msg.username || 'Unknown User'; // Use a default username if not provided
        console.log(username + ': ' + msg.message); // Log the message to the consoles
        $('#chat-messages').append('<p><strong>' + username + ':</strong> ' + msg.message + '</p>');
        messageReceived(); // Call the acknowledgment function here
    });

    // Event listener for submitting the chat form
    $('#chat-form').submit(function (event) {

        var userName = $(this).data('user-name');
        console.log(userName);
        event.preventDefault();

        // Get the message from the input field
        var message = $('#message-input').val();

        // Emit the 'my event' to the server along with the current username
        socket.emit('my event', { 'message': message, 'username': userName }); // Replace 'YourUsername' with the actual username

        // Clear the input field
        $('#message-input').val('');
    });

    // Callback function for acknowledging message received
    function messageReceived() {
        console.log('Message Sent');
    }

    $(".requestBtn").click(function () {
       
        window.location.href = '/dashboard';
    });
});
