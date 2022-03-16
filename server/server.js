const express = require("express");
const app = express();
const cors = require("cors");
require("dotenv").config({ path: "./config.env" });
const port = process.env.PORT || 5000; // Remember, port 5000 is in use in macOS environment by AirPlay
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

// Tutorial used to set up the MERN stack: https://www.mongodb.com/languages/mern-stack-tutorial
// How to deploy a new MongoDB cluster: https://docs.atlas.mongodb.com/tutorial/deploy-free-tier-cluster/
// How to set up SocketIO on MERN stack: https://www.valentinog.com/blog/socket-react/
// Schema = like blueprint