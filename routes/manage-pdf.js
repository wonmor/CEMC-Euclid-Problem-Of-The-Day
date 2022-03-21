const express = require("express");

// recordRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /manage-pdf
const recordRoutes = express.Router();

// USING THE TUTORIAL: https://www.npmjs.com/package/pdfreader

// USE MULTER FOR FILE UPLOAD FUNCTIONALITY: https://arosh-segar.medium.com/how-to-upload-images-using-multer-in-the-mern-stack-1c6bf691947e

// ALSO USING SCISSORS MODULE: https://www.npmjs.com/package/scissors

/*
ORDER OF OPERATIONS FOR PDF SLICING
1. READ THE LEFTMOST TEXT ELEMENTS ON THE PDF FILE AND CHECK IF THEY CONTAIN A NUMBER FOLLOWED BY A PERIOD. (DOT)
THEN, GET THE READING OF THE POSITION.
2. MOVE DOWN A LIL BIT FROM THE SAVED POSITION VALUES AND SLICE THE PDF AND SAVE THEM AS SEPERATE FILES.
3. REPEAT THE SAME PROCESS FOR THE ANSWER FILE
4. MATCH THE QUESTIONS WITH THE CORRESPONDING ANSWERS BY THEIR INDECES

AS A SIDE NOTE:
LET THE USER UPLOAD THEIR OWN PDF FILE. THE FILE UPLOAD SOLUTION WILL BE MULTER.
*/

var pdfreader = require("pdfreader");

var scissors = require('scissors');

var question_sheet = scissors('../parsepdf/EuclidCombinedContest.pdf');

var answer_sheet = scissors('../parsepdf/EuclidCombinedSolutions.pdf');

recordRoutes.route("/manage-pdf").get(function(req, res) {
    

});