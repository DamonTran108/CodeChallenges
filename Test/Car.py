class Car:
    def __init__(self, speed = 0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def get_speed(self):
        return self.speed

    def brake(self):
        self.speed -= 5
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):

        if self.time !=0:
            return  self.odometer / self.time
    #else:
           # pass
if __name__ == '__main__':

    my_car = Car()
    print("i'm a  car!")
    while True:
        action = input("What Should I do? [A]ccelerate. [[B]rake," 
        "show [O]dometer, or show average [S]peed?").upper()

        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue

        if action == "A":
            my_car.accelerate()
        elif action == "B":
            my_car.brake()
        elif action == "O":
            print("my car has driven {} Km".format(my_car.odometer))
        elif action == "S":
            print("The car is driving at {} Km".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()