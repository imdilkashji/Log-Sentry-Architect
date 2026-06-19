def analyze_server_logs():
    error_count = 0
    total_lines = 0
    critical_events = []

    print("[*] Initializing Log-Sentry Engine extraction...")
    try:
        with open("server.log", "r") as src:
            for line in src:
                total_lines += 1
                if "ERROR" in line or "CRITICAL" in line:
                    error_count += 1
                    if "CRITICAL" in line:
                        critical_events.append(line.strip())
                        
        error_density = (error_count / total_lines) * 100 if total_lines > 0 else 0
        
        # Output the report to terminal and write to a report file
        with open("metrics_report.txt", "w") as report:
            report.write("=== LOG-SENTRY ANALYTICS METRICS REPORT ===\n")
            report.write(f"Total Stream Vectors Audited: {total_lines}\n")
            report.write(f"Anomalous Vectors Isolated  : {error_count}\n")
            report.write(f"Calculated Error Density     : {error_density:.2f}%\n\n")
            report.write("--- CRITICAL SYSTEM VECTOR BREAKDOWN ---\n")
            for idx, event in enumerate(critical_events):
                report.write(f"{idx+1}. {event}\n")
                
        print("[+] Processing complete. 'metrics_report.txt' generated successfully.")
        print(f"[*] Operational Health: Total Logs: {total_lines} | System Error Density: {error_density:.2f}%")
        
    except FileNotFoundError:
        print("[-] Execution Error: 'server.log' not found. Run 'mock_generator.py' first.")

if __name__ == "__main__":
    analyze_server_logs()