from langchain.memory import ConversationBufferMemory # type: ignore
import logging

def get_memory(id, conn):
    # Recupera o crea la memoria del chatbot
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    list_messages = get_messages(id, conn)
    for message in list_messages:
        memory.save_context({"input": message[0]}, {"output": message[1]})
    return memory

def get_messages(id, conn):
    try:
        with conn.cursor() as cursor:
            query = "select pregunta, respuesta from memoria where id_mdm = %s order by fecha desc limit 5;"
            params = (id,)
            cursor.execute(query, params)
            list_messages = cursor.fetchall()
            logging.info('Recuperación de la memoria correcta')
            return list_messages
    except Exception as e:
        logging.info('Error al obtener los mensajes')
        raise Exception(f"Error al obtener los mensajes")

def save_memory(id, question, response, conn):
    try:
        with conn.cursor() as cursor:
            query = "INSERT INTO memoria (id_mdm, pregunta, respuesta) VALUES (%s, %s, %s);"
            params = (id, question, response)
            cursor.execute(query, params)
            conn.commit()
            logging.info('Memoria actualizada correctamente')
    except Exception as e:
        conn.rollback()
        logging.error('Error al actualizar la memoria')
        raise Exception(f"Error al actualizar la memoria")