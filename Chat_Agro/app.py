from flask import Flask
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

app = Flask(__name__)

def load_database(persist_directory):
    embedding = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
    return vectordb

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
