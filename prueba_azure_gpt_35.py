from langchain_openai import AzureChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

os.environ["OPENAI_API_VERSION"] = "2025-01-01-preview"
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")

llm = AzureChatOpenAI(
    deployment_name="prueba-gpt-35-turbo",
    temperature=0.1,
    max_tokens=100,
)

# Crear el objeto de memoria
memory = ConversationBufferMemory()
memory.save_context({"input": "¿Cómo funciona la inteligencia artificial?"}, {"output": "La inteligencia artificial funciona a través de algoritmos y modelos matemáticos que permiten a las computadoras analizar datos, aprender patrones y tomar decisiones sin intervención humana directa. Se basa en técnicas como el aprendizaje automático y las redes neuronales, que permiten a los sistemas mejorar su desempeño con el tiempo a medida que procesan más información."})
memory.save_context({"input": "¿Cuáles son los tipos de inteligencia artificial?"}, {"output": "Existen tres tipos principales de inteligencia artificial: la IA débil, que se enfoca en tareas específicas (como asistentes virtuales o filtros de spam); la IA fuerte, que hipotéticamente podría razonar y aprender como un ser humano; y la superinteligencia, un concepto aún teórico donde la IA superaría la inteligencia humana en todos los aspectos."})

template = """
    Eres un asistente conversacional, que debe responder la pregunta o duda del usuario
    
    {history}
    
    El usuario a preguntado: "{input}". 
    respondela de manera amigable.
    """

conversation = ConversationChain(
    llm=llm, 
    memory=memory,
    prompt = PromptTemplate(input_variables=["input"], template=template)
)

print(conversation.predict(input="Cual es la capital de españa?"))

# Recuperar y mostrar la memoria
'''
print("\nHistorial de la conversación:")
print(memory.buffer)

print("\nOTRA PRUEBA:")
print(memory.load_memory_variables({}))
'''
