import React from "react";
import ResumeUpload from "./components/Temp.jsx"; 
import "./app.css";

function App() {
  return (
    <div className="container">
      <div className="card">
        <h1>AI Resume Analyzer</h1>
        <p>
          Upload your resume and discover skill gaps, career suggestions, and
          improvements using AI.
        </p>

        {/* 2. FIXED: Changed <ResumeUploads /> to <ResumeUpload /> */}
        <ResumeUpload /> 
      </div>
    </div>

  );
}

export default App;







