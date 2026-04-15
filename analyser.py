from collections import Counter


def read_log_file(file_path):  
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
    
    return logs

def count_logs(logs):   
    error_count = 0
    warning_count = 0
    info_count = 0
    
    for log in logs:
        if 'ERROR' in log:
            error_count += 1
        elif 'WARN' in log:
            warning_count += 1
        elif 'INFO' in log:
            info_count += 1
    
    return {
        'error': error_count,
        'warning': warning_count,
        'info': info_count
    }

def extract_error_details(logs):
    error_details = []
    
    for log in logs:
        if 'ERROR' in log:
            error_details.append(log.strip())
    
    return error_details

def get_error_patterns(error_logs):
    cleaned_errors = []

    for log in error_logs:
        parts = log.split("ERROR")
        if len(parts) > 1:
            error_message = parts[1].strip()
            cleaned_errors.append(error_message)

    print(Counter(cleaned_errors)) 
    return Counter(cleaned_errors)

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

    if results['error'] == 0:
        alerts.append({
            "level": "INFO",
            "message": "No errors detected"
        })

    return alerts