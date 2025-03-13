def reverseseq(n):
    return list(range(n, 0, -1))

def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

def is_divisible(n,x,y):
    if n%x==0 and n%y==0:
        return True
    else:
        return False
    
def count_sheep(n):
    result = ""
    for i in range(1, n+1):
        result += f"{i} sheep..."
    return result

def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return 'D'
    else:
        return "F"
    