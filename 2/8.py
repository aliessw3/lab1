numbers = [1, 2, 3, 4, 5]
def remove_elements(lst):
    avg = sum(lst)/len(lst)
    print("average: ",avg)
    i = 0
    while i < len(lst):
        if lst[i] > avg:
            lst.pop(i)
        else:
            i += 1
remove_elements(numbers)
print(numbers)