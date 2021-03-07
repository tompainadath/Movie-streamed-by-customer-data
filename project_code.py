# Name: Tom Painadath
# Description: The program reads one line at a time. Each integer is checked
#              to see if it is a customer ID, Number of movies watched and Movie ID
#              The program then stores the data of each customers different arrays
#              All the arrays are then stored inside a single array. All the functions
#              iterated through the nested array to get the data

import os
array = []
arrays_list = []
limit = 2
i = 0
os.chdir('')  # add path to the file between ''
infile = open('dataFile.txt','r')
for line in infile:
    data = int(line)
    # check for the second item which is the number of movies watched
    if i == 1:
        next = data
        limit = i + next  # set limit for the last item to add in customer
        array.append(data)
    
    # Check if the limit is reached
    elif i == limit:
        array.append(data)  # add current item to customer array
        arrays_list.append(array)  # add current customer array to arrays_list array
        i = -1  # reset the i value
        array = []  # empty array to make space for new customer
        limit = 2  # set limit to 2 so that it reads atleast 2 items
    
    # add item to the array otherwise
    else:
        array.append(data)
    i = i+1  # increment i
infile.close()


# printAll function to print all the customers and theor data in the file
def printAll():
    arrays_list_len = len(arrays_list)  # find lenght of arrays_list
    
    # for loop to iterate through arrays_list
    for k in range(arrays_list_len):
        array_len = (len(arrays_list[k]))  # find length of current array in the arrays_list
        
        # for loop to iterate through current array items
        for j in range(array_len) :
            # add the first item in the array which is the customer ID
            if j == 0:
                customer = "Customer " + str(arrays_list[k][j])
            # add from 3rd item in the array which is the first Movie ID
            elif j == 2:
                customer = customer + " Watched " + str(arrays_list[k][j])
            # add remaining Movie IDs
            elif j != 1:
                customer = customer + "," + str(arrays_list[k][j])
        print(customer)  # Print customer data


# printCustomer function to print the data of just the customer specified 
def printCustomer(customerID):
    arrays_list_len = len(arrays_list) # find lenght of arrays_list
    # for loop to iterate through arrays_list
    for k in range(arrays_list_len):
        # check if customerID appears in any of the arrays in the list
        if customerID in arrays_list[k]:
            array_len = (len(arrays_list[k]))  # find length of current array in the arrays_list
            
            # for loop to iterate through current array items
            for j in range(array_len) :
                if j == 0:
                    customer = "Customer " + str(arrays_list[k][j])
                elif j == 2:
                    customer = customer + " Watched " + str(arrays_list[k][j])
                elif j != 1:
                    customer = customer + "," + str(arrays_list[k][j])
            print(customer)


# countViews function to find the number of times a movie was watched provide a Movie ID
def countViews(movieID):
    count = 0  
    arrays_list_len = len(arrays_list)  # find lenght of arrays_list
    # for loop to iterate through arrays_list
    for k in range(arrays_list_len):
        # check if the current array has an item matching MovieID
        if movieID in arrays_list[k]:
            count = count+1  # increment the count
            
    print("Movie " + str(movieID) + " was watched " + str(count) + " time(s)")  # print result


# main function to the test the program
def main():
  printAll()
  printCustomer(724)
  countViews(740)

if __name__ == "__main__":
    main()
