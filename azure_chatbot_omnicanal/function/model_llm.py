from dotenv import load_dotenv # type: ignore
from langchain_openai import AzureChatOpenAI # type: ignore
import os

def get_llm():
    load_dotenv()
    
    llm = AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        temperature=0    
    )
    
    return llm