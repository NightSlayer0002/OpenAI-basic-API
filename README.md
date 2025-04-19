# OpenAI-basic-API

# Basic OpenAI API Use (Python)

This is a simple example of using OpenAI's Chat Completion API (`gpt-3.5-turbo model`) with Python.  
It shows how to make a basic multi-turn conversation with an AI model — like asking a question and getting a creative response (e.g., generating a song!).

---

## What It Does

- Uses the `chat.completions.create()` method from OpenAI to send a list of messages (like a chat history).
- Sends a simple query:  
  - *Who won the World Series in 2020?*  (optional)
  - Then asks the AI to *make a song about Chihiro* (from *Spirited Away*).
- Returns the full response from the model.

---

## Why This Project?

This example lays the **foundation** for more advanced ideas:
- 🔄 Convert into a full chatbot with real-time chat.
- 🖥️ Add a user interface (using django, Flask, or React).
- 🤖 Connect it with messaging apps like Telegram or Discord.
- 🎨 Change the prompts to turn it into an idea generator, creative writer, or assistant.

---

## How to Run

1. Make sure you have Python installed.

2. Install the required package (`boltiotai`):
   ```
   pip install boltiotai
