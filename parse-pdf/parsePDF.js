// USING THE TUTORIAL: https://www.npmjs.com/package/pdfreader

// USE MULTER FOR FILE UPLOAD FUNCTIONALITY: https://arosh-segar.medium.com/how-to-upload-images-using-multer-in-the-mern-stack-1c6bf691947e

/*
ORDER OF OPERATIONS FOR PDF SLICING
1. READ THE LEFTMOST TEXT ELEMENTS ON THE PDF FILE AND CHECK IF THEY CONTAIN A NUMBER FOLLOWED BY A PERIOD. (DOT)
THEN, GET THE READING OF THE POSITION.
2. MOVE DOWN A LIL BIT FROM THE SAVED POSITION VALUES AND SLICE THE PDF AND SAVE THEM AS SEPERATE FILES.

AS A SIDE NOTE:
LET THE USER UPLOAD THEIR OWN PDF FILE. THE FILE UPLOAD SOLUTION WILL BE MULTER.
*/

var pdfreader = require("pdfreader");