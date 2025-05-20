from langchain.memory import ConversationBufferMemory
import logging

def get_memory(id, canal, conn):
    # Recupera o crea la memoria del chatbot
    memory = ConversationBufferMemory()
    
    list_messages = get_messages(id, canal, conn)
    
    for message in list_messages:
        memory.save_context({"input": message[0]}, {"output": message[1]})

    return memory

def get_messages(id, canal, conn):
    try:
        with conn.cursor() as cursor:
            query = "select pregunta, respuesta from memoria where id_cliente = (select id from cliente where valor = %s and id_canal = %s) order by fecha desc limit 5;"
            params = (id, canal)
            cursor.execute(query, params)
            list_messages = cursor.fetchall()
            if not list_messages:
                save_client(id, canal, conn)
            logging.info('Recuperación de la memoria correcta')
            return list_messages
    except Exception as e:
        logging.info('Error al obtener los mensajes')
        raise Exception(f"Error al obtener los mensajes")
        

def save_client(id, canal, conn):
    try:
        with conn.cursor() as cursor:
            query = "INSERT INTO CLIENTE (valor, id_canal) VALUES (%s, %s);"
            params = (id, canal)
            cursor.execute(query, params)
            conn.commit()
            logging.info('Cliente almacenado correctamente')
    except Exception as e:
        conn.rollback()
        logging.error('Error al guardar el cliente')
        raise Exception(f"Error al guardar el cliente")

def save_memory(id, canal, question, response, conn):
    try:
        with conn.cursor() as cursor:
            query = "INSERT INTO memoria (id_cliente, pregunta, respuesta) VALUES ((select id from cliente where valor =  %s and id_canal = %s), %s, %s);"
            params = (id, canal, question, response)
            cursor.execute(query, params)
            conn.commit()
            logging.info('Memoria actualizada correctamente')
    except Exception as e:
        conn.rollback()
        logging.error('Error al actualizar la memoria')
        raise Exception(f"Error al actualizar la memoria")