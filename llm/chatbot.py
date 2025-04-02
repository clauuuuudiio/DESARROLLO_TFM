from langchain_openai import AzureChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from memory import get_memory

# Cargar las variables del archivo .env
load_dotenv()

os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")

# Generar el modelo
llm = AzureChatOpenAI(
    deployment_name="prueba-gpt-35-turbo",
    temperature=0,
    max_tokens=100,
)


def llm_generate():
    llm = AzureChatOpenAI(
        deployment_name="prueba-gpt-35-turbo",
        temperature=0.1,
        max_tokens=100,
    )
    return llm
    
def chatbot_generate(id):
    chatbot = ConversationChain(
        llm=llm_generate(), 
        memory=get_memory(id),
        prompt=PromptTemplate(input_variables=["history", "input"], template=template_generate())
    )
    return chatbot

def template_generate():
    template = """
    Eres un asistente conversacional, que debe responder la pregunta o duda del usuario
    
    {history}
    
    El usuario a preguntado "{input}", respondela de manera amigable.
    """
    return template

def response_generate(id, pregunta):
    chatbot = chatbot_generate()
    response = chatbot.predict(input=pregunta)
    return response