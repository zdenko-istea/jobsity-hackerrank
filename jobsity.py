#The challenge was to complete a function that takes as an imput an integer and a list, based on the value specified on the integer,
#the list will be divided in sublists, then taking the minimum of each sublist we need to take the maximum of those minimums and use it
#as the value we'll return in our function.

#we'll save the first "x" values from the "space" list and save them in a second list, "listb". Then we'll select the minimum value from "listb"
#and save it on a third list called "listc". After each run, we will delete the first value saved on "space" list until we hit the limit where
#the length of "space" is minor than the value of "x". Once we hit that lenght, we'll look for the max value on list c and return that value.

def get_max(x,space):
    if x <=0:
        print("The value of x should be higher than 0")
        return
    l = len(space)
    if l < x:
        print("The value of x should not be higher than the length of the list")
        return
    listc = []
    while x < l:
        listb = []
        l = len(space)
        #print(list[0])
        listb = space[0:x]
        min_b = min(listb)
        print(listb)
        listc.append(min_b)
        del space[0]
    max_c = max(listc)
    print(max_c)
    return max_c

if __name__ == "__main__":
    get_max( 4, [1, 3, 5, 7, 9] )


