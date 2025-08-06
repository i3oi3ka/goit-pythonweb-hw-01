import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self, make, model):
        pass


class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):

    def create_car(self, make, model):
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):

    def create_car(self, make, model):
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{model} (EU Spec)")


us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

# Використання
vehicle1 = us_factory.create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
