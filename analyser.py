from collections import Counter


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
    response = {
        "results": [
            {
                "_time": "2026-04-10T10:01:05",
                "log_level": "ERROR",
                "message": "DB connection failed",
                "service_name": "auth-service"
            },
            {
                "_time": "2026-04-10T10:03:15",
                "log_level": "ERROR",
                "message": "Timeout while calling API",
                "service_name": "payment-service"
            },
            {
                "_time": "2026-04-10T10:05:25",
                "log_level": "ERROR",
                "message": "DB connection failed",
                "service_name": "auth-service"
            },
            {
                "_time": "2026-04-10T10:06:30",
                "log_level": "WARN",
                "message": "Disk space low",
                "service_name": "storage-service"
            }
        ]
    }

    return response["results"]

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

    if results['error'] >=3:
        alerts.append({
            "level": "CRITICAL",
            "message": "High Error Rate Detected"
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

    if results['error'] == 0:
        alerts.append({
            "level": "INFO",
            "message": "No errors detected"
        })

    return alerts