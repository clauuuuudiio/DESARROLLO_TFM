from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)
mensajes = [[{"input": "hi"}, {"output": "whats up"}], [{"input": "nice"}, {"output": "okey"}]]

memory.save_context([[{"input": "hi"}, {"output": "whats up"}], [{"input": "nice"}, {"output": "okey"}]])

print(memory.load_memory_variables({}))