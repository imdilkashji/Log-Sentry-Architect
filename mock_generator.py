import random
import time

def generate_logs():
    levels = ["INFO", "DEBUG", "WARN", "ERROR", "CRITICAL"]
    messages = [
        "Database connection stable",
        "API Gateway timeout",
        "User authentication success",
        "Memory leak detected in heap allocation",
        "Cache flush successful"
    ]
    
    print("[*] Simulating live server environment... writing 'server.log'")
    with open("server.log", "w") as log_file:
        for i in range(150):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            lvl = random.choice(levels)
            msg = random.choice(messages)
            log_file.write(f"[{timestamp}] [{lvl}] - {msg}\n")
    print("[+] 150 server log vectors successfully written to disk.")

if __name__ == "__main__":
    generate_logs()








