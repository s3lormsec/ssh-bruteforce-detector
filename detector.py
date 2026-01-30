import re
from collections import defaultdict

FAILED_PATTERN = re.compile(r"Failed password .* from ([0-9.]+)")

def analyze_log(file_path, threshold=5):
    failed_attempts = defaultdict(int)

    try:
        with open(file_path, "r") as log_file:
            for line in log_file:
                match = FAILED_PATTERN.search(line)
                if match:
                    ip = match.group(1)
                    failed_attempts[ip] += 1

        print("\nSSH Brute-Force Analysis Report")
        print("--------------------------------")

        suspicious = False
        for ip, count in failed_attempts.items():
            print(f"{ip} -> {count} failed attempts")
            if count >= threshold:
                suspicious = True

        if suspicious:
            print("\n⚠️  Potential brute-force activity detected.")
        else:
            print("\n✅ No brute-force activity detected.")

    except FileNotFoundError:
        print("Log file not found. Check the file path.")

if __name__ == "__main__":
    log_path = input("Enter path to SSH auth log: ")
    analyze_log(log_path)

