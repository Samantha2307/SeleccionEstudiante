from datetime import datetime
from src.seleccionestudiante.modelo.Actividad import Actividad
from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.Equipo import Equipo
from src.seleccionestudiante.modelo.Estudiante import Estudiante
from src.seleccionestudiante.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
   #Crea la BD
   Base.metadata.create_all(engine)

   #Abre la sesión
   session = Session()

   # crear estudiantes
   estudiante1 = Estudiante(apellidoPaterno="Ramos", apellidoMaterno="Ortega", nombres="Juan Carlos",
                                 elegible=True)
   estudiante2 = Estudiante(apellidoPaterno="Solis", apellidoMaterno="Matos", nombres="Pedro",
                                 elegible=True)
   estudiante3 = Estudiante(apellidoPaterno="Paredes", apellidoMaterno="Torres", nombres="Luis Alberto",
                                 elegible=True)
   estudiante4 = Estudiante(apellidoPaterno="Garcia", apellidoMaterno="Mateo", nombres="Miguel Angel",
                                 elegible=True)

   session.add(estudiante1)
   session.add(estudiante2)
   session.add(estudiante3)
   session.add(estudiante4)
   session.commit()

   # crear asignatura
   asignatura1 = Asignatura(nombreAsignatura="Análisis y diseño de sistemas")
   asignatura2 = Asignatura(nombreAsignatura="Pruebas de software")
   asignatura3 = Asignatura(nombreAsignatura="Sistemas Operativos")
   session.add(asignatura1)
   session.add(asignatura2)
   session.add(asignatura3)
   session.commit()

   # crear equipo de trabajo
   equipo1 = Equipo(denominacionEquipo="Equipo01")
   equipo2 = Equipo(denominacionEquipo="Equipo02")
   session.add(equipo1)
   session.add(equipo2)
   session.commit()

   # crear actividad
   actividad1 = Actividad(denominacionActividad="Prueba unitaria",
                               fecha=datetime(2021, 9, 28, 00, 00, 00, 00000))
   actividad2 = Actividad(denominacionActividad="TDD", fecha=datetime(2021, 9, 25, 00, 00, 00, 00000))
   actividad3 = Actividad(denominacionActividad="BDD", fecha=datetime(2021, 10, 15, 00, 00, 00, 00000))
   session.add(actividad1)
   session.add(actividad2)
   session.add(actividad3)
   session.commit()

   # Relacionar Asignatura con estudiantes
   asignatura1.estudiantes = [estudiante1, estudiante4]
   asignatura2.estudiantes = [estudiante2, estudiante3]
   session.commit()

   # Relacionar equipo con estudiantes
   equipo1.estudiantes = [estudiante1, estudiante3]
   equipo2.estudiantes = [estudiante2, estudiante4]
   session.commit()

   # Relacionar Equipo de trabajo con actividad
   equipo1.actividades = [actividad1, actividad2]
   equipo2.actividades = [actividad3]
   session.commit()

   session.close()