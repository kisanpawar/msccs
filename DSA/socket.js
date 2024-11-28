const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Serve static files (index.html, JS, CSS)
app.use(express.static('public'));

// WebSocket event handling
io.on('connection', (socket) => {
  console.log('a user connected');
  
  // Listen for a message from the client
  socket.on('send_message', (msg) => {
    io.emit('receive_message', msg);  // Broadcast message to all clients
  });

  // Handle disconnect
  socket.on('disconnect', () => {
    console.log('user disconnected');
  });
});

// Start the server
server.listen(3000, () => {
  console.log('Server listening on http://localhost:3000');
});
