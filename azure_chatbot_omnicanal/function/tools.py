from langchain.tools import Tool # type: ignore
from functools import partial
from function.chains import get_qa_chain
import re

def consultar_expediente(id: str, db_conn) -> str:
    if(re.fullmatch(r'[0-9]+', id)):
        # Buscar en base de datos 
        with db_conn.cursor() as cursor:
            query = "select * from alumno where id = %s limit 1;"
            params = (id)
            cursor.execute(query, params)
            row = cursor.fetchone()
            if row is None:
                return f"No es ha obtenido información sobre el expediente indicado"
            print("LA FILA DEVUELTA POR LA BBDD ES: ", row)
            nombre = row[1]
            apellidos = row[2]
            nota = row[3]
            curso = row[4]
            return f"El expediente {id} corresponde con el alumno {nombre} {apellidos} el cual esta en el curso {curso}º y tiene una nota media de {nota}."

    else:  
        return f"Debes indicarme un id para poder saber tu nota media."

def info_class(nombre_clase: str, db_conn) -> str:
    clases = ['matemáticas']
    nombre_min = nombre_clase.lower()
    if nombre_min in clases:
        with db_conn.cursor() as cursor:
            query = """
            SELECT *
            FROM clase
            INNER JOIN profesor p
            ON p.id = id_profesor
            WHERE LOWER(asignatura) LIKE %s
            limit 1;
            """            
            params = (f"%{nombre_min}%",)
            cursor.execute(query, params)
            row = cursor.fetchone()
            if(row):
                asignatura = row[1]
                dia = row[4]
                horario = row[5]
                nombre = row[8]
                apellidos = row[9]
                especialidad = row[10]
                return f"La clase de {asignatura} se imparte el dia {dia} a la hora {horario} por el profesor {nombre} {apellidos} especialista en {especialidad}"
            return f"No se encontro información de la clase especificada"
    else:
        return f"Debes especificar la asignatura de la clase que quieres obtener información"
    
def pregunta_incorrecta():
    return "Lo siento, no puedo ayudarte con esa consulta."

def get_tools(conn):
    qa_chain = get_qa_chain()
    
    consultar_expediente_conn = partial(consultar_expediente, db_conn=conn)
    info_class_conn = partial(info_class, db_conn=conn)
    
    tools = [
        Tool( # Consulta el expediente de un alumno
            name="ConsultarExpediente",
            func=consultar_expediente_conn,
            description="Usa esto para consultar el expediente o la nota media académico de un estudiante. Usa el identificador del estudiante como entrada."
        ),
        Tool( # Consulta la información de una clase
            name="ConsultarClase",
            func=info_class_conn,
            description="Usa esto para consultar la información relacionada con una clase (profesor, horario y/o materia). Usa el nombre de la asignatura como entrada."
        ),
        Tool.from_function( # Responde una FAQs
            func=lambda q: qa_chain({'query': q}),
            name="FAQsUniversidad",
            description="Usa esto para responder preguntas frecuentes sobre dudas comunes en procesos administrativos, académicos o servicios de la universidad "
        ),
        Tool( # Consulta el expediente de un alumno
            name="PreguntaIncorrecta",
            func=pregunta_incorrecta,
            description="Se usa cuando ninguna otra opción es válida."
        ),
    ]
    
    return tools