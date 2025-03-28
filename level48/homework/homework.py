def double_char(s):
    return "".join(i for i in s)

def feast(beast, dish):
    if beast[0]==dish[0] and beast[-1]==dish[-1]:
        return True
    else:
        return False
    
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)