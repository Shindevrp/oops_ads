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