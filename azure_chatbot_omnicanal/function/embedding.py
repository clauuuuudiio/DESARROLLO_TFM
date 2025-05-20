from langchain.schema import Document # type: ignore
from langchain_community.vectorstores import FAISS # type: ignore
from langchain_openai import AzureOpenAIEmbeddings # type: ignore
import os

def get_retriever():
    # Convertir JSON a Document LangChain
    faq_data = [
        {
        "pregunta": "¿Cuáles son los requisitos de admisión para nuevos estudiantes?",
        "respuesta": "Los requisitos varían según el programa, pero generalmente incluyen certificado de estudios anteriores, identificación oficial, formulario de solicitud completado y, en algunos casos, examen de admisión o entrevista."
        },
        {
        "pregunta": "¿Cuándo son las fechas de inscripción?",
        "respuesta": "Las inscripciones suelen abrirse dos veces al año: en enero y en julio. Las fechas específicas se publican en el calendario académico oficial disponible en nuestro sitio web."
        },
        {
        "pregunta": "¿La institución ofrece becas o ayudas económicas?",
        "respuesta": "Sí, contamos con programas de becas académicas, deportivas y de apoyo económico. Puedes consultar los requisitos y plazos en el Departamento de Bienestar Estudiantil."
        },
        {
        "pregunta": "¿Puedo realizar mi inscripción de manera virtual?",
        "respuesta": "Sí, todo el proceso de inscripción puede hacerse en línea a través de nuestro portal institucional."
        },
        {
        "pregunta": "¿Qué carreras o programas académicos ofrecen?",
        "respuesta": "Ofrecemos programas de nivel técnico, licenciatura, maestría y diplomados en diversas áreas como ciencias sociales, ingenierías, salud, y administración, entre otros."
        },
        {
        "pregunta": "¿Cuáles son los horarios de clase?",
        "respuesta": "Ofrecemos modalidades matutina, vespertina y en algunos casos, programas en línea o sabatinos para mayor flexibilidad."
        },
        {
        "pregunta": "¿Cómo puedo obtener mi constancia de estudios o certificado?",
        "respuesta": "Puedes solicitarlo en la Secretaría Académica de forma presencial o a través del sistema en línea, previo cumplimiento de los requisitos administrativos."
        },
        {
        "pregunta": "¿La institución tiene convenios con otras universidades?",
        "respuesta": "Sí, contamos con convenios nacionales e internacionales que permiten intercambios académicos y pasantías profesionales."
        },
        {
        "pregunta": "¿Qué servicios están disponibles para los estudiantes?",
        "respuesta": "Ofrecemos biblioteca, asesoría académica, orientación psicológica, actividades extracurriculares, bolsa de trabajo y centro de cómputo."
        },
        {
        "pregunta": "¿Dónde puedo presentar una queja o sugerencia?",
        "respuesta": "Contamos con un canal formal a través de la Oficina de Atención al Estudiante, disponible en línea o en nuestras instalaciones principales."
        }
    ]


    documents = [
        Document(page_content=f"Pregunta: {item['pregunta']}\nRespuesta: {item['respuesta']}")
        for item in faq_data
    ]
        
    embedding_model = AzureOpenAIEmbeddings(
        azure_deployment="text-embedding-3-small",  # <- Este es ahora azure_deployment
        openai_api_key=os.getenv("API_KEY"),
        azure_endpoint=os.getenv("API_BASE"),
        openai_api_version="2024-02-01",
        chunk_size=1000
    )
    
    vector_store = FAISS.from_documents(documents, embedding_model)

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    return retriever

"""    
    # Objeto Faiss de langchain
    index = vector_store.index
    index_bytes = FAISS.serialize_index(index)
"""