import os
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

os.environ['GROQ_API_KEY'] = "your-groq-api-key"


#load the JSON file:
with open('/path to/test.json','r') as file:
  data = json.load(file)

#define teacher's model:
chat = ChatGroq(temperature=0, groq_api_key= GROQ_API_KEY, model_name="llama3-70b-8192") #


# Define system prompt for reject any question that is not math related:
system = "You are now a famous math virtual teacher, you shall only accept questions that present any kind of math symbols, like + , -, *, /, and any other. For a question that doesn't contain any math symbols, tell the user to try again"
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

# create chain:
chain = prompt | chat


# define question and math-related symbols:
question = data["chatbot"]["question"]
math_symbol = ['+', '-', '×', '÷', '=']

# search for a math-related symbol in the question:
if any(symbol in question for symbol in math_symbol):
  
# pass the question to the math teacher:
  print(chain.invoke({"text": question}))
else:

# negative case respose: 
  response = data["chatbot"]["responses"]["default"]  
  print(response)