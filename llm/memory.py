from langchain.memory import ConversationBufferMemory

def get_memory(id):
    # Recupera o crea la memoria del chatbot
    memory = ConversationBufferMemory()
    
    lista_mensajes = get_mensajes(id)
    
    for mensajes in lista_mensajes:
        memory.save_context(mensajes[0], mensajes[1])

    return memory

def get_mensajes(id):
    # Obtener los mensajes de la BBDD, si existen
    bbdd = [1]
    if id in bbdd:
        return [[{"input": "Mi name is Claudio"},  {"output": "Good, Claudio!"}]]
        
    return []