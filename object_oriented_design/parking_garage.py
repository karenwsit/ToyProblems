#7.4 Parking Lot: Design a parking lot using object-oriented principles

#Questions:
#How to best structure all these different classes. Should they be subclasses? or stay separate classes?
#How to best pass variables from other classes when they are instance variables
#Reference to someone else's implementation in Python: https://gist.github.com/anonymous/a6247da9d061b1eab899

class ParkingLot(ParkingSpace):

    """All parking lots have a name, a maximum capacity and charge an hourly rate"""

    def __init__(self, id, street_address, owner_id ):
        self.id = id
        self.street_address = street_address
        self.owner_id = owner_id   # Foreign Key

    def find_compact_avail(self):
        # SELECT * FROM PARKING SPACE WHERE TYPE=COMPACT AND OCCUPIED=FALSE

    def find_parking_lot_avail(self):
        # SELF.CAPACITY - SELECT COUNT(*) FROM TICKET WHERE PAID= FALSE

    def calculate_daily_rev(self):
        # SELECT SUM(TOTAL_COST) FROM TICKET WHERE PAID= TRUE AND EXITTIME= TODAY(DATE)

class Owners(object):

    """Owners own Parking Lots"""

    def __init__(self, id, name, address, email, phone):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone


class ParkingSpace(object):

    """Parking spaces make up a parking lot with occupied and space type attributes"""

    def __init__(self, id, car_type, space_type, level):
        self.id = id
        self.parking_lot_id = id  # Foreign Key
        self.car_id = car_id  # if IS NULL then the parking space is empty, also a private variable
        self.car_type = car_type

class Ticket(ParkingLot):

    """Tickets are issued by a parking lot with entrance and exit times, paid, and total cost attributes"""

    def __init__(self, id, entrance_time, exit_time, parking_space_id, total_cost=None):
        self.entrance_time = entrance_time  # timestamp value
        self.exit_time = exit_time          # timestamp value
        self.parking_space_id = parking_space_id   # Foreign Key
        self.total_cost = total_cost

    def calculate_total_cost(self):
        parked_time = self.exit_time - self.entrance_time
        if parked_time == 0:
            parked_time += 1
        elif type(parked_time) != integer:
            #round up to the nearest hour if parked_time is not an integer
        parked_time * self.hourly_rate

######################################################
#Other Things to Consider for Parking Lot OOP Problem
######################################################

#Inputs for ParkingLot object

"""
from weight_sensor_vendor import AbstractInputFromSensors
from abc import ABCMeta, abstractmethod # <- standard library

class AbstractInputFromSensors(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def sensor_on(self, spot_number):
        "the sensor in spot_number detected a weight"
    @abstractmethod
    def sensor_off(self, spot_number):
        "the sensor in spot_number detected no weight"


AbstractInputFromSensors.register(InputFromSensors) # -> can be elsewhere

isinstance(InputFromSensors(), AbstractInputFromSensors) # -> True
"""

class InputFromSensors(object):
    def __init__(self):
        pass
        
    def sensor_on(self, spot_number):
        pass
        
    def sensor_off(self, spot_number):
        pass

class InputFromPayment(object):
    def __init__(self):
        pass
        
    def paid_for_spot(self, spot_number, amount):
        pass

class RecommendationInterface(object):
    def recommend_available_space(self):
        pass

"""
from payment_vendor import register_payment_input
from weight_sensor_vendor import register_sensor_notifications
from recommendation_screen_vendor import register_recommender
#Good Way
parking_lot = ParkingLot()

register_payment_input(InputFromPayment(parking_lot))
register_sensor_notifications(InputFromSensors(parking_lot))
register_recommender(RecommendationInterface(parking_lot))

#Bad Way: room for conflict of different and/or private attributes that might have the same name/id/num
#register_payment_input(parking_lot)
#register_sensor_notifications(parking_lot)
#register_recommender(parking_lot)
#class ParkingLot(AbstractInputFromSensors, AbstractInputFromPayment, AbstractRecommendationInterface):

# Output for ParkingLot - fake for now
"""

class TowingCompany(object):
    def __init__(self, sensors):
        self._sensors = sensors
    def call_tow_truck(self, spot_number):
        print("We called a tow truck!")
        self._sensors.sensor_off(spot_number)

class ParkingLot(object):
    pass

parking_lot = ParkingLot()

timing = TimeInterface(parking_lot)
sensors = InputFromSensors(parking_lot)

sensors.sensor_on(1)
timing.time_passed(45.0 * 60.) # 45 minutes

