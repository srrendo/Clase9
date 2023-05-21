import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication
from PyQt5 import QtGui


class Ventana2(QMainWindow):

    # Hacer el metodo de la construcción para la ventana
    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)

        # Creamos un atributo que guarde la ventana anterior
        self.ventanaAnterior = anterior

        # Poner el titúlo
        self.setWindowTitle("Usuarios registrados")

        # Poner el icono
        self.setWindowIcon(QtGui.QIcon("imagenes/balon.jpg"))

        # Establecemos las propiedades de ancho y alto
        self.ancho = 900
        self.alto = 600

        # Establecer el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # Hacer que la ventana se vea en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el ancho y el alto de la ventana
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecer el fondo principal
        self.fondo = QLabel(self)

        # Definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/Santiago.jpg')

        # Definimos la imagen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte el tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribucion de los elementos en layout vertical
        self.vertical = QVBoxLayout()

if __name__ == '__main__':

    app= QApplication(sys.argv)

    ventana2 = Ventana2()

    ventana2.show()

    sys.exit(app.exec_())
