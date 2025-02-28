

class DateADT:
    def __init__(self, *args) -> None:
        if len(args) == 3:
            self.year = int(args[0])
            self.month = int(args[1])
            self.day = int(args[2])
            self.hours = 0
            self.minutes = 0
            self.seconds =0
            self._validate_month()
            self._validate_day()
            self._validate_time()
            
        elif len(args) == 6:
            self.year = int(args[0])
            self.month = int(args[1])
            self.day = int(args[2])
            
            self.hours = int(args[3])
            self.minutes = int(args[4])
            self.seconds =int(args[5])
            self._validate_month()
            self._validate_day()
            self._validate_time()
        
                
                
        elif len(args) == 1 and isinstance(args[0],str):
            parts = args[0].split()
            date_parts = list(map(int, parts[0].split("-")))
            time_parts = list(map(int, parts[1].split(":")))
            year, month, day = date_parts
            self.year= year
            self.month =month
            self.day =day
            hours, minutes, seconds = time_parts
            self.hours = hours
            self.minutes = minutes
            self. seconds = seconds
            self._validate_month()
            self._validate_day()
            self._validate_time()

    def getYear(self):
        return self.year
    def getMonth(self):
        return self.month
    def getDay(self):
        return self.day
    def getHours(self):
        return self.hours
    def getMinutes(self):
        return self.minutes
    def getSeconds(self):
        return self.seconds
    

    def setYear(self, year):
        self.year = year
        # self.validate_data()
    
    def setMonth(self, month):
        self.month = month
        # self.validate_data()
    
    def setDay(self, day):
        self.day = day
        # self.validate_data()
    
    def setHours(self, hours):
        self.hours = hours
        # self.validate_data()
    
    def setMinutes(self, minutes):
        self.minutes = minutes
        # self.validate_data()
    
    def setSeconds(self, seconds):
        self.seconds = seconds
        # self.validate_data()
    



    def getTime(self):
        ms_per_day = 86400000
        ms = (self.year - 1970) * 365 * ms_per_day
        
        ms += self.month * 30 * ms_per_day
        ms += (self.day - 1) * ms_per_day
        ms += self.hours* 3600000
        ms += self.minutes * 60000
        ms += self.seconds * 1000
        
        return ms
    def setTime(self, ms):
        ms_per_day = 86400000
        total_days = ms // ms_per_day
        remaining_ms = ms % ms_per_day

        self.year = 1970 + total_days // 365
        total_days %= 365

        self.month = total_days // 30
        total_days %= 30

        self.day = total_days + 1
        
        remaining_seconds = remaining_ms // 1000
        self.hours = remaining_seconds // 3600
        remaining_seconds %= 3600
        self.minutes = remaining_seconds // 60
        self.seconds = remaining_seconds % 60

        

    def before(self,d1):
        if self.getYear() < d1.getYear():
            return True
        elif self.getYear() == d1.getYear():
            if self.getMonth() < d1.getMonth():
                return True
            elif self.getDay() < d1.getDay():
                return True
        return False
    
    def after(self,d1):
        return not self.before(d1)
    
    def _validate_month(self):
        if not (0 <= self.month <= 11):
            raise ValueError()

    def _validate_day(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days_in_month[1] = 29
        if not (1 <= self.day <= days_in_month[self.month]):
            raise ValueError()

    def _validate_time(self):
        if not (0 <= self.hours <= 23):
            raise ValueError()
        if not (0 <= self.minutes <= 59):
            raise ValueError()
        if not (0 <= self.seconds <= 60):
            raise ValueError()

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def toString(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d} " \
        f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"