import React from "react";
import { useNavigate } from "react-router-dom";
import CanvasFreeDrawing from "canvas-free-drawing";

// import jokes from './humour.json'

// WHY 'NPM RUN BUILD?'
// LINK: https://stackoverflow.com/questions/43664200/what-is-the-difference-between-npm-install-and-npm-run-build

// function GenerateJoke () {
//   const parsed_jokes = JSON.parse(jokes);
// }

// Use the module https://www.npmjs.com/package/react-pdf to display the PDF on React

export default function Home() {
  const navigate = useNavigate();
  const dateTimeRef = React.useRef(null);
  const [showResults, setShowResults] = React.useState(false);

  React.useLayoutEffect(() => {
    // initialize
    const cfd = new CanvasFreeDrawing({
      elementId: "cfd",
      width: 500,
      height: 500,
    });

    // set properties
    cfd.setLineWidth(2.5); // in px
    cfd.setStrokeColor([0, 0, 0]); // in RGB

    // listen to events
    cfd.on({ event: "redraw" }, () => {
      // code...
    });

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
      <div className="container-1">
        <h1>
          <b>Welcome to CEMC Euclid: Problem of the Day!</b>
        </h1>
        <h3>
          This is a platform developed to help students with different materials
          for University of Waterloo's own math competition for high school
          students. Please note that this website does not represent Waterloo's
          CEMC nor is it hosted by the university itself!
        </h3>
        <a href="#practice-question">
          <button id="scroll-down" className="btn btn-outline-light">
            Today's Practice Question
          </button>
        </a>
      </div>
      <ul id="horizontal-list" className="list-group list-group-horizontal-xl">
        <li>
          <div className="container-default">
            <h1>Hey, how are you feeling?</h1>
            <h3>
              Just in case you're wondering, it is{" "}
              <span ref={dateTimeRef}>
                <i>[Retrieving...]</i>
              </span>{" "}
              in your timezone. Hope you are enjoying your day!
            </h3>
            <br></br>
            <a href="https://www.youtube.com/watch?v=ZExFN4NchiU">
              <button className="btn btn-outline-light">
                I'm Feeling Lucky
              </button>
            </a>
          </div>
        </li>
        <li>
          <div className="container-default" id="container-2">
            <h1>Contribute to Our Project</h1>
            <h3>Add more questions and improve the quality of our website!</h3>
            <br></br>
            <button
              className="btn btn-outline-light"
              onClick={() => navigate("/admin")}
            >
              Access the Admin Website
            </button>
          </div>
        </li>
      </ul>
      <div className="container-1" id="practice-question">
        <h1>
          <b>Problem of the Day</b>
        </h1>
        <h3>
          Development is currently in the <b>work in progress</b> stage.
        </h3>
        <br></br>
        <div className="grid-container" id="question-drawing-container">
          <div className="grid-item">
            <img src="https://i.stack.imgur.com/TjbDN.png" alt="question"></img>
          </div>
          <div className="grid-item">
            <h3>
              <i>
                As Teachers Around the World Like to Say:<br></br>
                <b>Please Show All Your Work!</b>
              </i>
            </h3>
          </div>
          <div className="grid-item">
            <canvas id="cfd"></canvas>
          </div>
          <div className="grid-item">
            <span>
              Thank you{" "}
              <a href="https://github.com/federico-moretti/canvas-free-drawing">
                canvas-free-drawing
              </a>{" "}
              for providing the <b>drawing board API</b>!
            </span>
          </div>
          <div className="grid-item">
            <a href="https://math.stackexchange.com/questions/2632636/geometric-proof-in-waterloo-euclid-contest">
              <button
                className="btn btn-outline-light"
                // onClick={() => setShowResults(true)}
              >
                Check the Answers
              </button>
            </a>
          </div>
          <div className="grid=item">{showResults ? <Results /> : null}</div>
        </div>
      </div>
    </div>
  );
}

const Results = () => <div id="results"></div>;
