from langchain.memory import ConversationBufferMemory

def get_memory(id):
    # Recupera o crea la memoria del chatbot
    memory = ConversationBufferMemory()
    lista_mensajes = get_mensajes(id)
    for mensajes in lista_mensajes:
        memory.save_context(mensajes.input, mensajes.output)
    return memory

def get_mensajes(id):
    # Obtener los mensajes de la BBDD
    lista_mensajes  = []
    return lista_mensajes