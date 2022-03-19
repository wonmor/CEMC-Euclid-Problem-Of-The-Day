const express = require("express");
const { createProxyMiddleware } = require('http-proxy-middleware');
const app = express();
const cors = require("cors");
require("dotenv").config({ path: "./config.env" });
const port = process.env.PORT || 5000;
app.use(cors());
app.use(express.json());
app.use(require("./routes/record"));
app.use(
    '/record', // you miss this part in your server code
    createProxyMiddleware({ target: 'https://cemc-euclid-problem-of-the-day.herokuapp.com', changeOrigin: true })
);
app.listen(3000);
// get driver connection
const dbo = require("./db/conn");

app.listen(port, () => {
    // perform a database connection when server starts
    dbo.connectToServer(function(err) {
        if (err) console.error(err);

    });
    console.log(`Server is running on port: ${port}`);
});

// TEMPLATE USED: https://github.com/mongodb-developer/mern-stack-example
// Type 'npm start' in both the client AND server folders...

// TO DO: IMPLEMENT OOP FOR EVERYTHING

// HOW TO SET ID AND PW SECURELY ON HEROKU CLI: https://devcenter.heroku.com/articles/config-vars

// HOW TO DEPLOY MERN STACK ON HEROKU: https://dev.to/hawacodes/deploying-a-mern-app-with-heroku-3km7

// HOW TO FIX 'NOT SECURE' JAVASCRIPT CONSOLE ERROR: https://stackoverflow.com/questions/59023482/mern-stack-failed-to-load-resource-neterr-connection-refused

// CORS: a terminology that refers to a situation where you call the server side from the client side

// Accessing the path module
const path = require("path");

// Step 1:
app.use(express.static(path.resolve(__dirname, "./client/build")));
// Step 2:
app.get("*", function(request, response) {
    response.sendFile(path.resolve(__dirname, "./client/build", "index.html"));
});

/*
FOR DEVELOPMENT, ADD THESE LINES TO SCRIPTS CATEGROY IN THE CLIENT SIDE PACKAGE.JSON:
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
*/

// npm -g install bla bla => global installation
// Run the program by npm start