class Reservation:
    def __init__(self,name,roomNumber):
        self.name=name
        self.roomNumber=roomNumber
    def setRoom(self, roomNumber):
        self.roomNumber = roomNumber
    
    def setName(self, name):
        self.name = name
    
    def getRoom(self):
        return self.roomNumber
    
    def getName(self):
        return self.name

class Hotel:
    def __init__(self,numRooms=5):
        self.rooms= [None]*numRooms
        # pass
    # def Hotel(self):
    #     pass
    def buildRooms(self,num):
        self.rooms.extend([None] * num) 
    def reserveRoom(self,name,roomNum):
        if roomNum is not None:
            if 1<= roomNum <= len(self.rooms) and self.rooms[roomNum -1] is None:
                self.rooms[roomNum -1] =Reservation(name,roomNum)
                print(f"{name}- Room { roomNum} reserved")
            else:
                print("Room not available")
                return -1
        else:  
            for i in range(len(self.rooms)):
                if self.rooms[i] is None:
                    self.rooms[i] = Reservation(name, i + 1)
                    print(f"{name} - Room {i + 1} reserved")
                    return i + 1
            print("No available rooms")
            return -1
    def cancelReservations(self, name):
        for i in range(len(self.rooms)):
            if self.rooms[i] is not None and self.rooms[i].getName() == name:
                print(f"Reservation for {name} in Room {self.rooms[i].getRoom()} cancelled")
                self.rooms[i] = None
                return
        print("Reservation not found")
    def printReservations(self):
        total_reserved = sum(1 for room in self.rooms if room is not None)
        total_available = len(self.rooms) - total_reserved
        print("Current Reservations:")
        for i in range(len(self.rooms)):
            if self.rooms[i] is not None:
                print(f"{self.rooms[i].getName()} - Room {self.rooms[i].getRoom()}")
        print(f"Total Reservations: {total_reserved}")
        print(f"Available Rooms: {total_available}")
def run_Hotal():
    hotel = Hotel()
    while True:
        try:
            i=input().split()
            # print(i)
            # print(i[0].isdigit())
            if i[0].isdigit():
                print(i[0])
            else:
                if i[0] == "reserve":
                    print(i[1])
                elif i[0] == "print":
                    print("entered")
                elif i[0] == "cancel":
                    print(i[1])
                elif i[0] == "build" and len(i) > 1 and i[1].isdigit():
                    hotel.buildRooms(int(i[1]))

            
        
            

        except EOFError:
            break

if __name__=="__main__":
    run_Hotal()
