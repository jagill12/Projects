class Car:
    def __init__(self, gas_pedal, amount):
        self.gas_pedal = gas_pedal
        self.amount = amount
       
    
    def move(self):
        distance = 0
        distance += self.amount * self.gas_pedal
        return distance
    
    def __str__(self):
        distance = self.move()
        return f"Car with gas pedal={self.gas_pedal}, amount={self.amount}" + "\n" \
                "The car moved a distance equal to " + str(distance)
    
def main():
    car1 = Car(2, 6)
    print(car1.__str__())
main()
