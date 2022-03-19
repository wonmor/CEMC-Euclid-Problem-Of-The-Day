import React from "react";

export default function SourceCode() {
  return (
    <div>
      <h1>Server.JS</h1>
      <h3>Developed using the MERN stack</h3>
      <a href="https://github.com/wonmor/CEMC-Euclid-Problem-Of-The-Day">
        <button id="github-btn" className="btn btn-outline-light">
          Check out our GitHub page!
        </button>
      </a>
      <iframe
        title="WebView"
        id="webview"
        src="https://emgithub.com/embed.js?target=https%3A%2F%2Fgithub.com%2Fwonmor%2FCEMC-Euclid-Problem-Of-The-Day%2Fblob%2Fmaster%2Fserver.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"
        width="100%"
        height="800"
      >
        <p>Your browser does not support iframes.</p>
      </iframe>
    </div>
  );
}
