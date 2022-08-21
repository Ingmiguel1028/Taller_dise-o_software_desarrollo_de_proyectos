from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass


class LightBulb(Switchable):
    def encender(self):
        print("LightBulb: turned on...")

    def apagar(self):
        print("LightBulb: turned off...")


class Fan(Switchable):
    def encender(self):
        print("Ventilador: encendido...")

    def apagar(self):
        print("Ventilador: apagado...")


class ElectricPowerSwitch:

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.apagar()
            self.on = False
        else:
            self.client.encender()
            self.on = True


l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()
