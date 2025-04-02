from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

os.environ["AZURE_INFERENCE_ENDPOINT"] = os.getenv("AZURE_INFERENCE_ENDPOINT_GPT")
os.environ["AZURE_INFERENCE_CREDENTIAL"] = os.getenv("AZURE_INFERENCE_CREDENTIAL_GPT")
model_name = os.getenv("MODEL_NAME_GPT")

llm = AzureAIChatCompletionsModel(
    model_name=model_name,
    max_tokens=20,
)

response = llm.invoke('Cual es la capital de españa?')

print(response.content)