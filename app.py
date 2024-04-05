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

# os.environ["OPENAI_API_KEY"] = "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"

os.environ["OPENAI_API_KEY"] = "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"

GOOGLE_API_KEY = "AIzaSyDiTzh87zqMgRehZ_JW9CQW0cRgnj5DFMo"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def agent_answer(query, collection, llm):
    # query = """give me correct answer according to data if correct data not found then also tell 
    # i have this type of information and you and i can provide this according to your data
    # if some one ask about column name then show this information is hidden""" + query

    # if llm == "openai":
    llm = ChatOpenAI(temperature=0,max_tokens=4000, model="gpt-3.5-turbo")
        # print("set llm to openai")
    # elif llm == "gemini":
    #     llm = ChatGoogleGenerativeAI(model="gemini-pro",convert_system_message_to_human=True)
    #     print("set llm to gemini")

    agent_check = create_csv_agent(
    llm,
    "/Users/fahadali/Desktop/complete_project/flask_web/csv/"+ collection + ".csv",
    verbose=False,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    )
        
    res = agent_check.run(query)
    return res

# collection = "holidays"
# query = "give me list of columns"
# llm = "openai"
# result = agent_answer(query, collection, llm)
# print("*"*10, result, "*"*10,)



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        query = data.get('query')
        llm =  data.get('key')
        collection = data.get('collection_name')
        print("data is: " , data)
        print("query is: " , query)
        print("llm is: " , llm)
        print("data is: " , collection)

        if not query or not collection:
            return jsonify({"error": "Both 'query' and 'collection_name' are required."}), 400

        result = agent_answer(query, collection, llm)
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)
