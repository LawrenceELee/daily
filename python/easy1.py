'''
Simple a program that will ask the name, age, and height.

Outputs information back, in the format:
    Your name is __, you are ___ years old, and you are ___ high.

Extra credit, the program log this info in a file to be accessed later.

demos:
    reading input from command line.
    passing parameters as a list instead of individual vars.
    reading/writing to files.

To run: type "python3 filename.py"
'''


def read_input():
    '''
    return: tuple, (name, age, height)
    '''
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    height = input("Enter your height (cm): ")
    return (name, age, height)

def output(info):
    '''
    input: a tuple containing (name, age, height)
    return: none
    '''
    print("Your name is",info[0],", you are ",info[1]," years old, and you are ",info[2]," cm high.")

def log(info):
    '''
    input: a tuple containing (name, age, height)
    return: none
    '''
    #it is a good practice to use 'try/finally' in case an errors occur.
    #pre v2.5 style
    '''
    try:
        f = open('easy1.data', 'a') #r read-only, w read/write, a append.
        f.write(str(info)) #can't write tuple to file, convert to str first.
        f.write('\n')
    finally:
        f.close()
    '''
    #v2.5+ idiom is to use the 'with' keyword.
    with open('easy1.data', 'a') as f:
        f.write(str(info))
        f.write('\n')
        #Even though we didn’t call close(), the context manager closes it
        #after exiting the 'with' block


def main():
    '''
    driver/tester.
    '''
    info = read_input()
    output(info)
    log(info)


if  __name__ =='__main__':
    main()
