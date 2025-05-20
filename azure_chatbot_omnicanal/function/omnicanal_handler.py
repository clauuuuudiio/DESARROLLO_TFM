from function.chains import get_recover_data_chain
from function.user_handler import save_correo, save_telefono, get_alumno_by_expediente, get_alumno_by_valor
import ast

def verify_data(id_mdm, valor, pregunta, conn):
    recover_data_chain = get_recover_data_chain()
    response_data = recover_data_chain.invoke({'input': pregunta}).content
    try:
        data = ast.literal_eval(response_data)
    except Exception as e:
        return None
    if data["correo"]:
        # Unir el alumno con el correo indicado con el id_mdm
        save_correo(id_mdm, data["correo"], conn)
    if data["telefono"]:
        # Unir el telefono indicado con el id_mdm
        save_telefono(id_mdm, data["telefono"], conn)
    if data["expediente"]:
        # Buscar el expediente y unir con el id_mdm los valores del alumno
        alumno = get_alumno_by_expediente(data["expediente"], conn) # Buscar alumno por expediente
        print("AAAAAAAAAAA", alumno)
        if not (alumno is None):
            if not (alumno[0] is None):
                save_correo(id_mdm, alumno[0], conn) # Correo institucional
            if not (alumno[1] is None):
                save_correo(id_mdm, alumno[1], conn) # Correo personal
            if not (alumno[2] is None):
                save_telefono(id_mdm, alumno[2], conn) # Telefono
    if data["propio"]:
        # Buscar el expediente del valor de origen de la petición y unir con el id_mdm los valores alumnos
        list_alumnos = get_alumno_by_valor(valor, conn)
        if len(list_alumnos) == 1:
            alumno = list_alumnos[0]
            if not (alumno[0] is None):
                save_correo(id_mdm, alumno[0], conn) # Correo institucional
            if not (alumno[1] is None):
                save_correo(id_mdm, alumno[1], conn) # Correo personal
            if not (alumno[2] is None):
                save_telefono(id_mdm, alumno[2], conn) # Telefono
            return alumno[3]
    return None