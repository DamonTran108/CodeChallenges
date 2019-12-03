import unittest
from Car import Car



class TestCar(unittest.TestCase):
    def setUp(self):
      self.car = Car()


class TestInit(TestCar):
    def test_initial_speed(self):
        self.assertEqual(self.car.speed, 0 )

    def test_initial_odometer(self):
        self.assertEqual(self.car.odometer, 0)

    def test_initial_time(self):
        self.assertEqual(self.car.time, 0)

    def get_speed(self):
        return self.car.speed

class testAccelerate(TestCar):

    def test_accelerate(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 5)

    def test_multiple_accelerates(self):
        for _ in range(3):
            self.car.accelerate()
        self.assertEqual(self.car.get_speed(), 15)

class testBrake(TestCar):
    def test_brake_once(self):
        self.car.accelerate()
        self.car.brake()

        self.assertEqual(self.car.get_speed(), 0)

    def test_multiple_brakes(self):
        for _ in range(5):
            self.car.accelerate()
            print("{}".format(self.car.get_speed()))
            for i in range(2):
                print("{} speed Before breaking".format(self.car.get_speed()))
                self.car.brake()
                print("{} speed After breaking".format(self.car.get_speed()))
        self.assertEqual(self.car.speed, 0)

    def test_not_negative_speed(self):
        self.car.brake()
        self.assertEqual(self.car.speed, 0)

    def test_multiple_brakes_at_zero(self):
        for _ in range(10):
            self.car.brake()

        self.assertEqual(self.car.speed, 0)
