import random

class Personaje:
    def __init__(self, nombre):
        # Constructor: se asigna nombre y se inicializa en nivel 1 y experiencia 0
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
        self.estado = (self.nivel, self.experiencia)
    
    @property
    def estado(self):
        # Getter: muestra el estado actual del personaje
        print(f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}")
        return self.nivel, self.experiencia

    @estado.setter
    def estado(self, experiencia_extra):
        # Setter: ajusta experiencia y nivel en base a experiencia ganada o perdida
        nueva_exp = self.experiencia + experiencia_extra

        # Subir de nivel cada vez que la experiencia supera 100 puntos
        while nueva_exp >= 100:
            nueva_exp -= 100
            self.nivel += 1
        
        # Bajar de nivel si la experiencia queda bajo 0
        while nueva_exp < 0:
            if self.nivel > 1:
                self.nivel -= 1
                nueva_exp += 100
            else:
                nueva_exp = 0
                break
        
        self.experiencia = nueva_exp
    
     # Sobrecarga operador menor que: se compara por nivel
    def __lt__(self, other):
        return self.nivel < other.nivel

    # Sobrecarga operador mayor que: se compara por nivel
    def __gt__(self, other):
        return self.nivel > other.nivel

    # Sobrecarga operador igual que: útil para verificar igualdad de niveles
    def __eq__(self, other):
        return self.nivel == other.nivel

    def probabilidad_ganar(self, otro):
        # Retorna la probabilidad de ganar contra otro personaje
        if self > otro:
            return 0.66
        elif self < otro:
            return 0.33
        else:
            return 0.5

    @staticmethod
    def mostrar_dialogo(probabilidad):
        # Diálogo de enfrentamiento que explica las consecuencias del ataque
        print(f"\nCon tu nivel actual, tienes {probabilidad * 100:.1f}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        print("¿Qué deseas hacer?\n1. Atacar\n2. Huir")
        opcion = input("Ingresa tu opción: ")
        return opcion