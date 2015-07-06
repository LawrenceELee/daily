'''
Simple program that calculates a value using formula/equation.
This example is an interest calculator.

version 1: straight forward code using if/case or case statements to display
           options.

demos:
    *simple interest vs compound interest.

usage: "python3 filename.py"
'''


def display_menu_and_read_choice():
    '''
    use a dictionary to store choices for easier additions.
    rather than using if/else or case statements.
    '''
    print("1) Simple Interest")
    print("2) Compound Interest")
    return int(input("Enter the # of the choice: ")) #input returns a str

def read_input_and_calculate(choice):
    capital = float(input("Enter capital: "))
    interest_rate = float(input("Enter interest rate: "))
    time = float(input("Enter time (years): "))

    '''
    There is a slight bug using this method to pass in the choice.
    We don't know if the user picked a valid option until after we do the
    calculation.
    '''
    if choice == 1:
        print(simple(capital, interest_rate, time))
    elif choice == 2:
        print(compound(capital, interest_rate, time))
    else:
        print("Not a valid choice. Nothing was calculated")

def simple(capital, rate, time):
    return capital * (1 + (rate * time))

def compound(capital, rate, time):
    return capital * ((1 + rate) ** time)

def main():
    '''
    driver/tester.
    '''
    choice = display_menu_and_read_choice()
    read_input_and_calculate(choice)

if  __name__ =='__main__':
    main()
