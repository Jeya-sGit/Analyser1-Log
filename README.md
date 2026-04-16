# AI-Powered Log Analyzer (AIOps Project)

## 🚀 Overview
This project analyzes logs, detects error patterns, and uses AI to provide root cause analysis and suggestions.

## 🔥 Features
- Log parsing and analysis
- Error pattern detection
- Alert generation (INFO, WARNING, HIGH, CRITICAL)
- AI-based root cause analysis using Gemini API

## 🛠 Tech Stack
- Python
- Requests
- Google Gemini API
- dotenv

### 🔌 Log Source (API Integration)

For this project, a public API was used to simulate real-world log ingestion:

- API Used: https://jsonplaceholder.typicode.com/posts

This API provides sample JSON data which was treated as log input.

### 🔄 Data Transformation

Since the API does not provide logs in a standard log format, the response was transformed into a structured log format.

#### Original API Response Example:
{
  "userId": 1,
  "id": 2,
  "title": "qui est esse",
  "body": "..."
}

#### Transformed Log Format:
{
  "_time": "2026-04-10T10:00:00",
  "log_level": "ERROR",
  "message": "DB connection failed",
  "service_name": "demo-service"
}

### ⚙️ Transformation Logic

- `title` → used as log message
- `id` → used to simulate log severity:
  - even → ERROR
  - odd → INFO
- Static timestamp used for simulation
- Service name assigned as "demo-service"

### 🎯 Purpose

This transformation simulates how real systems (like Splunk or CloudWatch) ingest logs from different formats and normalize them for analysis.

## 📊 Workflow
Logs → Analyzer → Pattern Detection → Alerts → AI Analysis

## ▶️ How to Run

1. Clone repo
2. Create virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Add `.env` file:
   GEMINI_API_KEY=your_key
5. Run:
   python main.py

## 📌 Sample Output
- Error detection
- Pattern identification
- AI-generated root cause

## 💡 Future Enhancements
- FastAPI integration
- Dashboard (Grafana)
- Real Splunk integration