import random
import time

def standerd_search(x, target):
    for i in range(len(x)):
        if  x[i] == target:
            return i
    return -1


def binary_search(x, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:     
        high = len(x) - 1
    #Check if value is in list
    if high < low:
        return -1   


    midp = (low + high)// 2

    if x[midp] == target:
        return midp
    elif target < x[midp]:
        return binary_search(x, target, low, midp-1)
    else:
        return binary_search(x, target, midp+1, high)   

if __name__ == "__main__":
    

    length = 10000

    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3 *length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
            standerd_search(sorted_list, target)
    end = time.time()        
    print("Naive search time: ", (end - start)/length, "seconds")


    start = time.time()
    for target in sorted_list:
            binary_search(sorted_list, target)
    end = time.time()        
    print("Binary search time: ", (end - start)/length, "seconds")
