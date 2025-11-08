from datetime import datetime

def log_info(message: str):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] [INFO] {message}")

def log_error(message: str):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] [ERROR] {message}")
