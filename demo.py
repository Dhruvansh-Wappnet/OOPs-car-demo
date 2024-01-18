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
        self.airbags_enabled = False
        self.abs_enabled = False
        
    # def __init__(self):
    #     self.airbags_enabled = False
    #     self.abs_enabled = False

    # @staticmethod
    # def get_airbags_count():
    #     airbags_count = input("Enter the number of airbags: ")
    #     return int(airbags_count)

    # @staticmethod
    # def get_abs_type():
    #     abs_type = input("Enter the type of ABS system: ")
    #     return abs_type
    
    # @staticmethod
    # def get_seat_belt_type():
    #     seat_belt_type = input("Enter the type of ABS system: ")
    #     return seat_belt_type
    
    def enable_airbags(self):
        print("Airbags enabled for enhanced safety.")
        self.airbags_enabled = True

    def enable_abs(self):
        print("Anti-lock Braking System (ABS) enabled for improved braking safety.")
        self.abs_enabled = True
        

# class Engine:
#     def engine_starts(self):
#         print("Engine Starts.")

#     def engine_stops(self):
#         print("Engine Stops.")
        
        
# class Wheels:
#     def rotate(self):
#         print("Wheel is rotating.")

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
    def __init__(self,engine_model,wheel_size,steering_type,entertainment_brand,suspension_type, voltage):
        self.steering_system = SteeringSystem(steering_type)
        self.entertainment_system = EntertainmentSystem(entertainment_brand)
        self.suspension_system = SuspensionSystem(suspension_type)
        self.electrical_system = ElectricalSystem(voltage)
        self.engine = Engine(engine_model)
        self.wheels = Wheels(wheel_size)
        
    # @staticmethod
    # def get_engine_input():
    #     model = input("Enter engine model: ")
    #     return Engine(model)

    # @staticmethod
    # def get_wheels_input():
    #     size = input("Enter wheel size: ")
    #     return Wheels(size)

    # @staticmethod
    # def get_steering_system_input():
    #     type = input("Enter steering system type: ")
    #     return SteeringSystem(type)
    
    # @staticmethod
    # def get_entertainment_system_input():
    #     brand = input("Enter entertainment system brand: ")
    #     return EntertainmentSystem(brand)

    # @staticmethod
    # def get_suspension_system_input():
    #     type = input("Enter suspension system type: ")
    #     return SuspensionSystem(type)

    # @staticmethod
    # def get_electrical_system_input():
    #     voltage = input("Enter electrical system voltage: ")
    #     return ElectricalSystem(voltage)
    
        
    # def engine(self):
    #     return self.engine

    # def wheels(self):
    #     return self.wheels
              
        
class Car(SafetyFeatures, Car_parts):     #Abstract Class
    def __init__(self,model,colour,count, seat_belt_type, ABS_type, engine_model,wheel_size,steering_type,entertainment_brand,suspension_type, voltage):
        SafetyFeatures.__init__(count, seat_belt_type, ABS_type)
        Car_parts.__init__(engine_model,wheel_size,steering_type,entertainment_brand,suspension_type, voltage)
        self.__model = model     #Private 
        self.colour = colour
        self._speed = 0
        self._is_engine_on = False
        # self._safety_features = SafetyFeatures()
        # self._car_parts  = Car_parts()
        
    #Encapsulation---------In child class
    def get_model(self):
        return self.__model
    
    def set_model(self,model):
        self.__model = model    
    
    def start_engine(self):
        if not self._is_engine_on:
            print(f"The {self.colour} {self.__model} car's engine just starts.")
            self._is_engine_on = True
            # self._car_parts.engine.engine_starts()
        else:
            print(f"{self.colour} {self.__model} car's engine is already running.")
            
    def stop_engine(self):
        if self._is_engine_on == True:
            self._is_engine_on = False
            print(f"The {self.colour} {self.__model} car's engine just turn off.")
            # self._car_parts.engine.engine_stops()
        else:
            print(f"The {self.colour} {self.__model} car's engine is already off.")
            
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
        print("Beep! Beep!")
        
    @abstractmethod
    def shift_gear(self):
        pass
    
    def drive(self):
        print("General driving method.")
        #self._car_parts.wheels.rotate()
        
    def enable_airbags(self):
        self._safety_features.enable_airbags()

    def enable_abs(self):
        self._safety_features.enable_abs()
        
    # def display_safety_features(self):
        """Display all safety features of the car."""
        print(f"Safety Features for {self.colour} {self.__model} car:")
        print(f"- Airbags: {self.airbags.count} airbags")
        print(f"- Seat Belt: {self.seat_belt.type} seat belt")
        print(f"- Alarm System: {self.alarm_system.active}")
        print(f"- ABS: {self.abs.type} system")


