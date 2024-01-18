
from abc import ABC, abstractmethod


class Airbags:
    def __init__(self, count):
        self.count = count

    def deploy(self):
        return f"{self.count} airbags deployed for safety."


class SeatBelt:
    def __init__(self, seat_belt_type):
        self.type = seat_belt_type

    def fasten(self):
        return f"{self.type} seat belt fastened."


class AlarmSystem:
    def __init__(self):
        self.active = False

    def activate_alarm(self):
        self.active = True
        return "Alarm system activated."

    def deactivate_alarm(self):
        self.active = False
        return "Alarm system deactivated."


class ABS:
    def __init__(self, ABS_type):
        self.type = ABS_type

    def engage(self):
        return f"ABS engaged: {self.type} system."


class SafetyFeatures:
    def __init__(self, count, seat_belt_type, ABS_type):
        self.airbags = Airbags(count)
        self.seat_belt = SeatBelt(seat_belt_type)
        self.alarm_system = AlarmSystem()
        self.abs = ABS(ABS_type)


class Engine:
    def __init__(self, engine_model):
        self.model = engine_model

    def start(self):
        return f"{self.model} engine started."


class Wheels:
    def __init__(self, wheel_size):
        self.size = wheel_size

    def rotate(self):
        return f"Wheels rotating with size {self.size}."


class SteeringSystem:
    def __init__(self, steering_type):
        self.type = steering_type

    def steer(self):
        return f"Steering with {self.type} system."


class EntertainmentSystem:
    def __init__(self, entertainment_brand):
        self.brand = entertainment_brand

    def play_music(self):
        return f"{self.brand} entertainment system playing music."


class SuspensionSystem:
    def __init__(self, suspension_type):
        self.type = suspension_type

    def absorb_shock(self):
        return f"{self.type} suspension system absorbing shock."


class ElectricalSystem:
    def __init__(self, voltage):
        self.voltage = voltage

    def power_up(self):
        return f"Electrical system powered up with {self.voltage} voltage."
    
    
class Car_parts:
    def __init__(self, engine_model, wheel_size, steering_type, entertainment_brand, suspension_type, voltage):
        self.steering_system = SteeringSystem(steering_type)
        self.entertainment_system = EntertainmentSystem(entertainment_brand)
        self.suspension_system = SuspensionSystem(suspension_type)
        self.electrical_system = ElectricalSystem(voltage)
        self.engine = Engine(engine_model)
        self.wheels = Wheels(wheel_size)


class Car(SafetyFeatures, Car_parts, ABC):  # Abstract Class
    def __init__(self, model, colour, count, seat_belt_type, ABS_type, engine_model, wheel_size, steering_type,
                 entertainment_brand, suspension_type, voltage):
        SafetyFeatures.__init__(self, count, seat_belt_type, ABS_type)
        Car_parts.__init__(self, engine_model, wheel_size, steering_type, entertainment_brand, suspension_type, voltage)
        self._model = model
        self.colour = colour
        self._speed = 0
        self._is_engine_on = False

    @abstractmethod
    def shift_gear(self):
        pass

    def start_engine(self):
        if not self._is_engine_on:
            print(f"The {self.colour} {self._model} car's engine just starts.")
            self._is_engine_on = True
        else:
            print(f"{self.colour} {self._model} car's engine is already running.")

    def stop_engine(self):
        if self._is_engine_on:
            self._is_engine_on = False
            print(f"The {self.colour} {self._model} car's engine just turn off.")
        else:
            print(f"The {self.colour} {self._model} car's engine is already off.")

    def accelerate(self, speed_increase):
        if self._is_engine_on:
            self._speed += speed_increase
            print(f"The car is accelerating. Current speed: {self._speed} mph.")
        else:
            print("Start the engine first.")

    def brake(self, speed_decrease):
        if self._is_engine_on:
            if self._speed >= speed_decrease:
                self._speed -= speed_decrease
                print(f"The car is braking. Current speed: {self._speed} mph.")
            else:
                self._speed = 0
                print("The car has come to a stop.")
        else:
            print("Start the engine first.")

    def honk(self):
        print("Beep! Beep.")

    def drive(self):
        print("General driving method.")


class Automatic(Car):
    def __init__(self, model, colour, count, seat_belt_type, ABS_type, engine_model, wheel_size, steering_type,
                 entertainment_brand, suspension_type, voltage):
        super().__init__(model, colour, count, seat_belt_type, ABS_type, engine_model, wheel_size, steering_type,
                         entertainment_brand, suspension_type, voltage)
        self._transmission = "Automatic"

    def shift_gear(self):
        print("Automatic transmission shifts gears automatically.")

    def drive(self):
        print(f"Driving {self.colour} {self._model} with {self._transmission} transmission.")


class Manual(Car):
    def __init__(self, model, colour, count, seat_belt_type, ABS_type, engine_model, wheel_size, steering_type,
                 entertainment_brand, suspension_type, voltage):
        super().__init__(model, colour, count, seat_belt_type, ABS_type, engine_model, wheel_size, steering_type,
                         entertainment_brand, suspension_type, voltage)
        self._transmission = "Manual"

    def shift_gear(self):
        print(f"Manual car shifted gears manually.")

    def drive(self):
        print(f"Driving {self.colour} {self._model} with {self._transmission} transmission.")


# Example usage
model = input("Enter the car model: ")
colour = input("Enter the car colour: ")
count = int(input("Enter no. of airbags: "))
seat_belt_type = input("Enter Seat Belt Type: ")
ABS_type = input("Enter ABS type: ")
transmission = input("Enter the transmission: ")
engine_model = input("Enter the engine model: ")
wheel_size = input("Enter the wheel size: ")
steering_type = input("Enter Steering type: ")
entertainment_brand = input("Enter entertainment brand name: ")
suspension_type = input("Enter suspension type: ")
voltage = input("Enter Voltage of Electrical System: ")
print("\n")


Auto_car = Automatic(model, colour, count, seat_belt_type, ABS_type, engine_model, wheel_size, steering_type,
                     entertainment_brand, suspension_type, voltage)
Manual_car = Manual(model, colour, count, seat_belt_type, ABS_type, engine_model, wheel_size, steering_type,
                    entertainment_brand, suspension_type, voltage)

Auto_car.start_engine()
Auto_car.accelerate(20)
Auto_car.shift_gear()
Auto_car.drive()
Auto_car.brake(5)
Auto_car.honk()
Auto_car.brake(20)
Auto_car.stop_engine()
print("\n")
Manual_car.start_engine()
Manual_car.accelerate(20)
Manual_car.shift_gear()
Manual_car.drive()
Manual_car.brake(5)
Manual_car.honk()
#Manual_car.engine.start()
Manual_car.brake(20)
Manual_car.stop_engine()
