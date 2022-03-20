// Client side app generated by create-react-app
import React from "react";

// We use Route in order to define the different routes of our application
import { Route, Routes } from "react-router-dom";

// We import all the components we need in our app
import Navbar from "./components/navbar";
import Footer from "./components/footer"
import RecordList from "./components/admin/recordList";
import Edit from "./components/admin/edit";
import Create from "./components/admin/create";

import SourceCode from "./components/home/sourceCode"
import Home from "./components/home/home";

const App = () => {
  return (
    <div>
      <Navbar />
      <div style={{ margin: 20, 'min-height': '100vh'}}>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/source-code" element={<SourceCode />} />
        <Route exact path="/admin" element={<RecordList />} />
        <Route path="/admin/edit/:id" element={<Edit />} />
        <Route path="/admin/create" element={<Create />} />
      </Routes>
      </div>
      <Footer />
    </div>
  );
};

export default App;

// Run npm run build to apply all the changes made on the client-end...