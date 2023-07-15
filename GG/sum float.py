def sum_float(hw_list):
    sum = 0
    for hw_grade in hw_list:
        if type(hw_grade) == float:
            sum += hw_grade
    return sum
 
hw = [97, 77.7, 89.3, 0, 100]
print(sum_float(hw))