# # 8.3 T-shirt, 8.4
# def make_shirt(message,size = "L"):
#     print(f"Message to be printed: {message}")
#     print(f"You have order the size: {size}")

# make_shirt('I love python')
# print("\n")
# make_shirt('I love python', size="M")

# 8.5 Cities
# def describe_city(city_name, country="India"):
#     print(f"{city_name} is in {country}")

# describe_city('Hyderabad')
# describe_city('Munnar')
# describe_city('New York', 'USA')

# def bulid_person(first_name, last_name):
#     full_name = {
#         'first': first_name,
#         'last': last_name
#     }

#     return full_name


# bulid_person('Naveen', 'Kollu')


# def city_country(city, country):
#     return f"{city.title()}, {country.title()}"

# print(city_country('santiago', 'chile'))


# def make_album(artist, title):

#     artist_dict = {
#         'artist': artist.title(),
#         'title': title.title()
#     }

#     return artist_dict


# print(make_album('bruno mars', 'leave that door open'))

# def greet_message(names):

#     for name in names:
#         print(f"Hello, {name.title()}")

# user_name = ['ikaris', 'sersei', 'thena', 'fassos', 'sprite', 'kingo']
# print(greet_message(user_name))   


# unsent = ['Hi dude', 'good morning']
# sent = []

# def show_messages(messages):

#     for message in messages:
#         print(message)


# def send_messages(messages):

#     current_message = unsent.pop()
#     sent.append(current_message)

#     for message in messages:
#         print(f"Sent message: {message}")


# print(send_messages(unsent))

# def make_pizza(*toppings):
#     print(f"We are making your pizza with toppings:")

#     for topping in toppings:
#         print(f"- {topping}")


# print(make_pizza('mushroom', 'onion', 'pepperoni'))



# def make_pizza(size, *toppings):

#     print("We are making the pizza you have ordered:")
#     print(f"Pizza in inches: {size}")

#     for topping in toppings:
#         print(f"- {topping}")


# print(make_pizza(16, 'zucchini', 'squash', 'chicken'))

# def build_profile(first, last, **user_info):

#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info


# user_profile = build_profile(
#     'naveen', 'kollu', location="hyderabad", field="development"
# )

# print(user_profile)


# def make_sandwich(*ingredients):

#     print(f"You have order the sandwich with following:")

#     for ingredient in ingredients:
#         print(f"- {ingredient}")

#     print(f"Extra charges for mayonisse")

# ordered_sandwich = make_sandwich('chicken', 'mayonisse', 'pepper', 'some spice')

# print(ordered_sandwich)


# def make_user(first, last, **user_info):
#     print('Know your identity: ')

#     user_info['first_name'] = first
#     user_info['last_name'] = last
    
#     return user_info


# user_profile = make_user(
#     'bruce', 'mclaren', job="unemployed", city="Hyderabad"
# )

# print(user_profile)

# def make_car(manufacturer, model, **car_info):

    
#     car_dict = {
#         'manufacturer': manufacturer.title(),
#         'model': model.title(),
#     }

#     for key, value in car_info.items():
#                car_dict[key] = value

#     return car_dict



# new_car = make_car('totoya', 'supra', year=2020, color="red")
# print(new_car)



