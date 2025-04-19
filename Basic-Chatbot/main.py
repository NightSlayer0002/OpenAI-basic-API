from boltiotai import openai
import os
import sys

question = input("Q: What is your question/message?\n")

while True:
    try:
        # Check if the API key is set up
        openai.api_key = os.environ['OPENAI_API_KEY']
        if openai.api_key == "":
            sys.stderr.write("""
            You haven't set up your API key yet.
            
            If you don't have an API key yet, visit:
            
            https://platform.openai.com/signup
          
            1. Make an account or sign in
            2. Click "View API Keys" from the top right menu.
            3. Click "Create new secret key"
          
            Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
            """)
            exit(1)

        # Create the response using OpenAI's chat API
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system",
                "content": "You are a helpful assistant."
            }, {
                "role": "user",
                "content": "Who won the world series in 2020?"
            }, {
                "role": "assistant",
                "content": "The Los Angeles Dodgers won the World Series in 2020."
            }, {
                "role": "user",
                "content": question
            }])

        # Print the assistant's reply
        output = response['choices'][0]['message']['content']
        print("A:", output, "\n")

        # Ask for the next question
        question = input("Q: What is your next question/message?\n")

    except Exception as e:
        print(f"An error occurred: {e}")
        break  # Break the loop if an error occurs
