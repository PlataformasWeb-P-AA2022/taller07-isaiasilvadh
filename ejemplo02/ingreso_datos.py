from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


dataclub = open("data/datos_clubs.txt","r")
dataJugadores = open('data/datos_jugadores.txt', 'r')

for a in dataclub:
    fila = a.rstrip().split(';')
    c = Club(nombre=fila[0],deporte=fila[1], fundacion=fila[2])
    session.add(c)