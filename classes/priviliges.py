class Priviliges:

    def __init__(self, first_name, last_name, username, age, location):
        super().__init__(first_name, last_name, username, age, location)

        self.priviliges = ['can add post', 'can delete post', 'can ban user', 'can disable account']

    def show_priviliges(self):
        print(f"{self.username} has following priviliges:")

        for privilige in self.priviliges:
            print(f"- {privilige.upper()}")