'''
Simple program that calculates a value using formula/equation.
This example is an interest calculator.

version 2: use dictionary to store choicses to shorten code and make it
           more concise.
           more shell script like and less object-orient/modular program.

demos:
    *use dictionary for user choices instead of if/else or case statements.
    this makes it more extensible (easier to add more/newer choices) and
    adaptable.

    *use command line args to take in input so that it is more like a linux     utility instead of user input via menu.
    Then we can use it in bash scripts, more easily pipe the output to
    other programs, alias it to shorter commands, etc...

    *simple interest vs compound interest.

usage: "python3 filename.py calculation_type capital interest_rate time"
'''

from sys import argv, exit
'''
argv to read from command line args, exit to quit program.
'''


"""
def display_menu_and_read_choice():
    '''
    use a dictionary to store choices for easier additions.
    rather than using if/else or case statements.
    '''
    print("1) Simple Interest")
    print("2) Compound Interest")
    return int(input("Enter the # of the choice: ")) #input returns a str

def simple(capital, rate, time):
    return capital * (1 + (rate * time))

def compound(capital, rate, time):
    return capital * ((1 + rate) ** time)
"""

'''
shrunk the above down to a dict/hash and anonymous functions (lambda).
'''
choices = {
    'simple': lambda capital, rate, time: capital * (1 + (rate * time)),
    'compound': lambda capital, rate, time: capital * ((1 + rate) ** time)
}



'''
error checking args.
'''
if len(argv) != 5 or argv[1] not in choices:
    print("usage: %s <%s> capital rate time" % (argv[0], '|'.join(choices)))
    exit(1) #exit immediately if incorrect args.


"""
def read_input_and_calculate(choice):
    capital = float(input("Enter capital: "))
    interest_rate = float(input("Enter interest rate: "))
    time = float(input("Enter time (years): "))

    if choice == 1:
        print(simple(capital, interest_rate, time))
    elif choice == 2:
        print(compound(capital, interest_rate, time))
    else:
        print("Not a valid choice.")
"""

'''
we can refactor above code into a single 'map' since float function is called on each of the inputs.

since both functions take the same 3 variables, we ca use python's variable unpacking (comma) to pick out each arg from the ret val of map (list).
'''
capital, rate, time = map(float, argv[2:])





"""
def main():
    '''
    driver/tester.
    '''
    choice = display_menu_and_read_choice()
    read_input_and_calculate(choice)

if  __name__ =='__main__':
    main()
"""
'''
don't need a complicated main/driver. just apply the function name to the
parameters. not sure what feature of python this is called, reflection? function naming?
'''
print(choices[argv[1]](capital, rate, time))
