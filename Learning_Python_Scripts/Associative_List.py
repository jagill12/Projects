
class AssocArrays():
    
    def __init__(self):
        
        self.mystudents = []
        self.myclasses = []

    def add(self, name, course):
        self.mystudents.append(name)
        self.myclasses.append(course)

    def display(self):
        for i in range(len(self.mystudents)):
            print(self.mystudents[i] + " in " + self.myclasses[i])

    '''def delete(self, student):
        index = self.mystudents.index(student)
        course = self.myclasses[index]
        self.mystudents.remove(student)
        self.myclasses.remove(course)'''

    def delete2(self, student):
        index = self.mystudents.index(student)
        self.mystudents.pop(index)
        self.myclasses.pop(index)

    '''def delete3(self, student):
        for index in range(len(self.mystudents)):
            if self.mystudents[index] == student:
                self.mystudents.remove(index)
                self.myclasses.pop(index)'''

def main():
    me = AssocArrays()
    me.add("Bob", "CS5001")
    me.add("Sue", "CS5002")
    me.add("John", "CS5003")
    print("After add: ")
    me.display()
    me.delete2("Bob")
    print("\n", "After delete", "\n")
    me.display()

main()
