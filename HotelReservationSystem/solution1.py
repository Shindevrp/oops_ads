class Reservation:
    def __init__(self, name, roomNumber):
        self.name = name
        self.roomNumber = roomNumber
    
    def setRoom(self, roomNumber):
        self.roomNumber = roomNumber
    
    def setName(self, name):
        self.name = name
    
    def getRoom(self):
        return self.roomNumber
    
    def getName(self):
        return self.name

class Hotel:
    def __init__(self):
        self.rooms = [None] *5 
    def buidroom(self,num):
        if len(self.rooms) < num:

            self.rooms.extend([None] * num)
        else:
            self.rooms=self.rooms[:num]
    def buildsRooms(self, num):
        # print("j")
        # print(len(self.rooms),num)

        self.rooms.extend([None] * num)
            
        return f"Added {num} more rooms."

    def reserveRoom(self, name, roomNum=None):
        if roomNum is not None: 
            if 1 <= roomNum <= len(self.rooms) and self.rooms[roomNum - 1] is None:
                self.rooms[roomNum - 1] = Reservation(name, roomNum)
                print(f"{name} reserved Room {roomNum}")
                return roomNum
            else:
                print(f"Room {roomNum} is not available")
                return -1
        else:  
            for i in range(len(self.rooms)):
                if self.rooms[i] is None:
                    self.rooms[i] = Reservation(name, i + 1)
                    print(f"{name} reserved Room {i + 1}")
                    return i + 1
            print(f"Hotel is full. No room available for {name}")  
            return -1
  
    
    
    
    def cancelReservations(self, name):
        for i in range(len(self.rooms)):
            if self.rooms[i] is not None and self.rooms[i].getName() == name:
                print(f"Cancelled reservations for {name}")
                self.rooms[i] = None
                break
        
    
    def printReservations(self):
        total_reserved = sum(1 for room in self.rooms if room is not None)
        total_available = len(self.rooms) - total_reserved
        print("Current Reservations:")
        for i in range(len(self.rooms)):
            if self.rooms[i] is not None:
                print(f"{self.rooms[i].getName()} - Room {self.rooms[i].getRoom()}")
        print(f"Total Reservations: {total_reserved}")
        print(f"Available Rooms: {total_available}")

def run_Hotel():
    hotel = Hotel()
    while True:
        try:
            i = input().split()
            if i[0].isdigit():
                hotel.buidroom(int(i[0]))
            if i[0] == "reserve" and len(i) > 1:
                if len(i) == 3 and i[2].isdigit():
                    hotel.reserveRoom(i[1], int(i[2]))
                else:
                    hotel.reserveRoom(i[1])
            elif i[0] == "print":
                hotel.printReservations()
            elif i[0] == "cancel" and len(i) > 1:
                hotel.cancelReservations(i[1])
            elif i[0] == "build":
                print(hotel.buildsRooms(int(i[1])))
           
        except EOFError:
            break

if __name__ == "__main__":
    run_Hotel()
