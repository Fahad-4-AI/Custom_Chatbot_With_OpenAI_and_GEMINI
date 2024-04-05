from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os
import pandas as pd

from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI

from flask import Flask, render_template, request, jsonify
import time

import google.generativeai as genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = "AIzaSyDiTzh87zqMgRehZ_JW9CQW0cRgnj5DFMo"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


llm = ChatGoogleGenerativeAI(model="gemini-pro",convert_system_message_to_human=True)


os.environ["OPENAI_API_KEY"] = "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"

def agent_answer(query, collection):
    print(collection)
    llm = ChatGoogleGenerativeAI(model="gemini-pro",convert_system_message_to_human=True)
    agent_check = create_csv_agent(
    llm,
    "/Users/fahadali/Desktop/complete_project/flask_web/csv/"+ collection + ".csv",
    verbose=False,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    )
        
    res = agent_check.run(query)
    return res

collection = "holidays"
query = "give me best selling product on last month"
result = agent_answer(query, collection)
print("\n\n\n",result)



# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/chat', methods=['POST'])
# def chat():
#     try:
#         data = request.get_json()
#         query = data.get('query')
#         llm =  data.get('key')
#         collection = data.get('collection_name')
#         print("data is: " , data)
#         print("query is: " , query)
#         print("llm is: " , llm)
#         print("data is: " , collection)

#         if not query or not collection:
#             return jsonify({"error": "Both 'query' and 'collection_name' are required."}), 400

#         result = agent_answer(query, collection)
#         return jsonify({"result": result})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True,host='0.0.0.0', port=8000)
