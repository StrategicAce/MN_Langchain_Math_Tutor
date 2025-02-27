# Langchain based Math Tutor
GorqCloud and llama3-70b-8192 math tutor application 

This project is a math tutor that uses the LangChain library to process questions sent via a JSON file. The system checks if the question is truly a math-related one by verifying the presence of mathematical operators. If it is, the question is passed to the LLaMA3-70b-8192 model, which responds to the question using the `chain.invoke()` method.

## Prerequisites

Before getting started, ensure you have the following installed:

- Python 3.8 or higher
- LangChain library
- JSON library
- Access to the LLaMA3-70b-8192 model in the GroqCloud environment

You can install the required libraries using pip and the requirements file:

```bash
pip install -r /path/to/requirements.txt
```

## Load groq token

Using a Colab notebook, use the `userdata.get()` to load the GroqCloud API key to the environment

```bash
from groq import Groq
from google.colab import userdata

GROQ_TOKEN = userdata.get("GROQ_TOKEN")
```
If you are using any other framework define the APi key using:

```bash
import os
os.environ['GROQ_API_KEY'] = userdata.get('GROQ_API_KEY')
```

## Using the JSON file to load questions:

The JSON file used in this project follows a specific structure. It contains a dictionary named "chatbot", which includes two main keys:

"question": Refers to the question that will be directed to the math tutor. This is the input that the system will process to determine if it is math-related. If it is, the question will be sent to the LLaMA3-70b-8192 model for an answer.

"responses": Contains a list of pre-programmed responses. These responses are used in specific scenarios, such as when the question is not math-related or when the system needs to provide a default reply.

Example of the JSON File:
Here is an example of how the JSON file should be structured:

```bash
{
  "chatbot": {
    "question": "help me solve this equation: 2x^2 + 4x – 6 = 0",
    "responses": {
      "default": "I'm sorry, I didn't understand that."
    }
  }
}
```

## Uploading the JSON file: 

The JSON file will be uploaded to the system using the json library. Paste a valid file path to read and process the JSON file:
```bash
import json

with open('/path to/question.json','r') as file:
  data = json.load(file)

print(data)
```

