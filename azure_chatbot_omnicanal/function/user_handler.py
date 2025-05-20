import re
import logging

def get_id_mdm(valor, conn):
    try:
        with conn.cursor() as cursor:
            patron_telefono = r'^(\+)?[0-9]+$'
            # Comprobar si el valor es un telefono
            if re.fullmatch(patron_telefono, valor):
                query = "select mdm.id from mdm as mdm inner join telefono_usuario as tu on tu.id_mdm = mdm.id where tu.telefono = %s limit 1;"
            else:
                query = "select mdm.id from mdm as mdm inner join correo_usuario as cu on cu.id_mdm = mdm.id where cu.correo = %s limit 1;"
            params = (valor,)
            cursor.execute(query, params)
            user = cursor.fetchone()
            if user is None:
                return save_user(valor, conn)
            return user[0]
    except Exception as e:
        conn.rollback()
        logging.error('Error al obtener el id_mdm')
        raise Exception(f"Error al obtener el id_mdm")
    
    
def save_user(valor, conn):
    try:
        with conn.cursor() as cursor:
            query = "INSERT INTO mdm DEFAULT VALUES RETURNING id;"
            cursor.execute(query)
            id_mdm = cursor.fetchone()[0]
            patron_telefono = r'^(\+)?[0-9]+$'
            # Comprobar si el valor es un telefono
            if re.fullmatch(patron_telefono, valor):
                save_telefono(id_mdm, valor, conn)
            else:
                save_correo(id_mdm, valor, conn)
            return id_mdm
    except Exception as e:
        conn.rollback()
        logging.error('Error al guardar el usuario')
        raise Exception(f"Error al guardar el usuario")

def save_correo(id_mdm, valor, conn):
    try:
        with conn.cursor() as cursor:
            # Comprobar si existe
            query = "select 1 from mdm as mdm inner join correo_usuario as cu on cu.id_mdm = mdm.id where cu.correo = %s and mdm.id = %s limit 1;"
            params = (valor, id_mdm)
            cursor.execute(query, params)
            correo_user = cursor.fetchone()
            if correo_user is None:
                query = "INSERT INTO correo_usuario (correo, id_mdm) VALUES (%s, %s);"
                params = (valor, id_mdm)
                cursor.execute(query, params)
    except Exception as e:
        conn.rollback()
        logging.error('Error al guardar el correo')
        raise Exception(f"Error al guardar el correo")

def save_telefono(id_mdm, valor, conn):
    try:
        with conn.cursor() as cursor:
            # Comprobar si existe
            query = "select 1 from mdm as mdm inner join telefono_usuario as tu on tu.id_mdm = mdm.id where tu.telefono = %s and mdm.id = %s limit 1;"
            params = (valor, id_mdm)
            cursor.execute(query, params)
            telefono_user = cursor.fetchone()
            if telefono_user is None:
                query = "INSERT INTO telefono_usuario (telefono, id_mdm) VALUES (%s, %s);"
                params = (valor, id_mdm)
                cursor.execute(query, params)
    except Exception as e:
        conn.rollback()
        logging.error('Error al guardar el telefono')
        raise Exception(f"Error al guardar el telefono")
    
def get_alumno_by_expediente(exp, conn):
    try:
        with conn.cursor() as cursor:
            query = "select correo_institucional, correo_personal, numero_telefono from alumno where id = %s limit 1;"
            params = (exp,)
            cursor.execute(query, params)
            return cursor.fetchone()
    except Exception as e:
        conn.rollback()
        logging.error('Error al buscar el alumno por expediente')
        raise Exception(f"Error al buscar el alumno por expediente")

def get_alumno_by_valor(valor, conn):
    try:
        with conn.cursor() as cursor:
            patron_telefono = r'^(\+)?[0-9]+$'
            # Comprobar si el valor es un telefono
            if re.fullmatch(patron_telefono, valor):
                query = "select correo_institucional, correo_personal, numero_telefono, id from alumno where numero_telefono = %s limit 1;"
                params = (valor)
            else:
                query = "select correo_institucional, correo_personal, numero_telefono, id from alumno where correo_institucional = %s or correo_personal = %s;"
                params = (valor, valor)
            cursor.execute(query, params)
            return cursor.fetchall()
    except Exception as e:
        conn.rollback()
        logging.error('Error al buscar el alumno por expediente')
        raise Exception(f"Error al buscar el alumno por expediente")
