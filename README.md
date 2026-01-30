# ssh-bruteforce-detector
# SSH Brute-Force Detector

A Python tool that analyzes SSH authentication logs to identify potential brute-force attacks based on repeated failed login attempts from the same IP address.

## Features
- Parses SSH auth logs
- Counts failed login attempts per IP
- Flags suspicious activity based on a configurable threshold

## Usage
```bash
python3 detector.py

