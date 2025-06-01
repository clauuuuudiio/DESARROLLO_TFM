import { useState } from "react";
import "./App.css";
import MessageList from "./components/MessageList";
import MessageInput from "./components/MessageInput";
import axios from 'axios';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [correo, setCorreo] = useState("claudio.arribas@edu.uah.es");

  const handleSend = async () => {
    if (input.trim()) {
      setMessages([...messages, { sender: "user", text: input }]);
      setInput(""); // Limpiar input después de enviar

      try {
        const response = await axios.post('api/http_trigger_chatbot', 
          {
            'valor': correo,
            'question': input
          },
          {
            headers: {
              'Content-Type': 'application/json', // Header necesario
            },
          }
        );
  
        // La respuesta es un string, así que lo agregamos como mensaje del bot
        setMessages((prev) => [
          ...prev,
          { text: response.data, sender: "bot" }, // La respuesta es solo un string
        ]);
      } catch (error) {
        console.error('Error al enviar el mensaje:', error);
        setMessages((prev) => [
          ...prev,
          { text: "Error al enviar el mensaje. Intenta de nuevo.", sender: "bot" },
        ]);
      }
    };
  }

  return (
    <div className="d-flex flex-column align-items-center justify-content-center" style={{ width: "80%", margin: "0 auto" }}>
      <h1>Chatbot</h1>

      <MessageList messages={messages} />

      <MessageInput input={input} setInput={setInput} handleSend={handleSend} />
    </div>
  );
}

export default App;