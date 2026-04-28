import json
import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "").strip()
    doc_type = data.get("doc_type", "Document")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    prompt = f"""You are a Red Flag Detector. Analyze this {doc_type} and return ONLY valid JSON, no markdown, no backticks.
Document:
{text[:3000]}
Return this exact JSON structure:
{{"trust_score": <0-100>, "verdict": "<2-3 sentence summary>", "red_flags": [{{"title": "<flag>", "severity": "Critical|High|Medium", "explanation": "<why it's a red flag>"}}], "flag_count": <number>}}
Return ONLY the JSON object."""

    response = model.generate_content(prompt)
    raw = response.text.strip()
    clean = raw.replace("```json", "").replace("```", "").strip()
    result = json.loads(clean)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
