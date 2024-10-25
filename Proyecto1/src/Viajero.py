# Funciones comunes para resolver el problema del viajero
class Ciudad:
    def __init__(self, nombre, tipo, demanda = 0, suministra = 0):
        self.nombre = nombre
        self.tipo = tipo  # 'recolectar' or 'entregar'
        self.demanda = demanda  # Only for delivery cities
        self.suministra = suministra  # Only for collection cities

class Viajero:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.capacidad_actual = 0
        self.ruta = []
        self.visitado = set()

    def visitar_ciudad(self, ciudad):
        if ciudad.nombre in self.visitado:
            return False
        if ciudad.tipo == 'recolectar':
            self.capacidad_actual += ciudad.suministra
        elif ciudad.tipo == 'entregar':
            if self.capacidad_actual >= ciudad.demanda:
                self.capacidad_actual -= ciudad.demanda
            else:
                return False
        self.ruta.append(ciudad.nombre)
        self.visitado.add(ciudad.nombre)
        return True
    
    def reset(self):
        self.capacidad_actual = 0
        self.ruta = []
        self.visitado = set()

def evaluar_ruta(viajero, ciudades):
    viajero.reset()
    entregas = 0
    for ciudad in ciudades:
        if viajero.visitar_ciudad(ciudad):
            if ciudad.tipo == 'entregar':
                entregas += ciudad.demanda
    return entregas

def impirmir(ciudades, entregas):
    print(f"Entrgas optimizadas: {entregas}")
    for ciudad in ciudades:
        print(ciudad.nombre)

def cambios_ruta(ciudades):
    rutas = []
    for i in range(len(ciudades)):
        for j in range(i + 1, len(ciudades)):
            # Swap cities to create a new route
            nuevas_ciudades = ciudades[:]
            nuevas_ciudades[i], nuevas_ciudades[j] = nuevas_ciudades[j], nuevas_ciudades[i]
            rutas.append(nuevas_ciudades)
    return rutas