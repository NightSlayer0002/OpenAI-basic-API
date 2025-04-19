from boltiotai import openai  # Importing OpenAI from boltiotai SDK
import os
import sys

# Get the API key securely from environment variable
openai.api_key = os.environ['OPENAI_API_KEY']

# Check if the API key is missing
if openai.api_key == "":
    sys.stderr.write("""
    You haven't set up your API key yet.

    Steps to set it up:
    1. Go to https://platform.openai.com/signup
    2. Create/sign in to your account.
    3. Click "View API Keys" → "Create new secret key"
    4. Add it as an environment variable OPENAI_API_KEY using Secrets tool or export it.
    """)
    exit(1)

# Array of messages simulates a chat between user and AI
# This can be converted into a UI later with real-time input/output
response = openai.chat.completions.create(     #Chat Completion API by OpenAI
    model="gpt-3.5-turbo",  # Using GPT-3.5 Turbo model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},  # Sets the AI's personality
        #{"role": "user", "content": "Who won the world series in 2020?"},  # First user message (optional)
        #{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},  # AI response (optional)
        {"role": "user", "content": "Make a song about chihiro"}  # Second user message
    ]
)

# Print the full AI response (can be adjusted to just print content)
print(response)
