import math
import time
import subprocess

TOTAL_DURATION = 24 * 60 * 60  # 24 hours in seconds
INTERVAL = 10 * 60  # Check every 10 minutes

def seasonality_function(t):
    """Returns a scaled sine value to simulate the user count based on time.
       The function peaks at 5000 and goes down to 0.
    """
    return 2500 * (math.sin(math.pi * t / TOTAL_DURATION) + 1)

def run_locust(users):
    """Start a Locust instance with the specified number of users."""
    command = f"locust -f locust_eks.py --users {users} --run-time {INTERVAL}s --headless"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    start_time = time.time()
    while time.time() - start_time < TOTAL_DURATION:
        current_time = time.time() - start_time
        users = seasonality_function(current_time)
        run_locust(int(users))
        time.sleep(INTERVAL)
