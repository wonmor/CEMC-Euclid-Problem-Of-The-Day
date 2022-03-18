import React from "react";

// We import bootstrap to make our application look better.
import "bootstrap/dist/css/bootstrap.css";

// We import NavLink to utilize the react router.
import { NavLink } from "react-router-dom";

import { useLocation } from "react-router-dom";

import { Helmet } from "react-helmet";

const TITLE = "CEMC Euclid: POTD";

// Here, we display our Navbar
export default function Navbar() {
  const location = useLocation();

  return (
    <div>
      <Helmet>
        <title>{TITLE}</title>
      </Helmet>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <NavLink className="navbar-brand" to="/">
          <img
            style={{ width: 70 + "%" }}
            alt="Logo"
            src="https://uwaterloo.ca/profiles/uw_base_profile/modules/features/uw_nav_global_header/images/university-of-waterloo-logo.png"
          ></img>
        </NavLink>
        <button
          className="navbar-toggler"
          style={{ display: "none" }}
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              {location.pathname.includes("/admin") && (
                <NavLink className="nav-link" to="/admin/create">
                  Create Record
                </NavLink>
              )}
            </li>
          </ul>
        </div>
      </nav>
    </div>
  );
}
