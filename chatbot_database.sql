-- Tabla: canal
CREATE TABLE canal (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla: cliente
CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    valor VARCHAR(100) NOT NULL,
    id_canal INT NOT NULL,
    FOREIGN KEY (id_canal) REFERENCES canal(id) ON DELETE CASCADE
);

-- Tabla: memoria
CREATE TABLE memoria (
    id SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    pregunta TEXT NOT NULL,
    respuesta TEXT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id) ON DELETE CASCADE
);
