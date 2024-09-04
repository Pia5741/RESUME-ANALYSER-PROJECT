from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
google_api_key = os.getenv('GOOGLE_API_KEY')

# Use the API key in your application
print(f"Your Google API Key is: {google_api_key}")

# Example usage: Pass the API key to a function or API request
def use_api_key(api_key):
    # Replace with your actual API request code
    pass

use_api_key(google_api_key)

