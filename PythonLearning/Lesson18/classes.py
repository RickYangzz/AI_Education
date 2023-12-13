class Vehicle:
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model
    
    def moves(self):
        print("Moves along...")
    
    def get_maker_model(self):
        print(f"\nIt's a {self.maker} {self.model}.")

my_car = Vehicle("Tesla", "Model 3")

my_car.get_maker_model()
my_car.moves()

class AirPlane(Vehicle):
    def __init__(self, maker, model, faa_id):
        super().__init__(maker, model)
        self.faa_id = faa_id
    
    def moves(self):
        print(f"Flies along...{self.faa_id}")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")
    
class GolfCart(Vehicle):
    pass

my_air_plane = AirPlane("Tesla", "Model 3", "N-889")
my_truck = Truck("Tesla", "Model 3")
my_golf_cart = GolfCart("Tesla", "Model 3")

my_air_plane.get_maker_model()
my_air_plane.moves()

my_truck.get_maker_model()
my_truck.moves()

my_golf_cart.get_maker_model()
my_golf_cart.moves()

print("\n\n\n")


for v in (my_car, my_air_plane, my_truck, my_golf_cart):
    v.moves()