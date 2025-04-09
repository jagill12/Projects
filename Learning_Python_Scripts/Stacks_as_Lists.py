''' Align Online
CS5001
Sample code -- example of implementing the Stack ADT using
the built-in functionality of the Python list
'''
class Stack:
    def __init__(self, size):
        ''' Constructor
        Parameters:
        self -- the current object
        size -- the initialize size of our stack
        '''
        self.data = list()

    def push(self, item):
        ''' push -- adds something to the top of the stack
        Parameters:
        self -- the current object
        item -- the item to add to the stack
        Returns nothing
        '''
        self.data.append(item)

    def pop(self):
        ''' pop -- removes something from the top of the stack
        Parameters:
        self -- the current object
        Returns the top element after removing it from the stack
        '''
        return self.data.pop()
    
    def dump(self):
        ''' dump -- debugging method for the stack
        Parameters:
        self -- the current object
        '''
        for i in range(len(self.data) - 1, -1, -1):
            print(self.data[i])

    def count(self):
        ''' count
            Params - the current object
            returns the number of elements in our stack'''
        return len(self.data)
    
    def peek(self):
        '''peek at top of stack
            params: current object
            returns the top value on the stack
        '''
        if self.count():
            return self.data[-1]
        
    def pop_queue(self):
        '''removes the feature of self'''
        self.data.remove(self.data[0])
    
def main():
    '''
    Driver program that uses our stack so that we can see it working
    '''
    my_stack = Stack(5)
    while True:
        cmd = input("push, pop, dump, peek, count, or exit? ")
        if cmd == "push":
            val = input("Data to add? ")
            my_stack.push(val)
        elif cmd == "pop":
            val = my_stack.pop()
            print("pop() returned --", val)
        elif cmd == "dump":
            my_stack.dump()
        elif cmd == "peek":
            print(my_stack.peek())
        elif cmd == "count":
            print(my_stack.count())
        elif cmd == "exit":
            break
if __name__ == "__main__":
    main()
