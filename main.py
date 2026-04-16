from analyser import generate_alerts, count_logs, extract_error_details,get_error_patterns,fetch_logs_from_api, prepare_ai_summary,get_ai_analysis

def main():
    '''log_file = "app.log"
    logs = read_log_file(log_file)'''

    logs = fetch_logs_from_api()
    
    results = count_logs(logs)

    print("\n========== LOG ANALYSIS ==========")
    print(f"Errors: {results['error']}")
    print(f"Warnings: {results['warning']}")
    print(f"Info: {results['info']}")

    error_log_details = extract_error_details(logs)

    if results['error'] > 0:
        print("\nError Logs:")
        for err in error_log_details:
         print(f"{err['_time']} | {err['service_name']} | {err['message']}")

    error_patterns = get_error_patterns(error_log_details)

    print("\nError Patterns :")
    for error, count in error_patterns.items():
        print(f"{error} -> {count} times")

    alerts = generate_alerts(results, error_patterns)

    print("\n========== ALERTS ==========")
    for alert in alerts:
        print(f"[{alert['level']}] {alert['message']}")


    ai_input = prepare_ai_summary(results, error_patterns)

    print("\nAI Input:")
    print(ai_input)

    ai_output = get_ai_analysis(ai_input)

    print("\n========== AI ANALYSIS ==========")
    print(ai_output)

 
if __name__ == "__main__":
    main()
