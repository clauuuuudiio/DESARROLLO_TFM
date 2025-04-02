from llm.chatbot import response_generate
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

if __name__ == "__main__":
    # Prueba con usuario conocido
    id = 1
    pregunta = "Dime mi nombre"
    response_con_id = response_generate(id, pregunta)
    print(response_con_id)
    
    print("------------------------")
    
    # Prueba con usuario desconocido
    pregunta = "Dime mi nombre"
    response_sin_id = response_generate(None, pregunta)
    print(response_sin_id)