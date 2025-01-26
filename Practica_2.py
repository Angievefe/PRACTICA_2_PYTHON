#Realice un programa que pueda gestionar tickets de buses
# las clases a usar seran buses  , conductores
# 1. Un menu iteractivo con las siguiente opciones: agregar bus , agregar ruta a bus 
# registrar horario a bus, agregar conductor , agregar horario a conductor() y asignar bus a conductor(*)
# * consideremos que el horario de los conductores solo es a nivel de horas mas no dias ni fechas
# **validar que no haya conductores en ese horario ya asignados

class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []

    def agregar_horario(self, inicio, fin):
        for h_inicio, h_fin in self.horarios:
            if not (fin <= h_inicio or inicio >= h_fin):
                return False
        self.horarios.append((inicio, fin))
        return True


class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horarios = []
        self.conductor = None

    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def agregar_horario(self, inicio, fin):
        self.horarios.append((inicio, fin))

    def asignar_conductor(self, conductor):
        for b_inicio, b_fin in self.horarios:
            for c_inicio, c_fin in conductor.horarios:
                if not (b_fin <= c_inicio or b_inicio >= c_fin):
                    return False
        self.conductor = conductor
        return True


class Admin:
    def __init__(self):
        self.buses = {}
        self.conductores = {}

    def agregar_bus(self, placa):
        self.buses[placa] = Bus(placa)

    def agregar_conductor(self, nombre):
        self.conductores[nombre] = Conductor(nombre)

    def menu(self):
        while True:
            print("\n1. Agregar Bus\n2. Agregar Ruta\n3. Registrar Horario a Bus\n4. Agregar Conductor\n5. Agregar Horario a Conductor\n6. Asignar Conductor\n7. Salir")
            opcion = input("Seleccione: ")

            if opcion == "1":
                self.agregar_bus(input("Placa: "))
            elif opcion == "2":
                bus = self.buses.get(input("Placa: "))
                if bus: bus.asignar_ruta(input("Ruta: "))
            elif opcion == "3":
                bus = self.buses.get(input("Placa: "))
                if bus: bus.agregar_horario(*map(int, input("Horario (inicio fin): ").split()))
            elif opcion == "4":
                self.agregar_conductor(input("Nombre: "))
            elif opcion == "5":
                conductor = self.conductores.get(input("Nombre: "))
                if conductor: conductor.agregar_horario(*map(int, input("Horario (inicio fin): ").split()))
            elif opcion == "6":
                bus = self.buses.get(input("Placa: "))
                conductor = self.conductores.get(input("Nombre: "))
                if bus and conductor: bus.asignar_conductor(conductor)
            elif opcion == "7":
                break

# Ejecutar
Admin().menu()


