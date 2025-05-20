from langchain.agents import initialize_agent, AgentType # type: ignore
from function.tools import get_tools
from function.model_llm import get_llm
from langchain.schema import SystemMessage # type: ignore

def get_agent(memory, conn):
    tools = get_tools(conn)
    llm = get_llm()

    # Creacion del agente
    agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,    
    verbose=False,
    agent_kwargs={"prefix": "Responde en el mismo idioma que el del mensaje."}
    )
    
    return agent