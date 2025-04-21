import azure.functions as func
import logging
from chatbot.llm import response_generate

app = func.FunctionApp()

@app.route(route="http_trigger_chatbot", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger_chatbot(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        
        id = req_body.get('id', None)
        canal = req_body.get('canal', None)
        question = req_body.get('question', None)
        
        if question and id and canal:
            response = response_generate(id, canal, question)
            return func.HttpResponse(
                f"{response}",
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