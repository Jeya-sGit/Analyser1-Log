from collections import Counter
import google.genai as genai
from dotenv import load_dotenv
import os
import requests


load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

'''models = client.models.list()

for m in models:
    print(m.name)'''

'''genai.configure(api_key=os.getenv("GEMINI_API_KEY"))'''

'''def read_log_file(file_path):  
    try:
        with open(file_path, "r") as f:
         logs = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {
            'error': 0,
            'warning': 0,
            'info': 0
        }
    except OSError as e:
        print(f"Error reading file '{file_path}': {e}")
        return {
            'error': 0,
            'warning': 0,
            'info': 0
        }
    
    return logs'''

def fetch_logs_from_api():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    data = response.json()

    logs = []

    for item in data[:5]:
        logs.append({
            "_time": "2026-04-10T10:00:00",
            "log_level": "ERROR" if item["id"] % 2 == 0 else "INFO",
            "message": "DB connection failed" if item["id"] % 2 == 0 else item["title"],
            "service_name": "demo-service"
        })

    return logs

def count_logs(logs):   
   counts = {
        "error": 0,
        "warning": 0,
        "info": 0
    }
    
   for log in logs:
        if log["log_level"] == "ERROR":
            counts["error"] += 1
        elif log["log_level"] == "WARN":
            counts["warning"] += 1
        elif log["log_level"] == "INFO":
            counts["info"] += 1

   return counts

def extract_error_details(logs):
    errors = []

    for log in logs:
        if log["log_level"] == "ERROR":
            errors.append(log)

    return errors

def get_error_patterns(error_logs):
    messages = []

    for log in error_logs:
        messages.append(log["message"])

    print(messages)
    return Counter(messages)

def generate_alerts(results, error_patterns):
    alerts = []

   
    if results['error'] > 3:
        alerts.append({
            "level": "CRITICAL",
            "message": "High error rate detected"
        })

    
    for error, count in error_patterns.items():
        if count >= 2:
            alerts.append({
                "level": "HIGH",
                "message": f"Repeated error: '{error}' occurred {count} times"
            })


    if results['error'] == 1:
        alerts.append({
            "level": "WARNING",
            "message": "Single error detected"
        })

    if not alerts:
        alerts.append({
            "level": "INFO",
            "message": "No critical issues detected"
        })

    return alerts

def prepare_ai_summary(results, error_patterns):
    summary = f"""
Log Summary:
- Errors: {results['error']}
- Warnings: {results['warning']}
- Info: {results['info']}

Top Error Patterns:
"""

    for error, count in error_patterns.items():
        summary += f"- {error}: {count} times\n"

    return summary

def get_ai_analysis(summary):
    response = client.models.generate_content(
       model="gemini-2.5-flash",
        contents=f"""
You are an AIOps assistant.

Analyze the logs and provide:
1. Root cause
2. Impact
3. Suggested fixes

{summary}
"""
    )

    return response.text