class Event:
    def __init__(self,eventID,eventName,location,capacity) -> None:
        self.eventID=eventID
        self.eventName=eventName
        self.location=location
        self.capacity =capacity
        self.currentRegistrations = 0

    def isEventFull(self):
        
        if self.currentRegistrations >=self.capacity:
            return True
        return False
class Participant:  
    def __init__(self,participantID,name,email) -> None:
        self.participantID = participantID
        self.name = name
        self.email = email
    def getParticipantInfo(self):
        return f"participantID {self.participantID} name {self.name} emil {self.email} "


# class EventManager:
#     def __init__(self,events,participants) -> None:
#         self.events = events
#         self.participants = participants
#     def registerParticipant(self,eventID, participant):

#         for event in self.events:
#             if event.eventID == eventID:
#                 for i in self.participants:
#                     if i.par
class EventManager:
    def __init__(self, events, participants) -> None:
        self.events = events  # List of Event objects
        self.participants = participants  # List of Participant objects
        self.eventRegistrations = {}  # Dictionary to map eventID to registered participants

    def registerParticipant(self, eventID, participant):
        for event in self.events:  # Loop through events
            if event.eventID == eventID:  # If event found
                if event.isEventFull():  # Check if event is full
                    return False  # Cannot register, event is full
                
                # Check if participant is already registered
                for p in self.participants:
                    if p.participantID == participant.participantID:
                        break  # Participant already exists
                else:
                    self.participants.append(participant)  # Add new participant
                
                # Register participant to the event
                event.currentRegistrations += 1  # Increase participant count
                if eventID not in self.eventRegistrations:
                    self.eventRegistrations[eventID] = []
                self.eventRegistrations[eventID].append(participant)
                
                return True  # Registration successful

        return False  # Event not found

        

    def listParticipants(self, eventID):
        out = []
        if eventID in self.eventRegistrations:
            for participant in self.eventRegistrations[eventID]: 
                out.append(participant)
        return out 



def main():
# Create an event with capacity 2
    event = Event(1, "Tech Conference", "Hall A", 2)
    # Create participants
    participant1 = Participant(101, "Mike", "mike@example.com")
    participant2 = Participant(102, "Anna", "anna@example.com")
    participant3 = Participant(103, "John", "john@example.com")
    em = EventManager([], [])
    em.events.append(event)
    # Register participants
    reg1 = em.registerParticipant(1, participant1)
    reg2 = em.registerParticipant(1, participant2)
    reg3 = em.registerParticipant(1, participant3)
    print("Participant 101 registered:", reg1)
    print("Participant 102 registered:", reg2)
    print("Participant 103 registered (should fail):", reg3)
    # List participants
    print("Participants for event 1:")
    for p in em.listParticipants(1):
        print(p.name)
if __name__ == '__main__':
    main()
