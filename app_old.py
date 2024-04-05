from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain_community.document_loaders.mongodb import MongodbLoader
from langchain.text_splitter import CharacterTextSplitter

import pymongo
# import pandas as pd
import os
from flask import Flask, render_template
import time

from flask import Flask, request, jsonify


import google.generativeai as genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = "AIzaSyDiTzh87zqMgRehZ_JW9CQW0cRgnj5DFMo"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# !pip install pymongo
# !pip install motor
# pip install chromadb

OPENAI_API_KEY = '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'
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# add this import for running in jupyter notebook
import nest_asyncio

nest_asyncio.apply()

# MongoDB connection information
DB_USER = "dazboardsdapp2tab"
DB_PASSWORD = "dHhoBcZaEM20wod02DY24RkK"
DB_NAME = "app2db"
HOST = "74.208.107.144"

# MongoDB connection URI
uri = f"mongodb://{DB_USER}:{DB_PASSWORD}@{HOST}/{DB_NAME}"

# Create MongoDB client
client = pymongo.MongoClient(uri)

# Access the database
db = client[DB_NAME]

if db is not None:
    print("Connected to MongoDB successfully!")
else:
    print("Failed to connect to MongoDB.")


    
def extract_date_from_collection(collection_name, db):
    collection_name = collection_name
    print(collection_name,"\n")
    
    loader = MongodbLoader(
    connection_string= f"mongodb://{DB_USER}:{DB_PASSWORD}@{HOST}/{DB_NAME}",
    db_name=DB_NAME,
    collection_name= collection_name
    )
    
    return loader


res = 'holidays,orders,xeroinvoices,products,resellers,reviews,xerobanktransactions,vouchers,appliedtemplates,omniemails'


def check_collection_valid(name):
    res = 'holidays,orders,xeroinvoices,products,resellers,reviews,xerobanktransactions,vouchers,appliedtemplates,omniemails'
    res = res.split(",")
    if name in res:
        print("yes this name in collection")
        return True
    else:
        print("Please Enter Correct collect name, \n\n you can set one of them \n", ", ".join(res))
    

def extract_loader_date_from_collection(collection_name, db):
    try:
        collection_name = collection_name
        res = check_collection_valid(collection_name)
        if res == True:
            print("yes")
            loader = MongodbLoader(
            connection_string= f"mongodb://{DB_USER}:{DB_PASSWORD}@{HOST}/{DB_NAME}",
            db_name=DB_NAME,
            collection_name= collection_name
            )
            return loader
    except Exception as E:
        print(E)
    

def chat_with_data(query, collection_name, llm):
    try:
        if llm == "openai":
            llm = OpenAI()
        elif llm == "gemini":
            llm = ChatGoogleGenerativeAI(model="gemini-pro",convert_system_message_to_human=True)

        start_time=time.time()
        loader = extract_loader_date_from_collection(collection_name, db)
        end_time=time.time()
        print("Diffi laoder:-----",end_time-start_time)
        try: 
            docs = loader.load()
        except:
            return "Enter Correct name \n" + "You can select from\n" + res  
        index_creator = VectorstoreIndexCreator()
        docsearch = index_creator.from_loaders([loader])
        start_time_=time.time()
        chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.vectorstore.as_retriever(), input_key="question")
        # query = "is there chat coloumns exist in my database"
        query = query
        response = chain({"question": query})
        end_time_=time.time()
        print("Diffi laoder:-----",end_time_-start_time_)
        print(response['result'])
        return response['result']
    except Exception as E:
        print("\n"*5, E)



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
        collection_name = data.get('collection_name')
        print("data is: " , data)
        print("query is: " , query)
        print("llm is: " , llm)
        print("data is: " , collection_name)

        if not query or not collection_name:
            return jsonify({"error": "Both 'query' and 'collection_name' are required."}), 400

        result = chat_with_data(query, collection_name, llm)
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)
