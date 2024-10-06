from flask import Flask, request, Response, jsonify
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_chroma import Chroma
from langchain.memory import ConversationSummaryMemory

app = Flask(__name__)

def load_database(persist_directory):
    embedding = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    return vectordb

persist_directory = "./data/chroma"
vectordb = load_database(persist_directory)
retriever = vectordb.as_retriever(search_kwargs={"k": 6})
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.6)
history = ConversationSummaryMemory(llm = llm)
r = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, memory = history)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
