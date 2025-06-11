import azure.functions as func
import logging
import json
import requests
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_URL = os.getenv("TELEGRAM_API_URL")
URL_AZURE_CHATBOT = os.getenv("URL_AZURE_CHATBOT")

app = func.FunctionApp()

@app.route(route="http_trigger_telegram", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger_telegram(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        data = req.get_json()
        logging.info("Contenido del mensaje:\n%s", json.dumps(data, indent=2))

        # Extraer el id y el texto del mensaje
        chat_id = data["message"]["chat"]["id"]
        mensaje_usuario = data["message"].get("text", "")
        usuario_telegram = data["message"]["from"]["id"]

        body = {
            "valor": str(usuario_telegram),
            "question": mensaje_usuario
        }
                
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.post(URL_AZURE_CHATBOT, json=body, headers=headers).text

        # Construir mensaje de respuesta
        response_text = f"{response}"

        # Llamar a Telegram para responder al usuario
        send_message_url = f"{TELEGRAM_API_URL}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": response_text
        }
        requests.post(send_message_url, json=payload)
    except ValueError:
        logging.error("Error procesando el mensaje: %s", str(e))
        return func.HttpResponse("Error procesando JSON", status_code=400)

    return func.HttpResponse("Envio correcto", status_code=200)