#Class
class Student():
    
    # initialize when call Student
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    # Method: get, set attributes
    def get_id(self):
        return self.id
    
    def set_name(self, new_name):
        self.name = new_name
    
    def get_name(self):
        return self.name
    
    def show(self):
        print(f"ID: {self.get_id()}")
        print(f"Name: {self.get_name()}")
        
        
  