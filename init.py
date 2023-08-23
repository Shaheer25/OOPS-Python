class Computer:

    def __init__(self, processor,ram):
        self.processor=processor
        self.ram = ram

    def config(self):
        print(self.processor,self.ram)

lenovo= Computer("i5","512")
dell = Computer("Ryzen","1TB")

lenovo.config()
dell.config()