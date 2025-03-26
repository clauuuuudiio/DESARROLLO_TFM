from transformers import pipeline

# Cargar el modelo GPT-Neo 1.3B desde Hugging Face (modelo más grande)
model_pipeline = pipeline(
    "text-generation", 
    model="EleutherAI/gpt-neo-1.3B",  # Usar un modelo más grande
    tokenizer="EleutherAI/gpt-neo-1.3B",
    max_length=100,  # Limitar la longitud de la respuesta
    truncation=True,  # Activar truncamiento si excede el max_length
    no_repeat_ngram_size=2,  # Evitar repeticiones
    pad_token_id=50256  # Establecer el token de padding
)

# Generar la respuesta
def generar_respuesta(pregunta_usuario):
    # Ajustar el prompt para dar más contexto al modelo
    prompt = f"Eres un asistente conversacional amigable y servicial. Responde de manera clara y precisa. Por favor, responde de manera correcta y sin errores.\nUsuario: {pregunta_usuario}\nAsistente:"

    # Usar el pipeline para generar la respuesta
    respuesta = model_pipeline(prompt, max_length=100, truncation=True, num_return_sequences=1)

    # Mostrar la respuesta
    return respuesta[0]['generated_text'].strip()

# Ejemplo de uso
pregunta = "¿Cuál es la capital de Francia?"
respuesta = generar_respuesta(pregunta)
print(respuesta)
