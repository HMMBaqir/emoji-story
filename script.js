// script.js
document.getElementById('send-btn').addEventListener('click', sendMessage);

document.getElementById('chat-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const chatInput = document.getElementById('chat-input');
    const message = chatInput.value;

    // post to localhost:8000/stories

    const generateResponse = (message) => {
    const API_URL = "http://localhost:8000/stories";
    const requestOptions = {
        method: "POST",
  
        body: JSON.stringify({
            "emojiSequence": "message",
            "authorNickname": "User",
            "likes": 0
        }),
    };
    fetch(API_URL, requestOptions)
        .then(response => response.json())
        .then(data => {
            console.log("Response:", data);
        })
        .catch(error => {
            console.error("Error:", error);
        }); 
    };
    if (message.trim() !== "") {
        const chatBox = document.getElementById('chat-box');
        
        // Create a new message element
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', 'user-message');
        messageElement.textContent = message;

        // Append the message to the chat box
        chatBox.appendChild(messageElement);
        
        // Scroll to the bottom
        chatBox.scrollTop = chatBox.scrollHeight;

        // Clear the input field
        chatInput.value = '';
    }
}