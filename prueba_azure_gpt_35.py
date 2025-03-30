from langchain_openai import AzureChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

os.environ["OPENAI_API_VERSION"] = "2024-02-01"
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")

llm = AzureChatOpenAI(
    deployment_name="prueba-gpt-35-turbo",
    temperature=0.1,
    max_tokens=20,
)

conversation = ConversationChain(
    llm=llm, 
    verbose=True,
    memory=ConversationBufferMemory()
)

print(conversation.predict(input="Cual es el pais mas grande del mundo?"))
print(conversation.predict(input="Cual es la capital de ese pais?"))