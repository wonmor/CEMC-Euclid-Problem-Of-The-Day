import React from 'react';
import { useNavigate } from "react-router-dom";

// import jokes from './humour.json'

// WHY 'NPM RUN BUILD?'
// LINK: https://stackoverflow.com/questions/43664200/what-is-the-difference-between-npm-install-and-npm-run-build

// function GenerateJoke () {
//   const parsed_jokes = JSON.parse(jokes);
// }

export default function Home() {
  const navigate = useNavigate();
  const dateTimeRef = React.useRef(null);
  // eslint-disable-next-line no-mixed-operators

  React.useEffect(() => {
    const secondsTimer = setInterval(() => {
      if (dateTimeRef.current) {
        dateTimeRef.current.innerText = new Date().toLocaleString();
      }
    }, 1000);
    return () => clearInterval(secondsTimer);
  }, [dateTimeRef]);

  // This following section will display the table with the records of individuals.
  return (
    <div>
      <div id="container-1">
        <h1>Welcome to CEMC Euclid: Problem of the Day!</h1>
        <h3>
          This is a platform developed to help students with different materials
          for University of Waterloo's own math competition for high school
          students. Please note that this website does not represent Waterloo's
          CEMC nor is it hosted by the university itself!
        </h3>
      </div>
      <ul id="horizontal-list" className="list-group list-group-horizontal-xl">
        <li>
          <div className="container-default">
            <h1>Hey, how are you feeling?</h1>
            <h3>Just in case you're wondering, it is <span ref={dateTimeRef}>[Retrieving...]</span> in your timezone. Hope you are enjoying your day!</h3>
            <br></br>
            <button
              className="btn btn-outline-light"
            >
              I'm Feeling Lucky
            </button>
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
