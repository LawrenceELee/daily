#!/usr/bin/env python3

'''
A quick and dirty ping client.

demos:
    *pythons object-oriented (OO) properties by creating a Client class
    with static-like functions (methods bound to object instances) hence
    'self' as 1st arg to all functions.

    *Client inherits from 'object' class by using 3.x style.
    more info: http://stackoverflow.com/questions/4015417/python-class-inherits-object

    by doing so it comes with some built-in functions like:
    >>> dir(object)
    ['__class__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

    *using subprocess to have OS eval "commands".

Note: you can write a similar program using perl, but it would be more
verbose and you would have to learn perl syntax (which isn't as pleasant as python).

'''



import subprocess




#server class inherits from object, will implicitly inherit from object
#if not specified.
#python allows for multiple inheritance Client(type1, type2, etc) something
#java doesn't allow.
class Client(object):

    #like a constructor, 'self' refers to _this_ instance.
    #static-like functions have to pass 'self' as first arg.
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname

    def set_ip(self, ip):
        self.ip = ip

    def set_hostname(self, hostname):
        self.hostname = hostname

    def ping(self, ip_addr):
        print("Pinging %s from %s (%s)" % (ip_addr, self.ip, self.hostname))
        subprocess.call(["ping", str(ip_addr)])
        #python to uses OS's to eval "commands".
        #haven't gotten options to work, by default windows pings 4 times.
        #in theory use optparse to parse options (-l, --version, etc).
        print("==================================================\n")


#driver/tester.
#if __name__ ... prevents 'import' from running program in python console.
#can further modularize program by refactoring driver code into main()
#and call each of the sub-function separately.
if __name__ == '__main__':
    server = Client('127.0.0.1', 'my_local_computer')
    server.ping('8.8.8.8')      #google public DNS
    server.ping('4.2.2.2')      #Level3 public DNS
