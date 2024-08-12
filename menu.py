from os import system
from socio import Socio
from videoclub import VideoClub
from pelicula import Pelicula

class Menu: #Creamos la clase
	def __init__(self): #Constructor de la clase -> inicializacion de la clase
		self.videoclub = VideoClub() #self -> permite el trabajo de los onjetos

	def adicionar_socio(self):
		system("cls") #Limpieza de consola
		print("-------------------------------")
		print("|       ADICIONAR SOCIO       |")
		print("-------------------------------")
		codigo = input("Digite su numero de documento: ")
		nombre = input("Digite su nombre completo con apellidos: ")
		telefono = input("Digite su numero de telefono celular: ")
		direccion = input("Digite su direccion de residencia: ")
		multas = ("")

		socio = Socio(codigo, nombre, telefono, direccion, multas) 
		# instancia de clase
		# socio -> objeto
		# socio -> clase


		if self.videoclub.adicionar_socio(socio):
			print("---------------------------------------------------")
			print("|  Info - El socio fue adiccionado correctamente  |")
			print("---------------------------------------------------")
			input()

		else:
			print("----------------------------------------------")
			print("|  Error - El socio ya existe en el sistema  |")
			print("----------------------------------------------")
			input()

	def listar_socios(self):
		system("cls")
		print("-------------------------------")
		print("|        LISTAR SOCIOS        |")
		print("-------------------------------")
		self.videoclub.listar_socios()
		input()

	def modificar_socio(self):
		system("cls")
		print("--------------------------")
		print("|     MODIFICAR SOCIO    |")
		print("--------------------------")
		codigo = input("Digite el codigo del socio que desea buscar: ")

		if self.videoclub.modificar_socio(codigo): 
			print("----------------------------------------------------")
			print("|  Info - Los datos del socio fueron modificados.  |")
			print("----------------------------------------------------")
			input()

		else:
			print("---------------------------------------------------------")
			print("|  Error - los datos del socio no se pueden modificar.  |")
			print("---------------------------------------------------------")
			input()	
	def eliminar_socio(self):
		system("cls")
		print("-------------------------------")
		print("|       ELIMINAR SOCIO        |")
		print("-------------------------------")
		codigo = input("Digite el codigo del socio que desea buscar: ")
		if self.videoclub.eliminar_socio(codigo):
			print("-----------------------------------")
			print("|  Info - El socio fue eliminado  |")
			print("-----------------------------------")
			input()
		else:
			print("-------------------------------------------")
			print("|  Error - El socio no se puede eliminar  |")
			print("-------------------------------------------")
			input()


