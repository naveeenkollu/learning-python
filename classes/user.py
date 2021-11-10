class User:
    
    def __init__(self, first_name, last_name, username, age, location):
        self.first = first_name.title()
        self.last = last_name.title()
        self.full = first_name + " " + last_name
        self.username = username
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"Full Name: {self.full} \nAge: {self.age} \nLocation: {self.location}")

    def greet_user(self):
        print(f"Welcome back, {self.first}.\n")

    def login_attempt(self):
        print(f"Login Attempts: {self.login_attempts}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


user_1 = User('Naveen', 'Kollu', 'naveenkollu', 22, 'Hyderabad')
user_1.describe_user()
user_1.greet_user()


user_2 = User('Joe', 'Goldberg', 'pyschokiller', 28, 'Madre Linda')
user_2.describe_user()
user_2.greet_user()


user_3 = User('John', 'Wick', 'hitmanjohn', 38, 'Arizona')
user_3.describe_user()
user_3.greet_user()


user_4 = User('Will', 'Hunting', 'brilliantwill', 24, 'England')
user_4.describe_user()
user_4.greet_user()


user_5 = User('Dev', 'Patel', 'paradoxicaldev', 32, 'India')
user_5.describe_user()
user_5.greet_user()
user_5.increment_login_attempts()
user_5.increment_login_attempts()
user_5.increment_login_attempts()
user_5.login_attempt()

user_5.reset_login_attempts()
user_5.login_attempt()



