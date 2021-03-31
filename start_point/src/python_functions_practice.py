
def return_10():
    return 10

print (return_10)

def add(number1, number2):
    return (number1 + number2)


def subtract(number1, number2):
    return (number1 - number2)   


def multiply(number1, number2):
    return (number1 * number2)

def divide(number1, number2):
    return (number1 / number2)

def length_of_string(string_1):
    return len(string_1)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(number):
    if number is 1:
        return "January"
    elif number is 2:
        return "February"
    elif number is 3:
        return "March"
    elif number is 4:
        return "April"
    elif number is 5:
        return "May"
    elif number is 6:
        return "June"
    elif number is 7:
        return "July"
    elif number is 8:
        return "August"
    elif number is 9:
        return "September"
    elif number is 10:
        return "October"
    elif number is 11:
        return "November"
    elif number is 12:
        return "December"



def number_to_short_month_name(number):
    if number is 1:
        return "Jan"
    elif number is 2:
        return "Feb"
    elif number is 3:
        return "Mar"
    elif number is 4:
        return "Apr"
    elif number is 5:
        return "May"
    elif number is 6:
        return "Jun"
    elif number is 7:
        return "Jul"
    elif number is 8:
        return "Aug"
    elif number is 9:
        return "Sept"
    elif number is 10:
        return "Oct"
    elif number is 11:
        return "Nov"
    elif number is 12:
        return "Dec"

def volume_of_cube(side_length):
    return side_length * side_length * side_length

def reverse_string(string): 
    return string[::-1]

def farenheit_to_celsius(number):
    return (number - 32) * 5 / 9
    