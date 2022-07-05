import sys
import os
import unittest

from PyQt6.QtWidgets import QApplication,QDialog
from PyQt6 import uic
from tkinter import messagebox
from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.logica.GestionAsignatura import GestionAsignatura
from src.seleccionestudiante.modelo.Estudiante import Estudiante
from src.seleccionestudiante.modelo.Equipo import Equipo
from src.seleccionestudiante.modelo.Actividad import Actividad
from src.seleccionestudiante.modelo.declarative_base import engine, Base, Session

class Dialogo(QDialog):

    def __init__(self):
        ruta = os.path.dirname ( os.path.abspath ( __file__ ) ) + r"\..\vista\EditarAsignatura.ui"
        QDialog.__init__(self)
        uic.loadUi(ruta,self)

        Base.metadata.create_all(engine)

        self.gestionAsignatura = GestionAsignatura()

        self.lblID.setText('1')
        self.btnGuardar.clicked.connect(self.guardar_edicion)
        self.btnCancelar.clicked.connect(self.exit_app)

    def guardar_edicion( self ):

        nombre = self.ltNombre.text()
        resultado = self.gestionAsignatura.editar_asignatura(idAsignatura=1, nombreAsignatura=nombre)

        print (resultado)

        if resultado == True:
            print("Funcionó")
            op = messagebox.askokcancel("Confirmación", "Se editó la asignatura con éxito")
            if op == True:
                print ("Aceptó")
                quit(0)

        else:
            op2 = messagebox.askretrycancel("Error", "Ocurrió un error, vuelva a intentarlo")
            if op2 == False:
                print("No funcionó")
                quit(0)

    def exit_app( self ):
        resultado = messagebox.askquestion("Salir","¿Está seguro que desea salir?")
        if resultado == "yes":
            quit(0)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialogo=Dialogo()
    dialogo.show()
    app.exec()