import React from "react";

// We import bootstrap to make our application look better.
import "bootstrap/dist/css/bootstrap.css";

import { NavLink, useLocation } from "react-router-dom";

// Here, we display our Navbar
export default function Navbar() {
  const location = useLocation();

  return (
    <div>
      <nav
        id="navbar-main"
        className="navbar navbar-expand-xl navbar-dark bg-dark hover-shadow"
      >
        <NavLink id="navbar-brand" className="navbar-brand" to="/">
          <img
            style={{ width: 70 + "%" }}
            alt="Logo"
            src="https://uwaterloo.ca/profiles/uw_base_profile/modules/features/uw_nav_global_header/images/university-of-waterloo-logo.png"
          ></img>
        </NavLink>
        <div id="navbarSupportedContent">
          <ul className="nav nav-pills" id="navbarItems">
            <li className="nav-item">
              {location.pathname.includes("/admin") &&
                (location.pathname.includes("/create") ||
                  location.pathname.includes("/edit") ||
                  location.pathname.includes("/record-list")) && (
                  <NavLink
                    id="create-record"
                    className="nav-link"
                    to="/admin/create"
                  >
                    Create Record
                  </NavLink>
                )}
            </li>
            <li className="nav-item">
              {!location.pathname.includes("/admin") && (
                <NavLink id="create-record" className="nav-link" to="/">
                  Home
                </NavLink>
              )}
            </li>
            <li className="nav-item">
              {!location.pathname.includes("/admin") && (
                <NavLink
                  id="create-record"
                  className="nav-link"
                  to="/source-code"
                >
                  Source Code
                </NavLink>
              )}
            </li>
          </ul>
        </div>
      </nav>
    </div>
  );
}
