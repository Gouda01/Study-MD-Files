class Car :
    
    def __init__(self,color):
        self.color = color

    def increase_speed (self):
        print('increase speed +10k')

class Brand(Car):
    def __init__(self,brand,color):
        super().__init__(color)
        self.brand = brand

        print(self.brand)
        print(self.color)

    def increase_speed (self):
        super().increase_speed()
        print('increase speed +20k')
        
            
        

b = Brand('BMW','Red')
b.increase_speed()
