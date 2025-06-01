// MessageList.js
import React from "react";

const MessageList = ({ messages }) => {
  return (
    <div className="rounded p-3 mb-3 overflow-auto" style={{ height: "550px", width: "100%" }}>
      {messages.map((msg, i) => (
        <div key={i} className={`mb-2 text-${msg.sender === "user" ? "end" : "start"}`}>
            <span
            className="d-inline-block p-2 rounded text-dark"
            style={{ backgroundColor: msg.sender === "user" ? "#e0e0e0" : "", color: msg.sender === "user" ? "#000" : "#fff" }}
            >
                {msg.text}
            </span>
        </div>
      ))}
    </div>
  );
};

export default MessageList;
