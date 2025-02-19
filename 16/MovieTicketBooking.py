class Movie:
    def __init__(self,movieID,title,duration) -> None:
        self.movieID = movieID
        self.title = title
        self.duration = duration

    def getTitle(self):
        return self.title
class Ticket:
    def __init__(self,ticketID,movieID,seatNumber,price) -> None:
        self.TicketID = ticketID
        self.movieID = movieID
        self.seatNumber = seatNumber
        self.price = price

    def getTicketInfo(self):
        return f"ticketID {self.TicketID} MovieId {self.movieID} seatNumber {self.seatNumber} price {self.price}"

class Booking:
    def __init__(self,Ticket) -> None:
        self.Tickets=Ticket

    def bookTicket(self,Ticket):
        self.Tickets.append(Ticket)

    def cancelTicket(self,TicketID):
        for i in self.Tickets:
            if i.TicketID==TicketID:
                self.Tickets.remove(i)
                return True
        return False

    

    def getBookingDetails(self):
        return self.Tickets
    

def main():
    # Create a movie and multiple tickets
    movie = Movie(1, "Inception", 148)
    ticket1 = Ticket(101, movie.movieID, "A10", 12.5)
    ticket2 = Ticket(102, movie.movieID, "A11", 12.5)
    
    booking = Booking([])
    
    # Test booking tickets
    booking.bookTicket(ticket1)
    booking.bookTicket(ticket2)
    
    if len(booking.getBookingDetails()) != 2:
        print("Error: Tickets not booked correctly.")
    
    # Test ticket cancellation
    cancel_valid = booking.cancelTicket(101)
    print("Ticket 101 cancelled:", cancel_valid)
    
    cancel_invalid = booking.cancelTicket(999)
    print("Attempt cancellation of non-existent ticket:", cancel_invalid)
    
    # Final booking details
    print("Remaining tickets:")
    for t in booking.getBookingDetails():
        print(t.getTicketInfo())

if __name__ == '__main__':
    main()
