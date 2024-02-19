'''FOLLOW THAT SPY'''

'''You've been provided with an array of itinerary routes, 
decipher the precise destinations he will visit in the 
correct sequence according to his meticulously planned itineraries.
EXAMPLE:
Based on the provided routes:
[[USA, BRA], [JPN, PHL], [BRA, UAE], [UAE, JPN]]
The correct sequence of destinations is:
"USA, BRA, UAE, JPN, PHL"
NOTE:
You can safely assume that there will be no duplicate locations 
with distinct routes. All routes provided will have non-empty 
itineraries. There will always be at least one (1) route connecting 
one waypoint to another.'''


a = [['s', 'd'], ['a', 'g'], ['g', 'e'], ['e', 's']]

# VARIANT 1:
# =================


def find_routes(a):
    b = [x for row in a for x in row]
    n = 0
    string = ''
    for i in a:
        if b.count(i[0]) == 1:
            break
        n += 1
    t = a.pop(n)
    string += t[0] + ', ' + t[1]
    while len(a) > 0:
        n = 0
        for i in a:
            if t[1] == i[0]:
                string += ', ' + i[1]
                t = a.pop(n)
                n -= 1
            n += 1
    return string

# VARIANT 2:
# =================


def find_routes(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        x = 1
        string = arr[x - 1][0] + ', ' + arr[x - 1][1]
        return string
    else:
        string = arr[x - 1][0] + ', ' + arr[x - 1][1]
        for i in range(len(arr) - 1):  # len = 0,1,2
            if arr[x - 1][1] == arr[x][0]:
                string += ', ' + arr[x][0]
                x += 1
                continue
            elif arr[x - 1][1] != arr[x][0]:
                arr.insert(x, arr.pop())
                x = i + 1
    return string

# Best solution:
# =====================


def find_routes(routes: list) -> str:
    d = dict(routes)
    res = list(d.keys() - d.values())
    while res[-1] in d:
        res.append(d[res[-1]])
    return ', '.join(res)