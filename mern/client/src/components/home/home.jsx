import React from "react";
import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();
  // This following section will display the table with the records of individuals.
  return (
    <div>
      <h1>Welcome to CEMC Euclid Problem of the Day!</h1>
      <h3>To access our database, click the button down below.</h3>
      <br></br>
      <button onClick={() => navigate('/admin') }>MongoDB Redirect</button>
    </div>
  );
}
