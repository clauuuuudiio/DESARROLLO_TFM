import azure.functions as func
import logging
from function.chains import get_validation_chain
from function.agent import get_agent
from function.memory import get_memory, save_memory
from function.database import DatabaseConnection
from function.user_handler import get_id_mdm
from function.omnicanal_handler import verify_data
from function.response_clear import clear_backticks

app = func.FunctionApp()

@app.route(route="http_trigger_chatbot", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger_chatbot(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Desplegado v5.8
    try:
        req_body = req.get_json()
        
        valor = req_body.get('valor', None)
        question = req_body.get('question', None)

        if question and valor:
            
            validation_chain = get_validation_chain()
            validate = validation_chain.invoke({'input': question}).content
            
            if validate:                
                # Conexión con la base de datos
                db = DatabaseConnection()
                conn = db.connect()

                # Obtener el id de mdm
                id_mdm = get_id_mdm(valor, conn)
                
                # Revisar datos (omnicanalidad)
                exp = verify_data(id_mdm, valor, question, conn)

                # Crear chatbot y responder de manera correcta 
                memory = get_memory(id_mdm, conn)
                
                agente = get_agent(memory, conn, exp)
                
                response = agente.invoke(question)["output"]
                response = clear_backticks(response) # Eliminar ```
                                    
                save_memory(id_mdm, question, response, conn)
                db.close()
                
                return func.HttpResponse(
                    f"{response}",
                    status_code=200
                )
            else:
                return func.HttpResponse(
                    f"El mensaje enviado no es válida",
                    status_code=200
                )
        else:
            return func.HttpResponse(
                f"Falta un campo en la petición",
                status_code=400
            )
    except Exception as e:
        return func.HttpResponse(
             f"Error: {e}",
             status_code=400
        )