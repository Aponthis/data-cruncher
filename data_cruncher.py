#Used to find the mode of a list of numbers manually

data_list = []
data_position = 0
median = 0.0
mean = 0.0

def getData():  #returns the data with leading and following spaces stripped
    input_data = raw_input("List numbers here, each separated by a space. \n")
    return input_data.strip()

data_string = getData()

while(1):
    try: #checks that there is another number to be added
        data_string.split(' ')[data_position]
    except:
        break

    data_list.append(data_string.split(' ')[data_position]) #adds the next number to the list
    data_position += 1

data_list = list(map(float, data_list)) # converts the list into integers, from strings

def sortList():
    list_position = 0
    sorting_incomplete = 1
    while(sorting_incomplete): #sorts in order to find median
        sorting_incomplete = 0 #states that sorting is complete, which is assumed to be true until something is changed
        while(list_position < (len(data_list) - 1)): #checks if the second position to be compared exists
            if (data_list[list_position] > data_list[(list_position + 1)]):
                stored_value = data_list[list_position]
                data_list[list_position] = data_list[list_position + 1]
                data_list[list_position + 1] = stored_value
                sorting_incomplete = 1  #something was changed, so sorting is not complete

            list_position += 1 #moves to the next numbers to be compared
        list_position = 0

def findMedian():
    sortList()
    if(len(data_list) % 2): #finds median for list with odd number of data points
        return data_list[len(data_list) / 2]
    else: #finds median for list with even number of data points
        return (data_list[len(data_list) / 2] + data_list[len(data_list) / 2 - 1]) / 2

def findMean():
    list_position = 0
    total = 0
    while(list_position < len(data_list)): #finds total of all numbers
        total += data_list[list_position]
        list_position += 1

    return total / len(data_list)

def findMode(): #Finds the mode, assuming the list has been sorted
    list_position = 0
    frequent_value_identity = [0.0]
    frequent_value_count = 0
    observed_value_identity = 0.0
    observed_value_count = 0
    while(list_position < len(data_list)): #goes through the whole list
        observed_value_identity = data_list[list_position]
        observed_value_count = data_list.count(observed_value_identity)

        if(observed_value_count > frequent_value_count):
            frequent_value_identity = [0.0]#deletes the list
            frequent_value_identity[0] = data_list[list_position]
            frequent_value_count = observed_value_count

        elif(observed_value_count == frequent_value_count):
            frequent_value_identity.append(observed_value_identity) #adds the equal mode to the list

        list_position += observed_value_count #skips identical values (list is ordered)

    if(frequent_value_count == 1):
        frequent_value_identity = None

    if(len(frequent_value_identity) > 1): #if the list is actually a list, proceed
        return frequent_value_identity
    else:
        return frequent_value_identity[0] #if the list  is not actually a list, just return a float

mean = findMean()
median = findMedian()
mode = findMode()

print("Data sorted: {}" .format(data_list))
print("Median: {}" .format(median))
print("Mean: {}" .format(mean))
print("Mode: {}" .format(mode))
exit()
