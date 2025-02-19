class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    
    def __str__(self):
        return self.name + " " + str(self.phone_number) + " " + self.email

class ContactManager:
    def __init__(self):
       self.contact_manager = []
    
    def addContact(self, contact):
        self.contact_manager.append(contact)
    
    def searchContact(self, name):
        for index in range(len(self.contact_manager)):
            if self.contact_manager[index].name == name:
                return index
        return -1

    def deleteContact(self, name):
        idx = self.searchContact(name)
        if idx != -1:
            self.contact_manager.pop(idx)
            return True
        return False
    
    def __str__(self):
        s = ""
        for i in self.contact_manager:
            s += str(i) + "\n"
        return s[:-1]



s = input().split()
cm = ContactManager()

while s[0] != "end":
    if s[0] == "add":
        contact = Contact(s[1], int(s[2]), s[3])
        cm.addContact(contact)
    elif s[0] == "search":
        print(cm.searchContact(s[1]))
    elif s[0] == "delete":
        print(cm.deleteContact(s[1]))
    elif s[0] == "display":
        print(cm)
    s = input().split()

