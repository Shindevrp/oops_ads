from functools import cmp_to_key
class Team:
    def __init__(self, name, wins, losses, draws, no_result, points):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.no_result =no_result
        self.points = points
    def __str__(self) -> str:
        return f"{self.name}: Points={self.points}, Wins={self.wins}, Losses={self.losses}, Draws={self.draws}, NoResult={self.no_result}"
    
    
def custom_comparator(t1, t2):
    if t1.points < t2.points:
        return 1
    elif t1.points > t2.points:
        return -1
    else:
        if t1.wins < t2.wins:
            return 1
        elif t1.wins> t2.wins:
            return -1
        else:
            if t1.losses < t2.losses:
                return -1
            elif t1.losses> t2.losses:
                return 1
            else:
                if t1.draws < t2.draws:
                    return 1
                elif t1.draws> t2.draws:
                    return -1
                else:
                    if t1.no_result < t2.no_result:
                        return -1
                    elif t1.no_result> t2.no_result:
                        return 1
                    else:
                        if t1.name < t2.name:
                            return -1
                        elif t1.name> t2.name:
                            return 1
    return 0


def inputsparsing(): 
    teams =[]
    while True:
        try:
            s=input().split(",")
            # print(s)
            team = Team(s[0],int(s[1]),int(s[2]),int(s[3]),int(s[4]),int(s[5]))
            teams.append(team)  
        except:
            break

    teams.sort(key= cmp_to_key(custom_comparator))
    print("Sorted Leaderboard:")
    for i in teams:
        print(i)

inputsparsing()