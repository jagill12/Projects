''' John Gill
    Dr. Lindsay Jamieson
    CS 5001
    15 April 2023
'''
''' This program has a Stack class which the brackets application uses,
    and a Queue class which the tickets application uses.
'''
''' Align Online
    CS5001
    Sample code -- example of implementing the Stack ADT using
    the built-in functionality of the Python list
'''
import random

class Stack:
    def __init__(self, size):
        ''' Constructor
            Parameters:
            Self -- the current object
            Size -- the initialize size of our stack
        '''
        self.data = [0] * size
        self.end = 0

    def push(self, item):
        ''' Push -- adds something to the top of the stack
            Parameters:
            Self -- the current object
            Item -- the item to add to the stack
            Returns nothing
        '''
        if self.end >= len(self.data):
            print("Full!")
            return
        self.data[self.end] = item
        self.end += 1

    def pop(self):
        ''' Pop -- removes something from the top of the stack
            Parameters:
            Self -- the current object
            Returns the top element after removing it from the stack
        '''
        if self.end <= 0:
            print("Empty!")
            return
        self.end -= 1
        return self.data[self.end]

    def dump(self):
        ''' Dump -- debugging method for the stack
            Parameters:
            Self -- the current object
        '''
        for i in range(self.end - 1, -1, -1):
            print(self.data[i])

    def is_empty(self):
        ''' Is_empty -- checks if the stack is empty
            Parameters:
            Self -- the current object
            Returns True if the stack is empty, else False
        '''
        return self.end == 0
    
class Queue:
    def __init__(self, size):
        ''' Constructor
            Parameters:
            Self -- the current object
            Size -- the initialize size of our queue
        '''
        self.data = ["<EMPTY>"] * size
        self.end = 0
        self.start = 0

    def enqueue(self, item):
        ''' Enqueue -- adds something to the end of the queue
            Parameters:
            Self -- the current object
            Item -- the item to add to the queue
            Returns nothing
        '''
        if (self.end + 1) % len(self.data) == self.start:
            print("Full!")
            return
        self.data[self.end] = item
        self.end = (self.end + 1) % len(self.data)

    def dequeue(self):
        ''' Dequeue -- removes something from the front of the queue
            Parameters:
            Self -- the current object
            Returns the element of the front of the queue
        '''
        if self.start == self.end:
            print("Empty!")
            return
        item = self.data[self.start]
        self.data[self.start] = "<EMPTY>"
        self.start = (self.start + 1) % len(self.data)
        return item

    def dump(self):
        ''' Dump -- debugging method for the queue
            Parameters:
            Self -- the current object
        '''
        print(self.data, "Start:", self.start, ", End:", self.end)   

    def is_empty(self):
        ''' Checks if the queue is empty
            Parameters: None
            Self -- the current object
            Returns True if the queue is empty, else False
        '''
        return self.start == self.end    
    
def is_valid_brackets(string):
    ''' Takes in valid bracket pairs, tests their validity, then appends opening
        brackets to a list and pops closing brackets.
        Parameters -- string to be read in 
        Returns boolean value of the string according to string-reading parameters.
    '''
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']', '<': '>'}
    for char in string:
        if char not in brackets.keys() and char not in brackets.values():
            return False
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack:
                return False
            elif brackets[stack.pop()] != char:
                return False
    return not stack

def tickets(line):
    ''' Takes in line size, adds 0, 1, or 2 randomly for each spot to represent customers. 
        Says when a customer is being served, and which number they are.
        Parameters -- line size
        Returns print statements of current customer being served and how many are left after 100.
    '''
    q = Queue(size=line)
    num_entered = 0
    
    for i in range(line):
        # decide how many people to add to the queue
        num_add = random.randint(0, 2)
        num_entered += num_add
        
        for j in range(num_add):
            q.enqueue(f"Customer {num_entered - num_add + j + 1}")
        
        # serve a customer
        if not q.is_empty():
            served = q.dequeue()
            print(f"Serving {served}")
    
    # print the number of people still in the queue
    print(f"Customers still in queue: {q.end - q.start}")
         
def main():

    ''' This while loop continuously asks the user if they want to give it brackets.
        Then it analyzes those brackets to ensure they're valid. If not, it reprompts them
        until they're done. Then it runs the tickets function with a line length of 100.
    '''

    brackets = True
    while brackets:
        more = input("Do you want to test a stacking function for brackets? Enter Y for yes and N for no: ")
        while more != "Y" and more != "N":
            more = input("Looks like that wasn't a valid input! Input Y for yes and -1 for no: ")
        if more == "Y":
            string = input("Give me a set of brackets, both open and close." + "\n"
                        "Valid options are <, [, {, and (, with their closing counterparts.")
            if is_valid_brackets(string):
                print("That's valid.")
                continue
            if not is_valid_brackets(string):
                print("That's invalid.")
                continue
        elif more == "N":
            brackets = False
        

    tickets(100)

main()
