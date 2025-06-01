from langchain.prompts import PromptTemplate # type: ignore
from langchain.chains import RetrievalQA # type: ignore
from function.model_llm import get_llm
from function.embedding import get_retriever

def get_validation_chain():
    llm = get_llm()
    
    template = """
Tu tarea es determinar si una pregunta está relacionada con un entorno universitario.

Considera como temas válidos: asignaturas, profesores, horarios, calificaciones, matrícula, becas, campus, procesos administrativos, clases, carreras, programas académicos o vida estudiantil.

Responde solo con "1" si la pregunta está relacionada con temas universitarios. En cualquier otro caso, responde solo con "0".

Ahora evalúa esta pregunta:

"{input}"
    """

    prompt = PromptTemplate(
        input_variables=["input"],
        template=template
    )

    chain = prompt | llm
    
    return chain

def get_recover_data_chain():
    llm = get_llm()
    
    template = """
Extrae la información relevante de la siguiente frase y devuélvela en formato JSON con los siguientes campos:

- nombre: Nombre propio si se menciona, sino None.
- apellidos: Apellido(s) si se menciona, sino None.
- correo: Dirección de correo electrónico si aparece, sino None.
- telefono: Número de teléfono si aparece, sino None.
- expediente: ID numérico de un expediente académico si aparece, sino None.
- propio: 1 o 0.
    - 1: si la persona pregunta por sí misma y NO proporciona un correo, un telefono o un expediente.
    - 0: si proporciona algún valor anterior como expediente, correo o teléfono.

Ejemplo de formato de salida:
{{
  "nombre": None,
  "apellidos": None,
  "correo": None,
  "telefono": None,
  "expediente": None,
  "propio": 0
}}

Frase a evaluar:
"{input}"
"""

    prompt = PromptTemplate(
        input_variables=["input"],
        template=template
    )
    
    chain = prompt | llm
    
    return chain

def get_qa_chain(conn):
    llm = get_llm()
    retriever = get_retriever(conn)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    
    return qa_chain