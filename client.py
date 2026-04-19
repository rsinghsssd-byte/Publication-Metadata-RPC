import xmlrpc.client
import json

# Connect to the local server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Load metadata from file
with open("metadata.json", "r") as f:
    metadata = f.read()

# Call the remote analysis function
print("Sending metadata to server for analysis...")
response = proxy.analyze(metadata)
print("\n--- ANALYSIS RESULTS ---")
print(response)