

def countPairs(numbers,value):
    operated_number = []
    count = 0
    for num in numbers:
        for num2 in numbers:
            if f'{num} {num2}' not in operated_number and f'{num2} {num}' not in operated_number :
                operated_number.append('%s %s'%(str(num),str(num2)))
                operated_number.append('%s %s'%(str(num2),str(num)))
                if num + num2 == value:
                    count += 1
            else:
                pass
    print(f'Output: {count}')
    return count

#countPairs([1, 3, 2, 2, 3, 4], 5); // Output: 2
#countPairs([1, 1, 1, 1], 2); // Output: 1
#countPairs([1, 2, 3, 4, 5], 7); // Output: 2

countPairs([1, 3, 2, 2, 3, 4], 5);
countPairs([1, 1, 1, 1], 2); 
countPairs([1, 2, 3, 4, 5], 7);