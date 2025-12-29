import os, time, hashlib

# 100% SILENT CONFIGURATION
MONITOR_DIR = "."
LOG_FILE = "logs/sentinel.log"

def get_hash(f):
    try:
        with open(f, 'rb') as fb: return hashlib.sha256(fb.read()).hexdigest()
    except: return None

if __name__ == "__main__":
    # No print statements = No terminal output = No phone alerts
    baseline = {f: get_hash(f) for f in os.listdir(MONITOR_DIR) if os.path.isfile(f)}
    
    while True:
        time.sleep(30) # Check every 30 seconds
        for f in [f for f in os.listdir(MONITOR_DIR) if os.path.isfile(f)]:
            h = get_hash(f)
            if f not in baseline or baseline[f] != h:
                # ONLY write to the hidden file. Do NOT print to screen.
                with open(LOG_FILE, "a") as log:
                    log.write(f"Change detected: {f}\n")
                baseline[f] = h
