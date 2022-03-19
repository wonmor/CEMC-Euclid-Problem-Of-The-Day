import React from "react";
import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  var today = new Date(),

  date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
  let time = today.getHours() + ':' + today.getMinutes() + ':' + today.getSeconds();
  // This following section will display the table with the records of individuals.
  return (
    <div>
      <div id="container-1">
        <h1>Welcome to CEMC Euclid Problem of the Day!</h1>
        <h3>
          This is a platform developed to help students with different materials
          for University of Waterloo's own math competiton for high school
          students. Please note that this website does not represent Waterloo's
          CEMC nor is it hosted by the university itself!
        </h3>
      </div>
      <ul id="horizontal-list" className="list-group list-group-horizontal-xl">
        <li>
          <div className="container-default">
            <h1>Hey, how are you feeling?</h1>
            <h3>Right now, it is {time},<br></br>and today's date is<br></br>{date}.</h3>
            <br></br>
          </div>
        </li>
        <li>
          <div className="container-default" id="container-3">
            <h1>Contribute to Our Project</h1>
            <h3>To access our database, click the button down below.</h3>
            <br></br>
            <button
              className="btn btn-outline-light"
              onClick={() => navigate("/admin")}
            >
              MongoDB Redirect
            </button>
          </div>
        </li>
      </ul>
    </div>
  );
}
