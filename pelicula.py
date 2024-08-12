from datetime import datetime

class Pelicula:
	
	def __init__(self, codigo, titulo, genero, nombre_socio, fecha_inicio, fecha_fin):

		self.codigo = codigo
		self.titulo = titulo
		self.genero = genero
		self.alquilada = False
		self.nombre_socio =	 nombre_socio
		self.fecha_inicio = fecha_inicio
		self.fecha_fin = fecha_fin
		


	def mostrar_pelicula(self):
		print("Codigo: ", self.codigo)
		print("Titulo: ", self.titulo)
		print("Genero: ", self.genero)
		print("Alquilada: ", self.alquilada)
		print("Nombre del socio del alquiler: ", self.nombre_socio)
		print("La fecha del inicio del prestamo es: ", self.fecha_inicio)
		print("La fecha del fin del prestamo es: ", self.fecha_fin)

	def mostrar_pelicula_alquiladas(self):
		if self.alquilada == True:
			print("Codigo: ", self.codigo)
			print("Titulo: ", self.titulo)
			print("Genero: ", self.genero)
			print("Alquilada: ", self.alquilada)
			print("Nombre del socio del alquiler: ", self.nombre_socio)
			print("La fecha del inicio del prestamo es: ", self.fecha_inicio)
			print("La fecha del fin del prestamo es: ", self.fecha_fin)

	def mostrar_pelicula_disponible(self):
		if self.alquilada == False:
			print("Codigo: ", self.codigo)
			print("Titulo: ", self.titulo)
			print("Genero: ", self.genero)
			print("Alquilada: ", self.alquilada)
			print("Nombre del socio del alquiler: ", self.nombre_socio)
			print("La fecha del inicio del prestamo es: ", self.fecha_inicio)
			print("La fecha del fin del prestamo es: ", self.fecha_fin)

	def mostrar_prestamos_retrasados(self):
		fecha_actual  = datetime.now()
		formato = fecha_actual.strftime("%d/%m/%Y")
		if self.fecha_fin < formato:
			print("Codigo: ", self.codigo)
			print("Titulo: ", self.titulo)
			print("Genero: ", self.genero)
			print("Alquilada: ", self.alquilada)
			print("Nombre del socio del alquiler: ", self.nombre_socio)
			print("La fecha del inicio del prestamo es: ", self.fecha_inicio)
			print("La fecha del fin del prestamo es: ", self.fecha_fin)
			print("La devolucion del prestamo se encuentra fuera del limite de tiempo de entrega")