def moveElement(nums, element):
    # start loop to iterate over array
    for item in nums:
        # if the element in the array is equal to...
        if item == element:
            # get index of item
            index = nums.index(item)
            # copy the element and add it to the end of the array
            nums.append(item)
            # then remove the element from it's current spot in the array
            nums.pop(index)
    
    return nums

dates = [
    {'key': '2024-03-15', 'value': 67}, {'key': '2024-01-22', 'value': 82},
    {'key': '2023-07-03', 'value': 54}, None, {'key': '2023-09-08', 'value': 45},
    None, {'key': '2024-02-27', 'value': 11}, {'key': '2023-11-11', 'value': 99},
    {'key': '2024-01-14', 'value': 73}, {'key': '2023-12-18', 'value': 28},
    None, {'key': '2023-05-10', 'value': 42}, {'key': '2023-08-25', 'value': 35},
    None, {'key': '2024-03-02', 'value': 76}, None, {'key': '2023-10-14', 'value': 66},
    {'key': '2023-12-25', 'value': 55}, {'key': '2023-09-20', 'value': 13},
    None, {'key': '2024-01-30', 'value': 92}, None, {'key': '2023-04-10', 'value': 21},
    {'key': '2023-06-12', 'value': 34}, None, None, {'key': '2023-11-30', 'value': 16},
    {'key': '2023-10-02', 'value': 82}, {'key': '2024-02-15', 'value': 93},
    {'key': '2023-05-18', 'value': 39}, None, {'key': '2023-08-02', 'value': 79},
    None, {'key': '2024-03-01', 'value': 41}, {'key': '2023-11-17', 'value': 68},
    {'key': '2024-02-05', 'value': 54}, {'key': '2023-06-28', 'value': 56},
    None, {'key': '2024-01-18', 'value': 15}, {'key': '2023-09-13', 'value': 12},
    None, {'key': '2023-07-19', 'value': 23}, {'key': '2023-12-09', 'value': 18},
    {'key': '2024-03-07', 'value': 65}, None, {'key': '2023-10-20', 'value': 24},
    {'key': '2023-08-13', 'value': 98}, {'key': '2024-01-03', 'value': 61},
    {'key': '2023-11-25', 'value': 33}, {'key': '2023-12-04', 'value': 71},
    None, {'key': '2023-09-30', 'value': 19}, None, {'key': '2023-05-02', 'value': 37},
    {'key': '2024-02-11', 'value': 83}, {'key': '2023-08-22', 'value': 48},
    None, {'key': '2023-07-12', 'value': 74}, None, {'key': '2023-06-03', 'value': 80},
    {'key': '2024-01-08', 'value': 29}, None, {'key': '2023-11-08', 'value': 22},
    {'key': '2023-12-02', 'value': 49}, {'key': '2023-09-18', 'value': 59},
    None, {'key': '2023-10-10', 'value': 26}, {'key': '2024-01-25', 'value': 89},
    {'key': '2023-07-30', 'value': 58}, {'key': '2023-05-22', 'value': 64},
    {'key': '2023-11-22', 'value': 50}, {'key': '2023-09-14', 'value': 40},
    None, None
]



newList = moveElement(dates, None)
print(newList)   