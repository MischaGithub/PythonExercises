#Declaring a class called transport
class Transport:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

#Instantiating an object from the Tranport class
    def work(self):
        if self.occupation == "Driver":
            print(self.name, "driver of cab")
        elif self.occupation == "Bus Driver":
            print(self.name, "drives bus")

    def ask(self):
        print(self.name, "How are you today/?")

andrew = Transport("Andrew", "Driver")
andrew.work()
andrew.ask()