class Automatic(Car):
    def __init__(self, model, colour, count, seat_belt_type, ABS_type, engine_model, wheel_size, steering_type,
                 entertainment_brand, suspension_type, voltage, transmission):
        # Call the parent class constructors in the correct order
        super().__init__(model, colour, count, seat_belt_type, ABS_type, engine_model, wheel_size, steering_type,
                         entertainment_brand, suspension_type, voltage)
        self._transmission = transmission

    def shift_gear(self, new_gear):
        print("Automatic transmission shifts gears automatically.")

    def drive(self):
        # Override the drive method
        print(f"Driving {self.colour} {self.get_model()} with {self._transmission} transmission.")


class Manual(Car):
    def __init__(self, model, colour, count, seat_belt_type, ABS_type, engine_model, wheel_size, steering_type,
                 entertainment_brand, suspension_type, voltage, transmission):
        # Call the parent class constructors in the correct order
        super().__init__(model, colour, count, seat_belt_type, ABS_type, engine_model, wheel_size, steering_type,
                         entertainment_brand, suspension_type, voltage)
        self._transmission = transmission
        self._current_gear = 0

    def shift_gear(self, new_gear):
        self._current_gear = new_gear
        print(f"Manual car shifted to gear {self._current_gear}.")

    def drive(self):
        # Override the drive method
        print(f"Driving {self.colour} {self.get_model()} with {self._transmission} transmission.")



    
# class Automatic(Car):
#     def __init__(self,model,colour,count, seat_belt_type, ABS_type, engine_model,wheel_size,steering_type,entertainment_brand,suspension_type, voltage,transmission):
#         super().__init__(model,colour,count, seat_belt_type, ABS_type, engine_model,wheel_size,steering_type,entertainment_brand,suspension_type, voltage)
#         self._transmission = transmission

#     def shift_gear(self, new_gear):
#         print("Automatic transmission shifts gears automatically.")

#     def drive(self):                #Override
#         print(f"Driving {self.colour} {self.get_model()} with {self._transmission} transmission.")


# class Manual(Car):
#     def __init__(self,model,colour,count, seat_belt_type, ABS_type, engine_model,wheel_size,steering_type,entertainment_brand,suspension_type, voltage,transmission):
#         super().__init__(model,colour,count, seat_belt_type, ABS_type, engine_model,wheel_size,steering_type,entertainment_brand,suspension_type, voltage)
#         self._transmission = transmission
#         self._current_gear = 0

#     def shift_gear(self, new_gear):
#         self._current_gear = new_gear
#         print(f"Manual car shifted to gear {self._current_gear}.")

#     def drive(self):              #Override
#         print(f"Driving {self.colour} {self.get_model()} with {self._transmission} transmission.")
        
        
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


        
def test_drive(car):
    car.start_engine()
    car.accelerate(20)
    car.shift_gear(3)
    car.drive()
    car.brake(5)
    car.honk()
    car.brake(20)
    # car.enable_airbags()
    # car.display_safety_features()
    car.stop_engine()
    print("\n")
    
    
Auto_car = Automatic(model,colour,count, seat_belt_type, ABS_type, engine_model,wheel_size,steering_type,entertainment_brand,suspension_type, voltage, transmission)
Manual_car = Manual(model,colour,count, seat_belt_type, ABS_type, engine_model,wheel_size,steering_type,entertainment_brand,suspension_type, voltage, transmission)


test_drive(Auto_car)
test_drive(Manual_car)
        
