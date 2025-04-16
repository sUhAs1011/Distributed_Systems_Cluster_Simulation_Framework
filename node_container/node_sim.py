import os
import time
import requests

# Get environment variables for NODE_ID and API_URL
NODE_ID = os.getenv("NODE_ID")
API_URL = os.getenv("API_URL")

# Ensure that NODE_ID and API_URL are set
if not NODE_ID or not API_URL:
    raise ValueError("NODE_ID and API_URL environment variables must be set.")

# Print initial log to confirm the script started
print(f"[Node {NODE_ID}] Started with API Server at {API_URL}", flush=True)

# Start an infinite loop to send heartbeat
while True:
    try:
        # Send a heartbeat request to the API server
        response = requests.post(f"{API_URL}/heartbeat", json={"node_id": NODE_ID})

        # Log the result of the heartbeat request
        if response.status_code == 200:
            print(f"[Node {NODE_ID}] Heartbeat sent successfully: {response.status_code}", flush=True)
        else:
            print(f"[Node {NODE_ID}] Heartbeat failed with status code: {response.status_code}", flush=True)

    except Exception as e:
        # If there is an error in the heartbeat request, log the error
        print(f"[Node {NODE_ID}] Heartbeat failed: {e}", flush=True)

    # Sleep for 30 seconds before sending the next heartbeat
    time.sleep(30)
