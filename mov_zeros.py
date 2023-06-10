def move_zeros(lst):
    zeros = [number for number in lst if number == 0]
    res = [number for number in lst if number != 0] 
    return res + zeros






x =  [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
print (move_zeros(x))