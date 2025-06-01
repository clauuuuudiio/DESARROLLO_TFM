// MessageInput.js
import React from "react";

const MessageInput = ({ input, setInput, handleSend }) => {
  return (
    <div className="d-flex w-100 justify-content-center mt-3">
      <input
        type="text"
        className="form-control"
        placeholder="Escribe un mensaje..."
        aria-label="Username"
        aria-describedby="basic-addon1"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSend()}
      />
      <button type="button" className="btn btn-dark ms-3" onClick={handleSend}>
        Enviar
      </button>
    </div>
  );
};

export default MessageInput;
