class MyCalendar:

    def __init__(self):
        self.bookings = []
        

    def book(self, start: int, end: int) -> bool:
        if not self.bookings:
            self.bookings.append([start, end])
            return True

        for index in range(len(self.bookings)):
            if start < self.bookings[index][1]:
                if start >= self.bookings[index][0]:
                    return False
                if end > self.bookings[index][0]:
                    return False
 
        self.bookings.append([start, end])

        return True

            
        

[[47,50],[33,41],[25,32],[19,25],[3,8],[8,13],]
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)