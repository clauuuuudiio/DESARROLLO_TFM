from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv
import os

load_dotenv()

# Usar un modelo gratuito de Hugging Face
hf_llm = HuggingFaceHub(repo_id="Qwen/QwQ-32B", huggingfacehub_api_token=os.getenv('API_TOKEN_HF'))

# Crear un prompt más específico
template = """
Contexto: Este es un sistema que responde a preguntas de manera precisa.
Pregunta: {question}
Respuesta:
"""
prompt = PromptTemplate(input_variables=["question"], template=template)

# Usar la cadena con el modelo de Hugging Face
llm_chain = LLMChain(llm=hf_llm, prompt=prompt)

# Realizar una consulta al modelo
question = "¿Qué es la inteligencia artificial?"

response = llm_chain.run(question)
print(response)