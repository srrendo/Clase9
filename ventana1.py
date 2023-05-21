import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from cliente import Cliente
from ventana2 import Ventana2

class Ventana1(QMainWindow):

    # Hacer el metodo de construcción de la ventana
    def __init__(self, parent=None):
        super().__init__(parent)

        # Poner el título
        self.setWindowTitle("Formulario de registro")

        # Poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/balon.jpg'))

        # Establecer las propiedades de ancho y alto
        self.ancho = 1200
        self.alto = 900

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

        # Establecemos el fondo principal
        self.fondo = QLabel(self)

        # Definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/alianz.jpg')

        # Definimos la imagen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte el tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribución de los elementos con Layout horizontal
        self.horizontal = QHBoxLayout()
        # Le ponemos las margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        #---------- Layout izquierdo -----------

        # Creamos el layout del lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Les escribimos el texto
        self.letrero1.setText("Información del cliente")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andele Mono", 20))

        # Le ponemos el color de texto
        self.letrero1.setStyleSheet("color: #ffffff;")

        # Agregamos el letrero de la primera fila
        self.ladoIzquierdo.addRow(self.letrero1)

        # Hacemos el letrero
        self.letrero2 = QLabel()

        # Establecemos el ancho del label
        self.letrero2.setFixedWidth(340)

        # Le escribimos el texto
        self.letrero2.setText("Por favor ingrese la información del"
                              "\ncliente en el formulario de abajo. "
                              "\nLos campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra
        self.letrero2.setFont(QFont("Andale Mono", 10))

        # Le ponemos color de texto y margenes
        self.letrero2.setStyleSheet("color: #FFFFFF; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border.left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la linea siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar el nombre
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Nombre completo*", self.nombreCompleto)

        # Hacemos el campo para ingresar el usuario
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password
        self.contraseña = QLineEdit()
        self.contraseña.setFixedWidth(250)
        self.contraseña.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Contraseña*", self.contraseña)

        # Hacemos el campo para ingresar el password
        self.contraseña2 = QLineEdit()
        self.contraseña2.setFixedWidth(250)
        self.contraseña2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Verificación Contraseña*", self.contraseña2)

        # Hacemos el campo para ingresar el documento
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow("Correo electrónico*", self.correo)

        # Hacemos el botón para registrar los datos
        self.botonRegistrar = QPushButton("Registrar")

        # Establecemos el ancho del botón
        self.botonRegistrar.setFixedWidth(90)

        # Le ponemos los estilos
        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # Hacemos el botón para limpiar los datos
        self.botonLimpiar = QPushButton("Limpiar")

        # Establecemos el ancho del botón
        self.botonLimpiar.setFixedWidth(90)

        # Le ponemos los estilos
        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los dos botones al Layout ladoIzquierdo
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        # Agregamos el Layout ladoIzquierdo al layout horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)

        # ---------- Layout Derecho -----------

        # Creamos el layout del lado derecho
        self.ladoDerecho = QFormLayout()

        # Se asigna la margen solo a la izquierda de 100px
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # Hacemos el letrero3
        self.letrero3 = QLabel()

        # Le asignamos el texto
        self.letrero3.setText("Recuperar contraseña")

        # Le asignamos el tipo de letra
        self.letrero3.setFont(QFont("Andale Mono", 20))

        # Le ponemos el color de texto
        self.letrero3.setStyleSheet("color: #ffffff")

        # Agregamos el letrero en la primera fila
        self.ladoDerecho.addRow(self.letrero3)

        # Hacemos el letrero4
        self.letrero4 = QLabel()

        # Establecemos el ancho del label
        self.letrero4.setFixedWidth(400)

        # Le escribimos el texto
        self.letrero4.setText("Por favor ingrese la información para "
                              "\nrecuperar la contraseña."
                              "\nLos campos marcados"
                              "\ncon asteriscos, son obligatorios")

        # Le asignamos el tipo de letra:
        self.letrero4.setFont(QFont("Andale Mono", 10))

        # Le ponemos color al texto y margenes
        self.letrero4.setStyleSheet(("color: #FFFFFF; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border.left: none;"
                                    "border-right: none;"
                                    "border-top: none;"))

        # Agregamos el letrero 4 a la fila siguiente.
        self.ladoDerecho.addRow(self.letrero4)

        # ------ 1

        # Hacemos el letrero de la pregunta 1
        self.labelPregunta1 = QLabel("Primera pregunta de verificación*")

        # Agregamos el letrero en la fila siguiente.
        self.ladoDerecho.addRow(self.labelPregunta1)

        # Hacemos el campo para ingresar la pregunta 1
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.pregunta1)

        # Hacemos el letrero en la respuesta 1
        self.labelRespuesta1 = QLabel("Respuesta de verificación pregunta 1*")

        # Agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # Hacemos el campo para ingresar la respuesta 1
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.respuesta1)

        # ------ 2

        # Hacemos el letrero de la pregunta 2
        self.labelPregunta2 = QLabel("Segunda pregunta de verificación*")

        # Agregamos el letrero en la fila siguiente.
        self.ladoDerecho.addRow(self.labelPregunta2)

        # Hacemos el campo para ingresar la pregunta 2
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.pregunta2)

        # Hacemos el letrero en la respuesta 2
        self.labelRespuesta2 = QLabel("Respuesta de verificación pregunta 2*")

        # Agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # Hacemos el campo para ingresar la respuesta 2
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.respuesta2)

        # ------ 3

        # Hacemos el letrero de la pregunta 3
        self.labelPregunta3 = QLabel("Tercer pregunta de verificación*")

        # Agregamos el letrero en la fila siguiente.
        self.ladoDerecho.addRow(self.labelPregunta3)

        # Hacemos el campo para ingresar la pregunta 3
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.pregunta3)

        # Hacemos el letrero en la respuesta 3
        self.labelRespuesta3 = QLabel("Respuesta de verificación pregunta 3*")

        # Agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # Hacemos el campo para ingresar la respuesta 3
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.respuesta3)

        # Hacemos el botón para buscar las preguntas
        self.botonBuscar = QPushButton("Buscar")

        # Establecemos el ancho del botón
        self.botonBuscar.setFixedWidth(90)

        # Le ponemos los estilos al botón
        self.botonBuscar.setStyleSheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        # Hacemos que el botón buscar tenga su metodo
        self.botonBuscar.clicked.connect(self.accion_botonBuscar)


        # Hacemos el botón para recuperar la contraseña
        self.botonRecuperar = QPushButton("Recuperar PW")

        # Establecemos el ancho del botón
        self.botonRecuperar.setFixedWidth(120)

        # Le ponemos los estilos al botón
        self.botonRecuperar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;")

        # Hacemos que el botón recuperar tenga su metodo
        self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)


        # Agregamos los botones al Layout del lado derecho
        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)

        # ------- BOTÓN CONTINUAR -----------

        # Hacemos el botón para pasar a la siguiente ventana:
        self.botonContinuar = QPushButton("Continuar")

        # Establecemos el ancho del botón
        self.botonContinuar.setFixedWidth(90)

        # Le ponemos los estilos.
        self.botonContinuar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 10px"
                                          )

        # Hacemos que el botón continuar tenga su metodo:
        self.botonContinuar.clicked.connect(self.accion_botonContinuar)

        # Agregamos el botón continuar al layout del lado derecho
        self.ladoDerecho.addRow(self.botonContinuar)

        # Agregamos el layout ladoDerecho al layout horizontal
        self.horizontal.addLayout(self.ladoDerecho)

        # Agregamos el layout ladoDerecho al layout horizontal
        self.horizontal.addLayout(self.ladoDerecho)



        # --------- OJO IMPORTANTE PONER AL FINAL --------------

        # Indicamos que el Layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

        # ---------- CONSTRUCCIÓN DE LA VENTANA EMERGENTE ------------

        # Creamos la ventana de diálogo
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # Definimos el tamaño de la ventana
        self.ventanaDialogo.resize(300, 150)

        # Creamos el botón para aceptar
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # Establecemos el título de ventana
        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        # Configuración de la ventana para que sea modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # Creamos el layout vertical
        self.vertical = QVBoxLayout()

        # Creamos el label para los mensajes
        self.mensaje = QLabel("")

        # Le ponemos estilos al label mensaje
        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

        # Agregamos el label de mensajes
        self.vertical.addWidget(self.mensaje)

        # Agregamos las opciones de los botones
        self.vertical.addWidget(self.opciones)

        # Establecemos el layout para la ventana
        self.ventanaDialogo.setLayout(self.vertical)

    # Metodo del botón limpiar
    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.contraseña.setText('')
        self.contraseña2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    # Metodo del botón Registrar
    def accion_botonRegistrar(self):

        # Variable para controlar que se han ingresado los datos correctos
        self.datosCorrectos = True

        # Validamos que las contraseñas sean iguales
        if (
            self.contraseña.text() != self.contraseña2.text()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("Las contraseñas no son iguales")

            # Hacemos que la ventana de diálogo se vea
            self.ventanaDialogo.exec_()

        # Validamos que se ingresen todos los campos
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.contraseña.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):

            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("Debe diligenciar todos los datos")

            # Hacemos que la ventana de diálogo se vea
            self.ventanaDialogo.exec_()

        if self.datosCorrectos:

            # Abrimos el archivo en modo agregar escribiendo datos en binario
            self.file = open('datos/cliente.txt', 'ab')

            # Traer el texto de los Qline Edit() y los agrega concatenandolos
            # Para escribirlos en el archivo en formato binario UTF-8
            self.file.write(bytes(
                self.nombreCompleto.text() + ";"
                + self.usuario.text() + ";"
                + self.contraseña.text() + ";"
                + self.contraseña2.text() + ";"
                + self.documento.text() + ";"
                + self.correo.text() + ";"
                + self.pregunta1.text() + ";"
                + self.respuesta1.text() + ";"
                + self.pregunta2.text() + ";"
                + self.respuesta2.text() + ";"
                + self.pregunta3.text() + ";"
                + self.respuesta3.text() + "\n"
                , encoding= 'UTF-8'))
            # Cerramos el archivo
            self.file.close()

            # Abrimos en modo lectura en formato Byte
            self.file = open('datos/cliente.txt', 'rb')
            # Recorrer el archivo linea por linea
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '': # Para cuando encuentre una línea vacía
                    break
            self.file.close()

