const express = require("express");
const app = express();
const cors = require("cors");
require("dotenv").config({ path: "./config.env" });
const port = process.env.PORT || 5000;
app.use(cors());
app.use(express.json());
app.use(require("./routes/record"));
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