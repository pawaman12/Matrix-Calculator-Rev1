print('︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽')
print('ヅ             MATRIX CALCULATOR              ヅ')
print('︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾')
def matrix_create(): # made a function that could be called when inputting values for a matrix
    R = int(input("Enter Rows➔ ")) # inputting rows
    C = int(input("Enter Columns➔ ")) #inputting columns

    matrix =[] #initializing a list

    print('Your values will be entered one by one now')
    for i in range(R): # first for loop in the function
        a=[]
        for j in range(C): # nested loop in the function to differentiate between the columns and rows
            a.append(int(input('★Enter The Values★ ➔ '))) # taking user inputs for the values to be placed inside the list "a"
        matrix.append(a) # appending list "a" into matrix

    return matrix #returning call for the function
print('Please Enter Values For Matrix 1:') # used for the input :)
a=matrix_create() # calling the function once
print('\n')
print('Please Enter Values For Matrix 2:') # calling the function twice
b=matrix_create()

print('Matrix a = ',a) # printing the matrix entered under the label "b"
print('Matrix b = ',b) # printing the matrix entered as "b"

print('')
print('Operations Menu ヅ ') # printing a menu to make the program user friendly
print('Enter 1 to add the matrices ヅ ') # addition
print('Enter 2 to subtract the matrices ヅ ') # subtraction
print('Enter 3 to multiply the matrices ヅ ') # multiplication
print('Enter 4 to exit ヅ ') # break
while True: # infinite loop
    oper=int(input('Enter the operation you would like ッ ->> ')) # taking input to decide what operation was to be used
    if oper>4 or oper<1:
        print('You might have entered an incorrect value please try again ッ  ') # printing message to be more attentive
    elif oper==4:
        print('Thankyou for using the Matrix Calculator Sorry For The Bugs If Any ッ ') # breaking the loop
        break
    elif oper==1: # addition
        result=[]  # initializing a empty list
        for i in range (len(a)): # making nested loops to add the answers to a list "z" and then to a matrix "result"
            z=[]
            for j in range(len(b)): # taking lenghts of a and b to know of the rows and columns of the inputted matrix
                z.append(a[i][j] + b[i][j])
            result.append(z)
        print('the calculator adding says➜ ',result)
    elif oper==2:  # subtraction
        result=[]
        for i in range (len(a)):  # making nested loops to add the answers to a list "z" and then to a matrix "result"
            z=[]
            for j in range(len(b)):
                z.append(a[i][j] - b[i][j])
            result.append(z)
        print('the calculator subtracting says➜ ',result)
    elif oper==3:
        r=[]
        for i in range(len(a)):  # making 3 nested loops to add the answers to a list "z" and then to a matrix "result"
            z=[] #initializing an empty row
            for j in range(len(b[0])): #range is 3
                mul=0
                for k in range(len(a[i])):
                    mul+= a[i][k] * b[k][j] 
                z.append(mul)
            r.append(z)
        print('the calculator multiplying says➜ ',r)  #printing the final matrix containing the multiple 
