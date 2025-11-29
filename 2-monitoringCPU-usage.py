# Chandan
# Hero Vired Assigned 1 - Python Programming

# Q2. Write a Python program to monitor the health of the CPU.
# 


import time
import psutil  # pip install psutil


def monitor_cpu(threshold=80, interval=1):
    """
    Continuously monitor CPU usage and print an alert
    if usage exceeds the given threshold.
    """
    print("Monitoring CPU usage...")

    while True:
        try:
            # Get current CPU usage percentage over the given interval
            usage = psutil.cpu_percent(interval=interval)  # [web:55][web:60][web:63]

            # Print current usage (optional, but useful to see)
            print(f"Current CPU usage: {usage}%")

            # Check against threshold
            if usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {usage}%")

        except KeyboardInterrupt:
            # Gracefully exit if the user presses Ctrl+C
            print("\nMonitoring stopped by user.")
            break
        except Exception as e:
            # Catch-all for other unexpected errors
            print(f"An error occurred while monitoring CPU: {e}")
            # Small sleep to avoid tight error loop
            time.sleep(1)


if __name__ == "__main__":
    # You can change the threshold and interval if needed
    # e.g., monitor_cpu(threshold=75, interval=2)
    monitor_cpu(threshold=80, interval=1)
