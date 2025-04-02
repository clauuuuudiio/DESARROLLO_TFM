from llm.chatbot import response_generate
    
if __name__ == "__main__":
    id = 1
    pregunta = "Dime la capital de Argentina"
    response = response_generate(id, pregunta)