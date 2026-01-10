
import axios from "axios";
import { useState } from "react";

function ResumeUpload() {
  const [file, setFile] = useState(null);
  const [role, setRole] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("resume", file);
    formData.append("job_role", role);

    try {
      const res = await axios.post(
        "http://127.0.0.1:5000/analyze",
        formData
      );
      setResult(res.data);
      console.log("Backend Result:", res.data); // ✅ Debug-safe
    } catch (error) {
      console.error("Network Error:", error);
      alert(
        "Cannot connect to Backend! Ensure your Flask server is running on port 5000."
      );
    }
  };

  return (
    <>
      {/* Resume Upload */}
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      {/* Job Role Selection */}
      <select onChange={(e) => setRole(e.target.value)}>
        <option value="">Select Job Role</option>
        <option value="data analyst">Data Analyst</option>
        <option value="DevOps Engineer">DevOps Engineer</option>
        <option value="frontend developer">Frontend Developer</option>
        <option value="backend developer">Backend Developer</option>
        <option value="full stack developer">Full Stack Developer</option>
      </select>

      {/* Submit Button */}
      <button disabled={!file || !role} onClick={handleSubmit}>
        Analyze Resume
      </button>

      {/* Result Section */}
      {result && (
        <div className="result">
          {/* 1. Match Score */}
          <h3>Match Score: {result.score}%</h3>

          {/* 2. Skills Found */}
          <h3>Skills Found</h3>
          <div className="tags">
            {Array.isArray(result.matched) &&
              result.matched.map((skill, i) => (
                <span key={i} className="tag matched">
                  {skill}
                </span>
              ))}
          </div>

          {/* 3. Missing Skills */}
          <h3>Missing Skills</h3>
          <div className="tags">
            {Array.isArray(result.missing) &&
              result.missing.map((skill, i) => (
                <span key={i} className="tag missing">
                  {skill}
                </span>
              ))}
          </div>

          {/* 4. All Extracted Skills */}
         <h3>All Extracted Skills</h3>
         <ul>
          {Array.isArray(result.all_skills) &&
          result.all_skills.map((skill, i) => (
          <li key={i}>{skill}</li>
         ))}
        </ul>
        </div>
      )}
    </>
  );
}

export default ResumeUpload;
