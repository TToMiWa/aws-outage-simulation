import random
import time

def upload_weather_data():
    """Simulates a flaky server connection."""
    print(" Attempting to upload data...")
    
    # 70% chance of failure (Chaos!)
    if random.random() < 0.7:
        # This acts like the AWS 'DNS Failure'
        raise ConnectionError("🔥 Server is unreachable!")
        
    return " Success: Data uploaded!"

for attempt in range(5):
    delay = 2 ** attempt
    jitter = random.uniform(0, 1)
    try:
        result = upload_weather_data()
        print(result)
        break

    except ConnectionError:
        wait_time = delay + jitter
        print(f"⚠️ Attempt {attempt + 1} failed. Retrying in {wait_time} seconds...")
        time.sleep(wait_time)

    else:
        print(" Critical Error: All 5 attempts failed. Giving up.")


