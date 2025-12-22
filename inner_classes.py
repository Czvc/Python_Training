# Python Inner Classes
# Inner classes are classes defined inside another class to group related logic.

print("This is for a basic inner class with gaming desktop parts:")

class GamingDesktop:
    def __init__(self, name):
        self.name = name
        self.cpu = self.CPU()
        self.gpu = self.GPU()

    class CPU:
        def __init__(self):
            self.model = "Ryzen 7"

        def info(self):
            print("CPU:", self.model)

    class GPU:
        def __init__(self):
            self.model = "RTX 5090"

        def info(self):
            print("GPU:", self.model)

desktop = GamingDesktop("Beast PC")
print(desktop.name)
desktop.cpu.info()
desktop.gpu.info()

print("\nThis is for creating an inner class object from the outer object:")

class Case:
    def __init__(self, name):
        self.name = name

    class Fan:
        def __init__(self):
            self.count = 3

        def show(self):
            print("Number of fans:", self.count)

tower = Case("Mid Tower")
fans = tower.Fan()
fans.show()

print("\nThis is for inner class accessing outer instance (pass outer in):")

class Motherboard:
    def __init__(self, brand):
        self.brand = brand

    class RAM:
        def __init__(self, outer, size_gb):
            self.outer = outer
            self.size_gb = size_gb

        def show(self):
            print(f"Motherboard brand: {self.outer.brand}, RAM: {self.size_gb} GB")

mb = Motherboard("ASUS ROG")
ram_stick = mb.RAM(mb, 32)
ram_stick.show()

print("\nThis is for a practical inner class example (power supply inside PC):")

class GamingPC:
    def __init__(self, name):
        self.name = name
        self.psu = self.PowerSupply()

    class PowerSupply:
        def __init__(self):
            self.status = "Off"

        def turn_on(self):
            self.status = "On"
            print("Power supply turned On")

        def turn_off(self):
            self.status = "Off"
            print("Power supply turned Off")

    def boot(self):
        if self.psu.status == "On":
            print(f"{self.name} is booting up...")
        else:
            print("Turn on the power supply first!")

rig = GamingPC("Ultra Build")
rig.boot()
rig.psu.turn_on()
rig.boot()

print("\nThis is for multiple inner classes in one outer class:")

class FullDesktop:
    def __init__(self):
        self.cpu = self.CPU()
        self.gpu = self.GPU()
        self.storage = self.Storage()

    class CPU:
        def info(self):
            print("CPU: Intel i9")

    class GPU:
        def info(self):
            print("GPU: RTX 5090Ti")

    class Storage:
        def info(self):
            print("Storage: 2TB SSD")

pc = FullDesktop()
pc.cpu.info()
pc.gpu.info()
pc.storage.info()
