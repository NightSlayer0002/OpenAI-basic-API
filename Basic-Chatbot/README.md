# OpenAI-basic-API

## Basic Chatbot (main.py)

This is a basic implementation of OpenAI’s Chat Completion API using Python.  
It lets you ask a question, get an answer, and continue the conversation in a loop.

**This project uses API access provided via Bolt IoT.**  
I paid for the training from Bolt IoT, and this API key will only work inside that setup (like Replit used in the course).  
If you want to run it elsewhere, you’ll need your own OpenAI API key.

---

## What it does

- Uses the GPT-3.5-turbo model via `chat.completions.create()`  
- Starts with a simple system message and 2 example messages  
- Takes user input  
- Sends it to OpenAI  
- Prints the response  
- Loops the conversation

---

## How to run it

1. Make sure you have Python installed.

2. Install the required package (boltiotai):
   ```bash
   pip install boltiotai
   
3. Set your OpenAI API key as an environment variable: (Replit: Tools->Secrets->New Secret)
   ```bash
   export OPENAI_API_KEY=your_secret_key_here

4. Run the script:
   ```bash
   python main.py

## Sample Output:
   ```
   Environment updated. Reloading shell...
Q: What is your question/message?
hi how are you?
A: Hello! I'm just a virtual assistant, so I don't have feelings, but I'm here to help you. How can I assist you today? 

Q: What is your next question/message?
What is OpenAI API?
A: The OpenAI API is a powerful artificial intelligence model developed by OpenAI that allows developers to access state-of-the-art natural language processing capabilities in their applications. It provides a range of language models that can generate human-like text and perform various NLP tasks such as language translation, summarization, and more. Developers can use the OpenAI API to create innovative applications that leverage the power of AI to solve complex problems. 

Q: What is your next question/message?
How are you sending or generating these messages?
A: I am a computer program developed by a team of engineers and writers. I generate responses based on a vast set of information and programming algorithms to provide you with helpful and accurate responses. 

Q: What is your next question/message?
Tell me a joke
A: Sure, here's a joke for you:

Why did the math book look sad?
Because it had too many problems. 

Q: What is your next question/message?
