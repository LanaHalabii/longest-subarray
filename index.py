def longest_subarray(array) : 
    count_zeros = 0                                                     #to store the number of zeros
    count_ones = 0                                                      #to store the number of ones

    for i in range(len(array)):
        if array[i] == 0:
            count_zeros += 1                                            #if the value at the index is zero, count the zeros
        else:
            count_ones += 1                                             #if the value at the index is one, count the ones

    if count_zeros > count_ones:
        print("The length of the longest subarray is ", count_ones*2)   #if zeros are more than ones, then the array will be based on the number of ones times two to have equal zeros
    elif count_zeros < count_ones :
        print("The length of te longest subarray is ", count_zeros*2)   #if ones are more than zeros, then the array will be based on the number of zeros times to to have equal ones
    else:
        print("The array is already adjacent")                          #in case of the array being already adjacent, then there is no longer adjacent subarray

main_array = [0, 0, 0, 1, 1, 1, 1]
longest_subarray(main_array)
