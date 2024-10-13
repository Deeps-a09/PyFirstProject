class Car:
    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model

    def start_engine(self):
        print("Start a Engine with the name " + self.name)
        print("Start a Engine with the make " + self.make)
        print("Start a Engine with the model " + self.model)

lambo = Car("Lambo", "V2","2024")
lambo.start_engine()
xuv = Car("XUV", "V5","2024")
xuv.start_engine()