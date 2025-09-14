import os
from datetime import datetime

def log_result(tool_name, data):
    os.makedirs("logs", exist_ok=True)
    filename = f"logs/{tool_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)
