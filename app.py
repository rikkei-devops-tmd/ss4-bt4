import os

def load_application_config():
    api_endpoint = os.environ.get("API_ENDPOINT", "https://api.internal.local")
    return {
        "status": "active",
        "endpoint": api_endpoint
    }

if __name__ == "__main__":
    config = load_application_config()
    print("Application Endpoint:", config["endpoint"])
