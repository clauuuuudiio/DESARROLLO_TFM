exports.handler = async function(context, event, callback) {
  const twiml = new Twilio.twiml.MessagingResponse();

  // Obtenemos el número de teléfono y el mensaje del evento recibido
  const numero_telefono = event.From.replace('whatsapp:', ''); // Este es el número de quien escribe por WhatsApp
  const mensaje = event.Body;         // Este es el mensaje que la persona envía

  try {
    // Hacemos el POST con fetch
    const response = await fetch('https://chatbot-langchain.azurewebsites.net/api/http_trigger_chatbot', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        valor: numero_telefono,
        question: mensaje
      })
    });

    const respuesta = await response.text();

    // Respondemos al WhatsApp con el contenido que recibimos
    twiml.message(respuesta);

    callback(null, twiml);
  } catch (error) {
    // Si ocurre algún error, respondemos un mensaje de error
    twiml.message('Ocurrió un error al obtener la respuesta.');
    callback(null, twiml);
  }
};