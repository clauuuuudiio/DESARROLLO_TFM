from transformers import pipeline
#from langchain.llms import HuggingFacePipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Cargar el modelo GPT-Neo 125M desde Hugging Face
# model_pipeline = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
model_pipeline = pipeline(
    "text-generation", 
    model="EleutherAI/gpt-neo-125M",
    tokenizer="EleutherAI/gpt-neo-125M",
    max_length=50,  # Limita la longitud de la respuesta
    truncation=True,  # Activa la truncación
    no_repeat_ngram_size=2,  # Evita repeticiones
)
# Integrar el pipeline de Hugging Face con LangChain
llm = HuggingFacePipeline(pipeline=model_pipeline)

# Crear un template de conversación
'''
template = """
You are a friendly and helpful conversational assistant.
User: {question}
bot:"""
'''
template = """
Eres un asistente conversacional amigable y servicial. Responde de manera clara y precisa.
Usuario: {question}
Asistente:"""

# Crear el prompt template en LangChain
prompt = PromptTemplate(
    input_variables=["question"],
    template=template,
)

# Crear la cadena LLM con LangChain
llm_chain = LLMChain(llm=llm, prompt=prompt)

# Función para interactuar con el asistente
def conversar(pregunta_usuario):
    return llm_chain.run(question=pregunta_usuario)

# Ejemplo de uso
pregunta = "What is the capital of Spain?"
respuesta = conversar(pregunta)
print("The response: \n" + respuesta)