class Patient:
    def __init__(self,patientID,name,age) -> None:
        self.patientID = patientID
        self.name = name
        self.age = age

    def getPatientInfo(self):
        return f"patientID {self.patientID} name {self.name} age {self.age}"
class Appointment:
    def __init__(self,appointmentID,patientID,doctorName,appointmentTime) -> None:
        self.appointmentID=appointmentID
        self.patientID = patientID
        self.doctorName = doctorName
        self.appointmentTime = appointmentTime

    def getAppointmentDetails(self):
        return f"appointmentID {self.appointmentID} patientID{self.patientID}  doctorName {self.doctorName}appointmentTime {self.appointmentTime}"
class PatientManager: 
    def __init__(self,patients,appointments) -> None:
        self.patients = patients
        self.appointments =appointments
    def scheduleAppointment(self,Appointment):
        self.appointments.appennd(Appointment)
        
    def cancelAppointment(self,appointmentID):
        for i in self.appointments:
            if i.appointmentID==appointmentID:
                self.appointments.remove(i)
                return True
        return False
    def listAppointmentsForPatient(self,patientID):
        all=[]
        for i in self.patients:
            if i.patientID==patientID:
                all.append(i)
                
        return all
    
def main():
# Create a patient and two appointments
    patient = Patient(1, "Emma", 30)
    app1 = Appointment(101, patient.patientID, "Dr. Brown", "2:00 PM")
    app2 = Appointment(102, patient.patientID, "Dr. White", "3:00 PM")
    pm = PatientManager([], [])
    pm.patients.append(patient)
    pm.appointments.extend([app1, app2])
    # List appointments for patient
    print("Appointments for Emma:")
    for app in pm.listAppointmentsForPatient(1):
        print(app.getAppointmentDetails())
    # Cancel an appointment and check again
    cancelled = pm.cancelAppointment(101)
    print("Appointment 101 cancelled:", cancelled)
    print("Remaining appointments for Emma:")
    for app in pm.listAppointmentsForPatient(1):
        print(app.getAppointmentDetails())
if __name__ == '__main__':
    main()
