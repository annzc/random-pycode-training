class todolist:
    def init(self, todo):
        self.todo = todo
    def create(self):
        thing = input("What do you want to add? ")
        self.todo.append(thing)
    def display(self):
        print("Your todo list:")
        for i in range(len(self.todo)):
            print(f"{i+1}. {self.todo[i]}")
    def delete(self):
        self.display()
        try:
            item_pos = int(input("which item number do you want to delete? "))
            del self.todo[item_pos-1]
            self.display()
        except:
            print("Invalid number to delete")
