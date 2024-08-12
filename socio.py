class Socio: # definimos la clase socio

	def __init__ (self, codigo, nombre, telefono, direccion, multas): #Constructor de clase

		#atributos de clase
		#self.nombre_atributo = parametro
		self.codigo = codigo
		self.nombre = nombre
		self.telefono = telefono
		self.direccion = direccion
		self.multas = multas

	def mostrar_socio(self):
		print("codigo: ",self.codigo)
		print("Nombre Completo: ",self.nombre)
		print("Telefono: ",self.telefono)
		print("direccion: ",self.direccion)
		print("Multas: ",self.multas)
