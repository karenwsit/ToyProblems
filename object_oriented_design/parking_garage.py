#7.4 Parking Lot: Design a parking lot using object-oriented principles

#Questions:
#How to best structure all these different classes. Should they be subclasses? or stay separate classes?
#How to best pass variables from other classes when they are instance variables
#Reference to someone else's implementation in Python: https://gist.github.com/anonymous/a6247da9d061b1eab899

class ParkingLot(ParkingSpace):

    """All parking lots have a name, a maximum capacity and charge an hourly rate"""

    def __init__(self, name, capacity, hourly_rate):
        self.name = name
        self.capacity = capacity
        self.hourly_rate = hourly_rate

    def find_compact_avail(self):
        # SELECT * FROM PARKING SPACE WHERE TYPE=COMPACT AND OCCUPIED=FALSE

    def find_parking_lot_avail(self):
        # SELF.CAPACITY - SELECT COUNT(*) FROM TICKET WHERE PAID= FALSE

    def calculate_daily_rev(self):
        # SELECT SUM(TOTAL_COST) FROM TICKET WHERE PAID= TRUE AND EXITTIME= TODAY(DATE)


class ParkingSpace(object):

    """Parking spaces make up a parking lot with occupied and space type attributes"""

    def __init__(self, occupied, space_type):
        #boolean value
        self.occupied = occupied
        self.space_type = space_type

class Ticket(ParkingLot):

    """Tickets are issued by a parking lot with entrance and exit times, paid, and total cost attributes"""

    def __init__(self, entrance_time, exit_time, paid, total_cost=None):
        #timestamp value
        self.entrance_time = entrance_time
        #timestamp value
        self.exit_time = exit_time
        #boolean value
        self.paid = paid
        self.total_cost = total_cost

    def calculate_total_cost(self):
        parked_time = self.exit_time - self.entrance_time
        if parked_time == 0:
            parked_time += 1
        elif type(parked_time) != integer:
            #round up to the nearest hour if parked_time is not an integer
        parked_time * self.hourly_rate
