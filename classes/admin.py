from priviliges import Priviliges

class Admin:

    def __init__(self, first_name, last_name, username, age, location):
        super().__init__(first_name, last_name, username, age, location)
        
        self.priviliges = Priviliges()

 

admin_user = Admin('naveen', 'kollu', 'misterkurono', 22, 'Hyderabad')
admin_user.priviliges.show_priviliges()


