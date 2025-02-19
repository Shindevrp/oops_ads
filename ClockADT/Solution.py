class Time:
    def __init__(self, *args) -> None:
        if len(args) == 2:
            if args[0] > 24 or args[0] < 0 or args[1] > 60 or args[1] <= 0:
                self.hours = 0
                self.minutes = 0
            else:
                self.hours = args[0]
                self.minutes = args[1]
                
        if len(args) == 1:
            parts = args[0].split(":")
            if int(parts[0]) > 24 or int(parts[0]) < 0 or int(parts[1]) > 60 or int(parts[1]) <= 0:
                self.hours = 0
                self.minutes = 0
            else:
                self.hours = int(parts[0])
                self.minutes = int(parts[1])


    def tick(self):
        self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
            if self.hours == 24:
                self.hours = 0


    def advance(self, mins):
        self.minutes += mins
        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
            if self.hours == 24:
                self.hours = 0


    def isEarlierThan(self, otherTime):
        if self.hours < otherTime.hours:
            return True
        elif self.hours == otherTime.hours and self.minutes < otherTime.minutes:
            return True
        return False


    def display(self):
        return f"{self.hours:02d}:{self.minutes:02d}"


action = input()
count = int(input())

while count > 0:
    if action == 'constructor(int, int)':
        values = input().split(',')
        instance = Time(int(values[0]), int(values[1]))
        print(instance.display())

    elif action == 'constructor(String)':
        value = input()
        instance = Time(value)
        print(instance.display())

    elif action == 'tic()':
        value = input()
        instance = Time(value)
        instance.tick()
        print(instance.display())

    elif action == 'toc(int)':
        values = input().split(',')
        instance = Time(values[0])
        instance.advance(int(values[1]))
        print(instance.display())

    elif action == 'isEarlierThan(Clock)':
        values = input().split(',')
        time1 = Time(values[0])
        time2 = Time(values[1])
        if time1.isEarlierThan(time2):
            print('true')
        else:
            print('false')

    elif action == "toString()":
        print('null')

    count -= 1
