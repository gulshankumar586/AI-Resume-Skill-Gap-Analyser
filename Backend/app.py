from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from resume_analyzer import analyze_resume

app = Flask(__name__)
# This allows your React app on port 3000 to send data to this Flask app
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# app = Flask(__name__)
# CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return jsonify({"message": "AI Resume Skill Gap Analyser API"}), 200

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["resume"]
    role = request.form["job_role"]

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    result = analyze_resume(file_path, role)
    
    if not isinstance(result, dict):
        result = {"found": [], "missing": [], "suggestions": []}

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
