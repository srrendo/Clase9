import math
import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QWidget, QGridLayout, \
    QApplication, QButtonGroup, QPushButton
from PyQt5 import QtGui
from cliente import Cliente


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
        self.ancho = 1200
        self.alto = 800

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

        # Establecemos la distribución de los elementos en layout vertical
        self.vertical = QVBoxLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Les escribimos el texto
        self.letrero1.setText("Usuarios registrados")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andele Mono", 20))

        # Le ponemos el color de texto
        self.letrero1.setStyleSheet("color: #FFFFFF;")

        # Agregamos el letrero en la primera fila
        self.vertical.addWidget(self.letrero1)

        # Ponemos un espacio despues
        self.vertical.addStretch()

        # Creamos un scroll
        self.scrollArea = QScrollArea()

        # Le ponemos transparente el fondo del scroll
        self.scrollArea.setStyleSheet("background-color: transparent;")

        # Hacemos que el scroll se adapte a diferentes tamaños
        self.scrollArea.setWidgetResizable(True)

        # Creamos una ventana contenedora para la celda
        self.contenedora = QWidget()

        # Creamos un layout de grid para poner una cuadricula de elementos
        self.cuadricula = QGridLayout(self.contenedora)

        # Metemos la ventana contenedora en el scroll
        self.scrollArea.setWidget(self.contenedora)

        # Metemos el layout vertical en el scroll
        self.vertical.addWidget(self.scrollArea)

        # Abrimos el archivo en solo lectura
        self.file = open('datos/cliente.txt', 'rb')

        # Lista vacia para guardar los usaurios
        self.usuarios = []

        # Recorremos el archivo linea por linea
        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # Obtenemos del string una lista con 11 datos separados por ;
            lista = linea.split(";")

            # Se para si ya no hay mas registros en el archivo
            if linea == '':
                break

            # Creamos un objeto tipo cliente llamado U
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
            )

            # Metemos el objeto en la lista de usuarios
            self.usuarios.append(u)

        # Cerramos el archivo
        self.file.close()

        # En este punto tenemos la lista de usuarios con todos los usuarios

        # Obtenemos el número de usuarios registrados
        # Consultamos el tamaño de la lista de usuarios
        self.numeroUsuarios = len(self.usuarios)

        # Contador de elementos para controlar la lista usuarios
        self.contador = 0

        # Definimos la cantidad de elementos a mostrar por columna
        self.elementosPorColumna = 3

        # Calculamos el número de filas
        # Redondeamos al entero superior + 1, dividimos por elementosPorColumna
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) +1

        # Cotrolamos todos los botones por una variable
        self.botones = QButtonGroup()

        # Definimos que el cotrolador de los botones
        # debe agrupar a todos los botones internos
        self.botones.setExclusive(False)

        for fila in range (1, self.numeroFilas):
            for columna in range (1, self.elementosPorColumna + 1):

                # Validamos que se esten ingresando la cantidad de elementos correctos
                if self.contador < self.numeroUsuarios:

                    # En cada celda de la cuadricula va una ventana
                    self.ventanaAuxiliar = QWidget()

                    # Se determina su ancho y su alto
                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)

                    # Creamos un layout vertical para cada elemento de la cuadricula
                    self.verticalCuadricula = QVBoxLayout()

                    # Creamos un botón para cada usuario mostrando su cedula
                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    # Establecemos el ancho del boton
                    self.botonAccion.setFixedWidth(150)

                    # Le ponemos los estilos
                    self.botonAccion.setStyleSheet("background-color: #008B45;"
                                                   "color: #FFFFFF;"
                                                   "pandding: 10px;"
                                                   )

                    # Agregamos el botón al layout vertical para que se vea
                    self.verticalCuadricula.addWidget(self.botonAccion)

                    # Agregamos el botón al grupo, con su cédula como ID
                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))

                    # Agregamos un espacio en blanco
                    self.verticalCuadricula.addStretch()

                    # a la ventana le asignamos el layout vertical
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    # a la cuadricula le agregamos la ventana en la fila y columna actual
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    # Aumentamos el contador
                    self.contador += 1

        # Establecemos el metodo para que funcionen los botones
        self.botones.idClicked.connect(self.metodo_accionBotones)

        # --------------- Importante poner al final ---------------
        self.fondo.setLayout(self.vertical)

        # Metodo para controlar las acciones de los botones
    def metodo_accionBotones(self, cedulaUsuario):
        print(cedulaUsuario)



if __name__ == '__main__':

    app= QApplication(sys.argv)

    ventana2 = Ventana2()

    ventana2.show()

    sys.exit(app.exec_())
