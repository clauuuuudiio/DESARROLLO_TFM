from dotenv import load_dotenv # type: ignore
from langchain_openai import AzureChatOpenAI # type: ignore

def get_llm():
    load_dotenv()

    llm = AzureChatOpenAI(
        deployment_name="prueba-gpt-35-turbo",
        temperature=0,
        max_tokens=100,
    )
    
    return llm