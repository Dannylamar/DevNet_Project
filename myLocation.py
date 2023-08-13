class Location:
    def __init__(self, name, country):
        self.name=name
        self.country=country

    def myLocation(self):
        print("Hi, my name is " + self.name + " and i live in " + self.country+ ".")

loc1 = Location("Thomas", "Portugal")
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
loc1.myLocation()
loc2.myLocation()
loc3.myLocation()

your_loc = Location("Daniel", "Ghana")
your_loc.myLocation()
