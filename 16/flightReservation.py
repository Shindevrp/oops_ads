class Flight:
    def __init__(self,flightNumber,origin,destination,seatsAvailable) -> None:
        self.flightNumber = flightNumber
        self.origin = origin
        self.destination = destination
        self.seatsAvailable = seatsAvailable
        self.seats=[]

    def reserveSeat(self):
        if self.seatsAvailable >=len(self.seats):
            return True
        return False
    #  def reserveSeat(self):
    #     if self.seatsAvailable > 0:  
    #         self.seatsAvailable -= 1
    #         return True
    #     return False


class Reservation:
    def __init__(self,reservationID,flightNumber,passengerName) -> None:
        self.reservationID = reservationID
        self.flightNumber =flightNumber
        self.passengerName = passengerName
    def getReservationDetails(self):
        return f"reservationID {self.reservationID} flightNumber {self.flightNumber} passengerName {self.passengerName} "
class ReservationManager:
    def __init__(self,flights,reservations) -> None:
        self.flights = flights
        self.reservations = reservations
    def makeReservation(self,flightNumber,PassengerName):
        for f in self.flights:
            if f.flightNumber == flightNumber:
                for i in self.reservations:
                    if i.PassengerName == PassengerName:
                        self.reservations.append(i)
                        return i
        return False
    
# def __init__(self, flights) -> None:
#         self.flights = {flight.flightNumber: flight for flight in flights}  # Store flights in a dictionary
#         self.reservations = []
#         self.next_reservation_id = 1  

#     def makeReservation(self, flightNumber, passengerName):
#         if flightNumber in self.flights:
#             flight = self.flights[flightNumber]
#             if flight.reserveSeat():  
#                 reservation = Reservation(self.next_reservation_id, flightNumber, passengerName)
#                 self.reservations.append(reservation)
#                 self.next_reservation_id += 1
#                 return reservation
#             else:
#                 return "No seats available for this flight."
#         return "Flight not found."
        
        
        
    def cancelReservation(self,reservationID):
        # print(reservationID)
        for i in self.reservations:
            # print(reservationID)
            # print(i.reservationID)
            if i.reservationID==reservationID:
                
                self.reservations.remove(i)
                self.flights[i.flightNumber].seatsAvailable += 1
                return True
        return False
    

from flightReservation import Flight,Reservation,ReservationManager

def main():
# Create a flight with limited seats
    flight = Flight("FL123", "New York", "London", 2)
    # Reserve seats until flight is full
    print("Seat reservation 1:", flight.reserveSeat())
    print("Seat reservation 2:", flight.reserveSeat())
    print("Seat reservation 3 (should fail):", flight.reserveSeat())
    # Create reservations
    reservation1 = Reservation(1, flight.flightNumber, "John Smith")
    reservation2 = Reservation(2, flight.flightNumber, "Jane Doe")
    # Create ReservationManager and add the flight
    rm = ReservationManager([flight], [])
    rm.makeReservation(flight.flightNumber, "John Smith")
    rm.makeReservation(flight.flightNumber, "Jane Doe")
    # Display and cancel reservation
    print("Reservation details for ID 1:", reservation1.getReservationDetails())
    cancelled = rm.cancelReservation(1)
    print("Reservation 1 cancelled:", cancelled)
if __name__ == '__main__':
    main()