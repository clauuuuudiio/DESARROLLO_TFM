from langchain_openai import AzureChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
#from dotenv import load_dotenv
import os
from llm.memory import get_memory

def llm_generate():
    # Cargar las variables del archivo .env para crear el LLM
    #load_dotenv()
    # Cargar las variables mediante os
    os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")
    os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")
    os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
    
    llm = AzureChatOpenAI(
        deployment_name="prueba-gpt-35-turbo",
        temperature=0,
        max_tokens=10,
    )
    
    return llm

def prompt_generate():
    template = """
    Eres un asistente conversacional, que debe responder la pregunta o duda del usuario
    
    {history}
    
    El usuario a preguntado "{input}", respondela de manera amigable.
    Response:
    """
    
    prompt = PromptTemplate(input_variables=["history", "input"], template=template)
    
    return prompt

def chatbot_generate(id):
    chatbot = ConversationChain(
        llm=llm_generate(), 
        memory=get_memory(id),
        prompt=prompt_generate()
    )
    
    return chatbot

def response_generate(id, pregunta):
    chatbot = chatbot_generate(id)
    response = chatbot.predict(input=pregunta)
    return response