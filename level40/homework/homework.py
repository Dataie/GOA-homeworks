def paperwork(n, m):
    if n<0 or m<0:
        return 0
    else:
        return m*n
    
def make_upper_case(s):
    return s.upper()

def are_you_playing_banjo(name):
    if name[0]=="R" or name[0]=="r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
def past(h, m, s):
    return h*3600000+m*60000+s*1000

def abbrev_name(name):
    parts = name.split()                   
    initials = parts[0][0].upper() + '.' + parts[1][0].upper()
    return initials