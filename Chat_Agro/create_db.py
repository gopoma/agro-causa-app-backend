import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

print("xd", os.environ.get("OPENAI_API_KEY"))

def create_database(pdf_path, persist_directory):
    # Verificar si el archivo PDF existe
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"El archivo {pdf_path} no existe.")

    # Cargar y procesar el documento PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    # Dividir el documento en fragmentos
    c_splitter = CharacterTextSplitter(chunk_size=600, chunk_overlap=100, separator=' ')
    docs = c_splitter.split_documents(pages)

    # Crear los embeddings
    embedding = OpenAIEmbeddings()

    # Crear la base de datos en Chroma y persistirla
    vectordb = Chroma.from_documents(documents=docs, embedding=embedding, persist_directory=persist_directory)
    print(f"Base de datos creada y guardada en: {persist_directory}")

if __name__ == "__main__":
    pdf_path = os.path.join(os.path.dirname(__file__), "data", "entrenamiento", "entrenamiento.pdf")
    persist_directory = "./data/chroma"
    create_database(pdf_path, persist_directory)