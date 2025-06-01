from langchain.tools import Tool # type: ignore
from functools import partial
from function.chains import get_qa_chain
import re
import logging

def consultar_expediente(id: str, db_conn, exp) -> str:
    logging.info('AQUIiiiiiiiiiiiiiiiiiiii')
    logging.info('1')
    logging.info(id)
    logging.info('2')
    logging.info(exp)
    if(re.fullmatch(r'[0-9]+', id) or exp):
        if(exp):
            expediente = exp
        else:
            expediente = id
        # Buscar en base de datos 
        with db_conn.cursor() as cursor:
            query = "select * from alumno where id = %s limit 1;"
            params = (expediente)
            cursor.execute(query, params)
            row = cursor.fetchone()
            if row is None:
                return f"No es ha obtenido información sobre el expediente indicado"
            nombre = row[1]
            apellidos = row[2]
            nota = row[3]
            curso = row[4]
            estudios = row[8]
            return f"El expediente {expediente} corresponde con el alumno {nombre} {apellidos} el cual esta en el curso {curso}º de {estudios} y tiene una nota media de {nota}."

    else:  
        return f"Debes indicarme un id para poder acceder a la información"

def info_class(nombre_clase: str, db_conn) -> str:
    logging.info('999999999999999999999999999')
    nombre_min = nombre_clase.lower().strip("'")
    logging.info(nombre_min)
    logging.info('BBBBBBBBBBBBBBBBBB')
    logging.info(re.fullmatch(r'[a-záéíóúñü ]+', nombre_min))
    logging.info('CCCCCCCCCCCCCCCCCCC')
    logging.info(repr(nombre_min))
    
    if(re.fullmatch(r'[a-záéíóúñü ]+', nombre_min)):
        logging.info('777777777777777777777777777')
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

def get_tools(conn, exp):
    qa_chain = get_qa_chain(conn)
    
    consultar_expediente_conn = partial(consultar_expediente, db_conn=conn, exp=exp)
    info_class_conn = partial(info_class, db_conn=conn)
    
    tools = [
        Tool( # Consulta el expediente de un alumno
            name="ConsultarExpediente",
            func=consultar_expediente_conn,
            description=(
                "Usa esta herramienta para consultar información del expediente académico de un alumno. "
                "Permite obtener datos como la nota media, el curso actual (1º, 2º, etc), y los estudios que está realizando "
                "(por ejemplo, Informática, Lengua, etc). "
                "Requiere como entrada el identificador único del estudiante (ID del expediente)."
            )        
        ),
        Tool( # Consulta la información de una clase
            name="ConsultarClase",
            func=info_class_conn,
            description=(
                "Usa esto para consultar información relacionada con una clase o asignatura, "
                "incluyendo profesor, horario y materia. "
                "Proporciona el nombre exacto de la asignatura como entrada, por ejemplo: "
                "'Bases de Datos', 'Matemáticas Avanzadas', etc."
            )        
        ),
        Tool.from_function(
            func=lambda q: qa_chain({'query': q}),
            name="FAQsUniversidad",
            description="Usa esta herramienta cuando el usuario haga preguntas generales o frecuentes relacionadas con procesos administrativos o académicos de la universidad, como: inscripción, matrícula, horarios, servicios estudiantiles, requisitos, o fechas clave.",
        ),
        Tool( # Consulta el expediente de un alumno
            name="PreguntaIncorrecta",
            func=pregunta_incorrecta,
            description="Se usa cuando ninguna otra opción es válida."
        ),
    ]
    
    return tools