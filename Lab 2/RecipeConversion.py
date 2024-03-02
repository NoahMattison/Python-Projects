# Recipe Conversion Program


from fraction import Fraction

def getFile():

    ''' Returns as a tuple the file name entered by the user and the
        open file object. If the file exceeds three attempts of opening
        sucessfully, an IO exception is raised.
    '''
    # ask for the file name
    rePrompt = True
    while rePrompt:
        fileName = input("Enter file name: ")
        for i in range(3):
            try:
                print(fileName)
                file = open(fileName, 'r')
            except FileNotFoundError:


    # check if the name is correct

    # if the name is correct then open the file

    # somehow return the file name and the open file object itself as a tuple

    # if wrong display error message

    # give three attempts

    # end program if exceeding three

    #code goes here

    return (file_name, input_file)


#don't touch removeMeasure
def removeMeasure(line):

    ''' Returns provided line with any initial digits and fractions (and
        any surrounding blanks) removed. 
    '''
    # creates and assigns two variables
    k = 0
    blank_char = ' '
    # checks to see if the first character of the line is a number and then replaces it
    while k < len(line) and (line[k].isdigit() or \
                             line[k] in ('/', blank_char)):
        k = k + 1

    return line[k:len(line)]

#don't touch scanAsFraction
def scanAsFraction(line):

    ''' Scans all digits, including fractions, and returns as a Fraction
        object. For example, '1/2' would return as Fraction value 1/2,
        '2' would return as Fraction 2/1, and '2 1/2' would return as
        Fraction value 3/2.
    '''

    # sets completed scan to boolean of False
    completed_scan = False
    # assigns a variable to a fraction using the Fraction built in class
    value_as_frac = Fraction(0,1)

    # k is 0 initially
    while not completed_scan:
        k = 0
        # checks for numbers in the beginning of the line
        while k < len(line) and line[k].isdigit():
            k = k + 1

        # slices the digit in the line from index 0 to k and converts it to an int
        numerator = int(line[0:k])

        # checks for a number or fraction
        if k < len(line) and line[k] == '/':
            k = k + 1
            start = k
            while k < len(line) and line[k].isdigit():
                k = k + 1

            # if no number then sets the denominator to the integer of the start of the line
            denominator = int(line[start:k])
        else:
            denominator = 1

        # creates the fraction
        value_as_frac = value_as_frac + Fraction(numerator, denominator)

        # if there is no number then the scan is completed
        if k == len(line):
            completed_scan = True
        # otherwise gets a slice from k to the length of line and strips it
        else:  
            line = line[k:len(line)].strip()
            
            if not line[0].isdigit():
                completed_scan = True
            
    return value_as_frac

def convertLine(line, factor):

    ''' If line begins with a digit, then returns line with the value
        incremented by factor. Otherwise, returns line unaltered.
        (For example, for a factor of 2, '1/4 cup sugar' returns as
        '1/2 cup sugar and '2 cups sugar' returns as '4 cups sugar'.)
    '''

    #code goes here
    #The idea is that you are going to step through the line of the recipe
    #if you find the digit in the line
    #scan through the line looking for the fraction and mulitply it by the factor to create a new fraction
    #then you need to build the new line by removing the original measure and putting the new fraciton measure in the line
    #return the new line
    #this method should utilize the scanasfraction and removemeasure functions



    return conv_line




# Do not change anything below this line!
# You are responsible for writing the 2 empty functions above
# ---- main
# This is where the program begins running
# Step through this and make sure you understand what main is doing

# display welcome
print('This program will convert a given recipe to a different')
print('quantity based on a specified conversion factor. Enter a')
print('factor of 1/2 to halve, 2 to double, 3 to triple, etc.\n')

try:

    # get file name and open file
    file_name, input_file = getFile()   #you need to write this function

    # get conversion factor
    conv_factor = input('Enter the conversion factor: ')
    conv_factor = scanAsFraction(conv_factor)   #you need to write this function

    # open output file named 'conv_' + file_name
    output_file_name = 'conv_' + file_name
    output_file = open(output_file_name, 'w')

    # convert recipe                  
    empty_str = ''
    recipe_line = input_file.readline()  #you are converting the recipe line by line

    while recipe_line != empty_str:     #while we haven't gotten to the end of the file
        recipe_line = convertLine(recipe_line, conv_factor)    #you need to write this funciton
        output_file.write(recipe_line)      #write the new line to the new file
        recipe_line = input_file.readline()   #get the next line of the original recipe

    # close files
    input_file.close()
    output_file.close()

    # display completion message to user
    print('Converted recipe in file: ', output_file_name)

except IOError as err_mesg:  # catch file open error
    print(err_mesg)

