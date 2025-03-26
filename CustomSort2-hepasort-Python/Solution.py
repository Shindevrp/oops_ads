from functools import cmp_to_key
class Scorecard:
    def __init__(self,team_name, wins, losses, draws, no_result, points):
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.no_result = no_result
        self.points = points
    
    def __str__(self):
        return f"{self.team_name}: Points={self.points}, Wins={self.wins}, Losses={self.losses}, Draws={self.draws}, NoResult={self.no_result}"
    
    def compare(self, other):
        if self.points < other.points:
            return 1
        elif self.points > other.points:
            return -1
        else:
            if self.wins < other.wins:
                return 1
            elif self.wins > other.wins:
                return -1
            else:
                if self.losses < other.losses:
                    return -1
                elif self.losses > other.losses:
                    return 1
                else:
                    if self.draws < other.draws:
                        return 1
                    elif self.draws > other.draws:
                        return -1
                    else:
                        if self.no_result < other.no_result:
                            return -1
                        elif self.no_result > other.no_result:
                            return 1
                        else:
                            if self.team_name < other.team_name:
                                return -1
                            elif self.team_name < other.team_name:
                                return 1
        return 0

    
class BinaryHeapPriorityQueue:
    def __init__(self):
        self.array = []
        self.size1 = 0

    def add(self, ele):
        self.array.append(ele)
        self.size1 += 1
        self.swim(self.size1 - 1)
    
    def offer(self, ele):
        self.add(ele)

    def size(self):
        return self.size1
    
    def contains(self, ele):
        for i in self.array:
            if i == ele:
                return True
        return False
    
    def index_of(self, ele):
        for i in range(len(self.array)):
            if self.array[i] == ele:
                return i
        return None
    
    def peek(self):
        return self.array[0]
    
    def poll(self):        
        root = self.array[0]
        self.array[0] = self.array[self.size1 - 1]
        self.size1 -= 1
        self.array.pop()
        self.sink(0)
        return root
    
    def remove(self, ele):
        index = self.index_of(ele)        
        self.array[index] = self.array[self.size1 - 1]
        self.size1 -= 1
        self.array.pop()
        self.sink(index)
        self.swim(index)
        return True
    
    def clear(self):
        self.array = []
        self.size1 = 0

    def iterator(self):
        return self.array
    
    def __str__(self):
        return f"{self.array}"

    def swim(self, index):
        while index > 0 :
            parent = (index-1)//2
            if Scorecard.compare(self.array[index],self.array[parent])<0:
                self.array[index], self.array[parent] = self.array[parent], self.array[index]
                index = parent
            else:
                break
    
    def sink(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        s = index
        
        if left < self.size1 and Scorecard.compare(self.array[left], self.array[s]) < 0:
            s = left
        
        if right < self.size1 and Scorecard.compare(self.array[right], self.array[s]) < 0:
            s = right
        
        if s != index:
            self.array[index], self.array[s] = self.array[s], self.array[index]
            self.sink(s)


def sort():
    data = []
    a = 0
    while True:
        try:
            s = input().split(",")
            if len(s) == 1:
                a = int(s[0])
            elif len(s) > 1:
                team = Scorecard(s[0], int(s[1]), int(s[2]), int(s[3]), int(s[4]), int(s[5]))
                data.append(team)

        except Exception as e:
            break

    pq = BinaryHeapPriorityQueue()
    for team in data:
        pq.add(team)
    
    print(f"Top {a} teams:")
    for i in range(a):
        print(pq.poll())

sort()
