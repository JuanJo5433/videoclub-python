from socio import Socio
from pelicula import Pelicula
from datetime import datetime
#definimos la calse
class VideoClub:
	fecha_actual  = datetime.now()
	formato = fecha_actual.strftime("%d/%m/%Y")
	#constructor de clase
	def __init__(self):
		#atributo tipo lista

		self.socios = []
		self.peliculas = []

	def buscar_socio(self, codigo):
		for i in range(len(self.socios)): 
			if self.socios[i].codigo == codigo:
				return i
		return -1

	def adicionar_socio(self, socio):
		if self.buscar_socio(socio.codigo) == -1:
			self.socios.append(socio)
			return True
		return False

	def listar_socios(self):
		for i in self.socios:
			print("-------------------------------")
			i.mostrar_socio()

	def modificar_socio(self, codigo):
		pos_socio = self.buscar_socio(codigo)
		if pos_socio != -1:
			if self.socios[pos_socio].codigo  == codigo:
				print("-------------------------------")
				print("|   OPCIONES PARA MODIFICAR   |")
				print("-------------------------------")

				try:
					print("1 = Modificar nombre completo")
					print("2 = Modificar Telefono")
					print("3 = Modificar la dirreccion")
					print("-------------------------------")

					op = int(input("Digite la opcion a modificar: "))

					if op == 1:
						nombre = input("Digite el nuevo nombre del socio: ")
						self.socios[pos_socio].nombre = nombre
						return True
					elif op == 2:
						telefono = input("Digite el nuevo telefono del socio: ")
						self.socios[pos_socio].telefono = telefono
						return True
					elif op == 3:
						direccion = input("Digite la nueva dirreccion del socio: ")
						self.socios[pos_socio].direccion = direccion
						return True
					else:
						return False
				except ValueError:
					print("-----------------------------------")
					print("| Error - El dato debe ser entero |")
					print("-----------------------------------")
					input()
			else:
				return False
		else:
			return False

	def eliminar_socio(self, codigo):
		pos_socio = self.buscar_socio(codigo)
		if pos_socio != -1:
			del(self.socios[pos_socio])
			return True
		return False

	def adicionar_pelicula(self, pelicula):
		if self.buscar_pelicula(pelicula.codigo) == -1:
			self.peliculas.append(pelicula)
			return True
		return False

	def buscar_pelicula(self, codigo):
		for i in range(len(self.peliculas)): 
			if self.peliculas[i].codigo == codigo:
				return i
		return -1	

	def listar_pelicula(self):
		for pelicula in self.peliculas:
			print("------------------------")
			pelicula.mostrar_pelicula()

	def modificar_pelicula(self, codigo):
		pos_pelicula = self.buscar_pelicula(codigo)
		if pos_pelicula != -1:
			if self.peliculas[pos_pelicula].codigo == codigo:
				print("-------------------------------")
				print("|   OPCIONES PARA MODIFICAR   |")
				print("-------------------------------")

				try:
					print("1 = Modificar titulo de la pelicula")
					print("2 = Modificar genero de la pelicula")
					print("-------------------------------")

					op = int(input("Digite la opcion a modificar: "))

					if op == 1:
						titulo = input("Digite el nuevo titulo de la pelicula: ")
						self.peliculas[pos_pelicula].titulo = titulo
						return True

					elif op == 2:
						genero = input("Digite el nuevo genero de la pelicula: ")
						self.peliculas[pos_pelicula].genero = genero
						return True	

					else:
						return False

				except ValueError:
					print("-----------------------------------")
					print("| Error - El dato debe ser entero |")
					print("-----------------------------------")
					input()
			else:
				return False
		else:
			return False

	def eliminar_pelicula(self, codigo):
		pos_pelicula = self.buscar_pelicula(codigo)
		if pos_pelicula != -1:
			del(self.peliculas[pos_pelicula])
			return True
		return False

	def alquilar_pelicula(self, codigo_pelicula, codigo_socio):
		pos_pelicula = self.buscar_pelicula(codigo_pelicula)
		pos_socio = self.buscar_socio(codigo_socio)

		if pos_pelicula != -1 and pos_socio != -1:
			if self.peliculas[pos_pelicula].codigo == codigo_pelicula:
				if self.socios[pos_socio].codigo == codigo_socio:
					self.peliculas[pos_pelicula].alquilada = True
					self.peliculas[pos_pelicula].nombre_socio = self.socios[pos_socio].nombre
					self.peliculas[pos_pelicula].fecha_inicio = self.formato
					fecha_ingresada = input("Digite la fecha final del prestamo en formato dd/mm/aaaa: ")
					fecha = datetime.strptime(fecha_ingresada, "%d/%m/%Y")
					self.peliculas[pos_pelicula].fecha_fin = fecha.strftime("%d/%m/%Y")


					return True
				else:
					return False	
			else:
				return False
		else:
			return False

	def devolver_pelicula(self, codigo_pelicula, codigo_socio):
		pos_pelicula = self.buscar_pelicula(codigo_pelicula)
		pos_socio = self.buscar_socio(codigo_socio)

		if pos_pelicula != -1 and pos_socio != -1:
			if self.peliculas[pos_pelicula].codigo == codigo_pelicula:
				if self.socios[pos_socio].codigo == codigo_socio:
					self.peliculas[pos_pelicula].alquilada = False
					self.peliculas[pos_pelicula].nombre_socio = ("NA")
					self.peliculas[pos_pelicula].fecha_inicio = ("NA")
					self.peliculas[pos_pelicula].fecha_fin = ("NA")
					return True
				else:
					return False	
			else:
				return False
		else:
			return False

	def listar_pelicula_alquiladas(self):
		for pelicula in self.peliculas:
			print("------------------------")
			pelicula.mostrar_pelicula_alquiladas()

	def listar_pelicula_disponible(self):
		for pelicula in self.peliculas:
			print("------------------------")
			pelicula.mostrar_pelicula_disponible

	def listar_prestamos_retrasados(self):
		for pelicula in self.peliculas:
			print("------------------------")
			pelicula.mostrar_prestamos_retrasados()
			
	def agregar_multa(self, codigo):
		pos_socio = self.buscar_socio(codigo)
		if pos_socio != 1:
			if self.socios[pos_socio].codigo == codigo:
				print("-------------")
				print("|   MULTAS  |")
				print("-------------")

				try:
					print("1 = Multa por retraso de devolucion")
					print("2 = Multa por daños fisicos a la pelicula")
					print("3 = Multa por perdida de la pelicula")
					print("-------------------------------")

					op = int(input("Digite la multa que desa añadir: "))

					if op ==1:
						self.socios[pos_socio].multas += ("RETRASO POR DEVOLUCION. ")
						return True
					elif op ==2:
						self.socios[pos_socio].multas += ("DAÑO FISICOS A LA PELICULA. ")
						return True
					elif op ==3:
						self.socios[pos_socio].multas += ("PERDIDA DE LA PELICULA. ")

						return True
					else:
						return False

				except ValueError:
					print("-----------------------------------")
					print("| Error - El dato debe ser entero |")
					print("-----------------------------------")
					input()
			else:
				return False
		else:
			return False






