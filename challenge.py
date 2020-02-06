def actionProfit(array, difference_real = 0):
    for index_array, value_day in enumerate(array):
        for value_next_day in array[index_array+1:]:
            if value_day > value_next_day:
                continue
            difference = value_next_day - value_day
            if difference > difference_real:
                difference_real = difference
    return difference_real

print(actionProfit([7,1,5,3,6,4]))
