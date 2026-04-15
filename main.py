from analyser import generate_alerts, read_log_file, count_logs, extract_error_details,get_error_patterns



def main():
    log_file = "app.log"
    logs = read_log_file(log_file)
    
    results = count_logs(logs)

    print("Log Analysis Results:")
    print(f"Errors: {results['error']}")
    print(f"Warnings: {results['warning']}")
    print(f"Info: {results['info']}")

    error_log_details = extract_error_details(logs)

    if results['error'] > 0:
        print("\nError Logs:")
        for err in error_log_details:
            print(err)

    error_patterns = get_error_patterns(error_log_details)

    print("\nError Patterns :")
    for error, count in error_patterns.items():
        print(f"{error} -> {count} times")

    alerts = generate_alerts(results, error_patterns)

    print("\nAlerts:")

    for alert in alerts:
      print(f"[{alert['level']}] {alert['message']}")

 
if __name__ == "__main__":
    main()
