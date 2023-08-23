class Computer:

    def config(self):
        print("i5","512")

    def configure(self):
        print("Ryzen5","512")


lenovo = Computer()
dell = Computer()

# print(type(lenovo))

Computer.config(lenovo)
Computer.configure(dell)

lenovo.config()
dell.configure()