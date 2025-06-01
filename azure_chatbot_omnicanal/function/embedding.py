from langchain.schema import Document # type: ignore
from langchain_community.vectorstores import FAISS # type: ignore
from langchain_openai import AzureOpenAIEmbeddings # type: ignore
import os
import logging

def get_faq(conn):
    try:
        with conn.cursor() as cursor:
            query = "select pregunta as pregunta, respuesta as respuesta from faq;"
            cursor.execute(query)
            list_faq = cursor.fetchall()
            logging.info('Obtención de las preguntas y respuestas')
            return list_faq
    except Exception as e:
        logging.info('Error al obtener las preguntas y respuestas')
        raise Exception(f"Error al obtener las preguntas y respuestas")

def get_retriever(conn):
    # Recuperar FAQs de la base de datos
    faq_data = get_faq(conn)

    documents = [
        Document(page_content=f"Pregunta: {item[0]}\nRespuesta: {item[1]}")
        for item in faq_data
    ]
    
    embedding_model = AzureOpenAIEmbeddings(
        azure_deployment="text-embedding-3-small",  # <- Este es ahora azure_deployment
        openai_api_key=os.getenv("API_KEY"),
        azure_endpoint=os.getenv("API_BASE"),
        openai_api_version="2024-02-01",
        chunk_size=1000
    )
    
    vector_store = FAISS.from_documents(documents, embedding_model)

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    return retriever

"""    
    # Objeto Faiss de langchain
    index = vector_store.index
    index_bytes = FAISS.serialize_index(index)
"""