##############################################################################
	def adicionar_pelicula(self):
		system("cls") #Limpieza de consola
		print("-------------------------------")
		print("|     ADICIONAR PELICULA      |")
		print("-------------------------------")
		codigo = input("Digite el codigo de la pelicula: ")
		titulo = input("Digite el nombre de la pelicula: ")
		genero = input("Digite el genero de la pelicula: ")
		nombre_socio = ("NA")
		fecha_inicio = ("NA")
		fecha_fin =  ("NA")
		pelicula = Pelicula(codigo, titulo, genero, nombre_socio, fecha_inicio, fecha_fin)

		if self.videoclub.adicionar_pelicula(pelicula):
			print("------------------------------------------------------")
			print("|  Info - La pelicula fue adiccionada correctamente  |")
			print("------------------------------------------------------")
			input()

		else:
			print("----------------------------------------------")
			print("|  Error - La pelicula no se pudo adicionar  |")
			print("----------------------------------------------")
			input()

	def listar_pelicula(self):
		system("cls")
		print("-------------------------------")
		print("|       LISTAR PELICULAS      |")
		print("-------------------------------")
		self.videoclub.listar_pelicula()
		input()

	def modificar_pelicula(self):
		system("cls")
		print("-------------------------------")
		print("|     MODIFICAR PELICULA      |")
		print("-------------------------------")
		codigo = input("Digite el codigo de la pelicula que desea buscar: ")

		if self.videoclub.modificar_pelicula(codigo): 
			print("---------------------------------------------------------")
			print("|  Info - Los datos de la pelicula fueron modificados.  |")
			print("---------------------------------------------------------")
			input()

		else:
			print("--------------------------------------------------")
			print("|  Error - los datos de la pelicula no se pueden modificar.  |")
			print("--------------------------------------------------")
			input()	


	def eliminar_pelicula(self):
		system("cls")
		print("-------------------------------")
		print("|       ELIMINAR PELICULA     |")
		print("-------------------------------")
		codigo = input("Digite el codigo de la pelicula que desa buscar: ")
		if self.videoclub.eliminar_pelicula(codigo):
			print("--------------------------------------")
			print("|  Info - La pelicula fue eliminada  |")
			print("--------------------------------------")
			input()
		else:
			print("----------------------------------------------")
			print("|  Error - La pelicula no se puede eliminar  |")
			print("----------------------------------------------")
			input()

	def alquilar_pelicula(self):
		system("cls")
		print("-------------------------------")
		print("|       ALQUILAR PELICULA     |")
		print("-------------------------------")
		codigo_pelicula = input("Digite el codigo de la pelicula que desa buscar: ")
		codigo_socio = input("Digite el codigo del socio que desa buscar: ")
		if self.videoclub.alquilar_pelicula(codigo_pelicula, codigo_socio) :
			print("--------------------------------------")
			print("|  Info - La pelicula fue alquilada  |")
			print("--------------------------------------")
			input()
		else:
			print("----------------------------------------------")
			print("|  Error - La pelicula no se puede alquilar  |")
			print("----------------------------------------------")
			input()

	def devolver_pelicula(self):
		system("cls")
		print("-------------------------------")
		print("|      DEVOLVER PELICULA      |")
		print("-------------------------------")
		codigo_pelicula = input("Digite el codigo de la pelicula que desa buscar: ")
		codigo_socio = input("Digite el codigo del socio que desa buscar: ")
		if self.videoclub.devolver_pelicula(codigo_pelicula, codigo_socio) :
			print("-------------------------------------")
			print("|  Info - La pelicula fue devuelta  |")
			print("-------------------------------------")
			input()
		else:
			print("----------------------------------------------")
			print("|  Error - La pelicula no se puede devolver  |")
			print("----------------------------------------------")
			input()

	def listar_pelicula_alquiladas(self):
		system("cls")
		print("-----------------------------------------")
		print("|       LISTAR PELICULAS ALQUILADAS     |")
		print("-----------------------------------------")
		self.videoclub.listar_pelicula_alquiladas()
		input()

	def listar_pelicula_disponible(self):
		system("cls")
		print("-----------------------------------------")
		print("|      LISTAR PELICULAS DISPONIBLES     |")
		print("-----------------------------------------")
		self.videoclub.listar_pelicula_disponible()
		input()		
	
	def listar_prestamos_retrasados(self):
		system("cls")
		print("-----------------------------------------")
		print("|       LISTAR PRESTAMOS RETRASADOS     |")
		print("-----------------------------------------")
		self.videoclub.listar_prestamos_retrasados()
		input()
	def agregar_multa(self):
		system("cls")
		print("---------------------------")
		print("|       AGREGAR MULTA     |")
		print("---------------------------")
		codigo = input("Digite el codigo del socio que desa buscar: ")
		self.videoclub.agregar_multa(codigo)
		input()

	def listar_socios_con_multa(self):
		system("cls")
		print("------------------------------------")
		print("|       LISTAR SOCIOS MULTADOS     |")
		print("------------------------------------")
		self.videoclub.listar_socios_con_multa()
		input()

	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("|------------------------------------------------------|")
			print("|------------------------------------------------------|")
			print("|                      VIDEOCLUB                       |")
			print("|------------------------------------------------------|")
			print("|------------------------------------------------------|")
			print("|                    MENU PRINCIPAL                    |")
			print("|------------------------------------------------------|")
			print("| 1. Adicionar Socio                                   |")
			print("| 2. Listar Socios                                     |")
			print("| 3. Modificar Socio                                   |")
			print("| 4. Eliminar Socio                                    |")
			print("|                                                      |")
			print("| 5. Adicionar Pelicula                                |")
			print("| 6. Listar Peliculas                                  |")
			print("| 7. Modificar Pelicula                                |")
			print("| 8. Eliminar Pelicula                                 |")
			print("|                                                      |")
			print("| 9. Alquilar Pelicula                                 |")
			print("| 10. Devolver Pelicula                                |")
			print("| 11. Listar peliculas alquiladas                      |")
			print("| 12. Listar pelicula disponibles                      |")
			print("| 13. Listar devolucion de prestamos retrasados        |")
			print("| 14. Adicionar multa a un socio                       |")
			print("|                                                      |")
			print("| 15. Salir                                            |")
			print("|------------------------------------------------------|")

			try:
				op = int(input("Digite su opcion: "))

				if op == 1:
					self.adicionar_socio() #Se invoca el metodo

				elif op == 2:
					self.listar_socios()

				elif op == 3:
					self.modificar_socio()

				elif op == 4:
					self.eliminar_socio()

				elif op == 5:
					self.adicionar_pelicula()

				elif op == 6:
					self.listar_pelicula()

				elif op == 7:
					self.modificar_pelicula()

				elif op == 8:
					self.eliminar_pelicula()

				elif op == 9:
					self.alquilar_pelicula()

				elif op == 10:
					self.devolver_pelicula()

				elif op == 11:
					self.listar_pelicula_alquiladas()

				elif op == 12:
					self.listar_pelicula_disponible()

				elif op == 13:
					self.listar_prestamos_retrasados()

				elif op ==14:
					self.agregar_multa()

				elif op == 15:
					print("---------------------------")
					print("| HAS SALIDO DEL SISTEMA  |")
					print("---------------------------")
					break
				else:
					print("------------------------------")
					print("|  Error - opcion no valida  |")
					print("------------------------------")
					input()


			except ValueError:
				print("--------------------------------------------")
				print("|  Error - El dato ingresado no es entero  |")
				print("--------------------------------------------")
				input()

if __name__ == '__main__':
	#Instancia clase menu
	menu = Menu()
	menu.mostrar_menu_principal()