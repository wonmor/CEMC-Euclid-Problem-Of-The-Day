import React from "react";
import { useNavigate } from "react-router-dom";

// import jokes from './humour.json'

// WHY 'NPM RUN BUILD?'
// LINK: https://stackoverflow.com/questions/43664200/what-is-the-difference-between-npm-install-and-npm-run-build

// function GenerateJoke () {
//   const parsed_jokes = JSON.parse(jokes);
// }

export default function AdminHome() {
  const navigate = useNavigate();

  // This following section will display the table with the records of individuals.
  return (
    <div>
      <div id="container-1">
        <h1><b>This is admin home.</b></h1>
        <h3>Press the button below to access the database.</h3>
        <br></br>
        <button
          className="btn btn-outline-light"
          onClick={() => navigate("/admin/record-list")}
        >
          MongoDB Redirect
        </button>
      </div>
    </div>
  );
}
