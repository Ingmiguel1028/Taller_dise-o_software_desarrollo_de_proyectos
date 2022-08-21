import string
import random


class VehicleInfo:
    
    def __init__(self, marca, electrico, precio_catalogo):
        self.marca = marca
        self.electrico = electrico
        self.precio_catalogo = precio_catalogo

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electrico:
            tax_percentage = 0.02
        return tax_percentage * self.precio_catalogo

    def print(self):
        print(f"marca: {self.marca}")
        print(f"impuesto a pagar: {self.compute_tax()}")

class Vehicle:

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class Registrovheiculo:

    def __init__(self):
        self.vehicle_info = { }
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)
        self.add_vehicle_info("Tesla Model Y", True, 75000)

    def add_vehicle_info(self, marca, electrico, precio_catalogo):
        self.vehicle_info[marca] = VehicleInfo( marca, electrico, precio_catalogo)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(id)
        return Vehicle(id, license_plate, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = Registrovheiculo()

        vehicle = registry.create_vehicle(brand)

        # print out the vehicle information
        vehicle.print()

app = Application()
app.register_vehicle("Tesla Model Y")
