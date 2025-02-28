import os
from pprint import pprint
import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser

os.environ['GROQ_TOKEN'] = "your-groq-api-key"

GROQ_LLM = ChatGroq(temperature=0, groq_api_key= GROQ_TOKEN, model_name="llama3-70b-8192")

#Question reciver and filte promp
question_reciver = PromptTemplate(
    template="""
    You are a question Categorizer agent, you are a master at identifing the nature of the question proposed by the user it in a useful way


    Conduct a comprehensive analysis of the email provided and categorize into one of the following categories:
        math - when the asked question is math related, this question should present math symbols like +, -, *, / or any other
        non_math = when the asked question is not math related

            Output a single cetgory only from the types ('math, non_math') \

            if you categorize a question as a non_math question, please tell the user to try again and do not proceed to the next step!

             Return a JSON with a single key 'keywords' with no more than 2 keywords, the complete initial question asked by the student and category, dont' give any other premable or explaination. use the following exemple:

          
    {{
        "keywords": {{
            "question": "(question asked by the user)",
            "category": "(category that you chose)"
        }}
    }}
    
    QUESTION CONTENT:\n\n {initial_question} \n\n
    """,
    input_variables=["initial_question"],
)

question_category_generator = question_reciver | GROQ_LLM | StrOutputParser()

initial_question = """Please, help me solve this equation: 5x2 + 2x + 2 = 0
#"""

#initial_question="""Who is napoleon Bonaparte
#"""


question_result = question_category_generator.invoke({"initial_question": initial_question})
print(question_result)

#Converting categorization as a dictionary
try:
    question_dict = json.loads(question_result)
except json.JSONDecodeError as e:
    print("Erro ao decodificar JSON:", e)
    question_dict = {}
  
#Saving JSON file 
with open('question.json', 'w') as f:
    json.dump(question_dict, f, indent=4)


# question Answering prompt
question_answering = PromptTemplate(
    template="""

    You are a famous math teacher, trained to anwser any math question for children from 8 to 12 years old.

    given the CATEGORY of the question, respond as the following:

      for the "math" CATEGORY, solve the equation or anser as aked in QUESTION

      for the "non_math" CATEGORY, tell the user to try again with a math question

    QUESTION: {initial_question} \n
    CATEGORY: {category} \n
    """,
    input_variables=["initial_question","category"],
)

question_answering = question_answering | GROQ_LLM | JsonOutputParser()

#load JSON categorization file
with open('question.json', 'r') as f:
  data = json.load(f)

initial_question = data["keywords"]["question"]
category = data["keywords"]["category"]

#Answering the question
print(question_answering.invoke({"initial_question": initial_question, "category":category}))
