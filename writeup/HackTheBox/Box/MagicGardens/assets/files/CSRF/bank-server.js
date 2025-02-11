const http = require('http');

const server = http.createServer((req, res) => {
  console.log(`Received ${req.method} request from ${req.connection.remoteAddress}`);
  console.log('Request Headers:', req.headers); // Log request headers

  let requestBody = '';
  req.on('data', chunk => {
    requestBody += chunk.toString(); // Accumulate request body
  });

  req.on('end', () => {
    console.log('Received Request Body:', requestBody); // Log request body

    if (req.method === 'POST' && req.url === '/api/payments/') {
      try {
        // Parse the JSON data
        const requestData = JSON.parse(requestBody);
        const cardName = requestData.cardname;
        const cardNumber = requestData.cardnumber;

        // Construct the response JSON for a successful payment
        const jsonResponse = {
          status: '200',
          message: 'Payment received successfully',
          cardname: cardName,
          cardnumber: cardNumber
        };

        // Log the received JSON data and the JSON response
        console.log('Received JSON data:', requestData);
        console.log('Sending JSON response:', jsonResponse);

        // Log the response headers
        console.log('Sending Response Headers:');
        console.log('HTTP/1.1 200 OK'); // Log HTTP status line
        console.log('Server: nginx/1.22.1');
        console.log('Date:', new Date().toUTCString());
        console.log('Content-Type: application/json');
        console.log(`Content-Length: ${Buffer.byteLength(JSON.stringify(jsonResponse))}`);
        console.log('Connection: keep-alive');
        console.log('X-Frame-Options: DENY');
        console.log('X-Content-Type-Options: nosniff');
        console.log('Referrer-Policy: same-origin');
        console.log('Cross-Origin-Opener-Policy: same-origin');

        // Log the response body
        console.log('Sending Response Body:', jsonResponse);

        // Send the response with status code 200 and specified headers
        res.writeHead(200, {
          'Content-Type': 'application/json',
          'Server': 'nginx/1.22.1',
          'Date': new Date().toUTCString(),
          'Content-Length': Buffer.byteLength(JSON.stringify(jsonResponse)),
          'Connection': 'keep-alive',
          'X-Frame-Options': 'DENY',
          'X-Content-Type-Options': 'nosniff',
          'Referrer-Policy': 'same-origin',
          'Cross-Origin-Opener-Policy': 'same-origin'
        });

        // Send the response body
        res.end(JSON.stringify(jsonResponse)); // Stringify the JSON response before sending
      } catch (error) {
        console.error('Error parsing JSON:', error.message);
        res.statusCode = 500;
        res.end('Internal Server Error');
      }
    } else {
      res.statusCode = 404;
      res.end();
    }
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