# Metodo botón buscar
    def accion_botonBuscar(self):

        # Variable para controlar que se han ingresado los datos correctos
        self.datosCorrectos = True

        # Establecemos el título de la ventana
        self.ventanaDialogo.setWindowTitle("Buscar preguntas de validación")

        # Validar que se haya ingresado el documento
        if (
            self.documento.text() == ''
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("Si va a buscar las preguntas"
                                 "para recuperar la contraseña"
                                 "\ndebe primero ingresar el documento")

            # Hacemos que la ventana de diálogo se vea
            self.ventanaDialogo.exec_()

        # Validar si el documento es numérico
        if (
            not self.documento.text().isnumeric()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("El documento debe ser numérico"
                                     "\nno ingrese letras ni "
                                     "caracteres especiales")

            # Hacemos que la ventana de diálogo se vea
            self.ventanaDialogo.exec_()

            # Limpiamos el campo del documento
            self.documento.setText('')


        # Si los datos estan correctos
        if (
            self.datosCorrectos
        ):
            # Abrimos el archivo en modo lectura
            self.file = open('datos/cliente.txt', 'rb')

            # Lista vacia para guardar todos los usuarios
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                # Obtenemos del string una lista con 11 datos separados por ;
                lista = linea.split(";")


                # Se para si no hay mas registros en el archivo
                if linea == '':
                   break
                # Creamos un objeto tipo cliente llamado u
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

                # Metemos el objeto en la lista de Usuarios
                usuarios.append(u)

            # Cerramos el archivo
            self.file.close()

            # En este punto ya tenemos la lista con todos los usuarios:

            # Variable para controlar que existe el documento
            existeDocumento = False

            # Buscamos en la lista usuario por usuario si existe el documento
            for u in usuarios:
                # Comparamos el documento ingresado
                # Si corresponde con el documento es el usuario correcto
                if u.documento == self.documento.text():
                    # Mostrar las preguntas en el formulario
                    self.pregunta1.setText(u.pregunta1)
                    self.pregunta2.setText(u.pregunta2)
                    self.pregunta3.setText(u.pregunta3)
                    # Indicamos que encotramos el documento
                    existeDocumento = True
                    # paramos el for
                    break

            # Si no existe un usuario con este documento
            if (
                not existeDocumento
            ):
                # Escribimos el texto explicativo
                self.mensaje.setText("No existe usuario con este documento:\n"
                                     +self.documento.text())

                # Hacemos que la ventana de diálogo se vea
                self.ventanaDialogo.exec_()

# Metodo del botón recuperar
    def accion_botonRecuperar(self):

        # Variable para controlar que se han ingresado los datos correctos
        self.datosCorrectos = True

        # Establecemos el titúlo de la ventana
        self.ventanaDialogo.setWindowTitle("Recuperar contraseña")

        # Validamos que se hayan buscado las preguntas
        if (
            self.pregunta1.text() == '' or
            self.pregunta2.text() == '' or
            self.pregunta3.text() == ''
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("Para recuperar la contraseña debe:"
                                 "\nBuscar las preguntas de verificación"
                                 "\n\nprimero ingrese su documento"
                                 "\n Luego precione el boton buscar")

            # Hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

        # Validamos si se buscaron las preguntas pero no se ingresaron las respuestas
        if (
            self.pregunta1.text() != '' and
            self.respuesta1.text() == '' and
            self.pregunta2.text() != '' and
            self.respuesta2.text() == '' and
            self.pregunta3.text() != '' and
            self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("Para recuperar la contraseña debe:"
                                 "\nIngresar las respuestas de cada pregunta")

            # Hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

        # Si los datos son correctos
        if(
            self.datosCorrectos
        ):
            # Abrimos el archivo en modo de lectura
            self.file = open('datos/cliente.txt', 'rb')

            # Lista vacia para guardar los usuarios
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # Obtenemos del string una lista con 11 datos separados por ;
                lista = linea.split(";")

                # Se para si ya no hay mas registros en el archivo
                if linea == '':
                    break
                # Creamos un objeto de tipo cliente llamado u
                U = Cliente(
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
                    lista[10]

                )
                # Metemos el objeto en la lista de usuarios.
                usuarios.append(U)

            # Cerramos el archivo
            self.file.close()

            # En este punto tenemos la lista usuarios con todos los usuarios:

            # Variable para controlar si existe el documento
            existeDocumento = False

            # Defininmos las variables para guardar las preguntas
            resp1 = ''
            resp2 = ''
            resp3 = ''
            passw = ''

            # Buscamos en la lista de usuario por usuario si existe la cedula
            for U in usuarios:
                # Comparamos el documento ingresado
                # si corresponde con el documento, es el usuario correcto
                if U.documento == self.documento.text():
                    # Indicamos que encontramos el documento
                    existeDocumento = True
                    # Guardamos las respuestas
                    resp1 = U.respuesta1
                    resp2 = U.respuesta2
                    resp3 = U.respuesta3
                    passw = U.contraseña
                    # Paramos el for
                    break

            # Verificamos que las respuestas son las correctas
            # Hacemos que las respuestas sean en letra minuscula:
            if(
                # usamos strip() para borrar espacios y saltos en las lineas
                self.respuesta1.text().lower().strip() == resp1.lower().strip() and
                self.respuesta2.text().lower().strip() == resp2.lower().strip() and
                self.respuesta3.text().lower().strip() == resp3.lower().strip()
            ):
                # Limpiamos los campos
                self.accion_botonLimpiar()

                # Escribimos el texto explicativo
                self.mensaje.setText("Contraseña:" + passw)

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()

            else:
                # Escribimos el texto explicativo
                self.mensaje.setText("Las respuestas no son correctas "
                                     "\npara las preguntas de validación")

                # Hacemos que  la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

    # Metodo del botón continuar
    def accion_botonContinuar(self):
        self.hide()
        self.ventana2 = Ventana2(self)
        self.ventana2.show()






if __name__ == '__main__':

    app= QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())