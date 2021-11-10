# # Creating a Dictionary
# car = {
#     'brand': 'Mercedes',
#     'model': 'AMG GTR',
#     'year' : '2021',
#     'inStock': True
# }

# # Accessing values by its key
# print(car['brand'])

# # Adding new key-value pairs
# car['cost'] = '$980000'
# print(car)

# # Modifying values
# car['model'] = 'G-Wagon'
# print(car)


# print("""
# Select your speed:
# slow    medium      fast
# """)

# squid_game = {
#     'start': 0,
#     'end': 99,
#     'speed': input('Speed: ').lower()
# }


# if squid_game['speed'].lower() == 'slow':
#     start_increment = 2

# elif squid_game['speed'].lower() == 'medium':
#     start_increment = 4

# elif squid_game['speed'].lower() == 'fast':
#     start_increment = 6

# else:
#     start_increment = 0

# squid_game['start'] += start_increment

# print(squid_game)


# To access any value from dictionary
# we can use -- get(WHAT TO ACCESS BY KEY, RETURN STATEMENT IF KEY DOESNT EXIST )

# suv_showroom = {
#     'totoya': 'fortuner',
#     'ford': 'endeavour',
#     'mahindra': 'xuv700',
#     'mg': 'hector',
#     'hyundai': 'alcazar'
# }

# del suv_showroom['totoya']
# # print(suv_showroom)

# car_search = suv_showroom.get('totoya', 'We are not selling totoyas')
# print(car_search)

# car_search = suv_showroom.get('mercedes')
# print(car_search)

# suv_showroom['aston martin'] = 'DBX'
# print(suv_showroom)




# print(person_details)
# print(person_details['first_name'])
# print(person_details['last_name'])
# print(person_details['age'])
# print(person_details['city'])



# favorite_numbers = {
#     'joe': 77,
#     'max': 33,
#     'daniel': 3,
#     'lewis': 44,
#     'carlos': 55
# }

# print(f"Joe - {favorite_numbers['joe']}")
# print(f"Max - {favorite_numbers['max']}")
# print(f"Daniel - {favorite_numbers['daniel']}")
# print(f"Lewis - {favorite_numbers['lewis']}")
# print(f"Carlos - {favorite_numbers['carlos']}")




# print(f"Tuples - {glossary.get('tuples')}")
# print(f"Dictionary - {glossary.get('dictionaries')}")
# print(f"Lists - {glossary.get('lists')}")
# print(f"Boolean - {glossary.get('boolean')}")
# print(f"String - {glossary.get('strings')}")




# items() - returns the list of key/value pairs
# keys()

# employee = {
#     'first_name': 'joe',
#     'last_name': 'goldberg',
#     'user_name': 'pyschoKiller',
#     'designation': 'Book Keeper',
#     'city': 'Madre Linda'
# }

# # Looping through all key/value pairs in dict. 
# for key, value in employee.items():
#     print(f"{key.upper()}: {value.title()}")


# gamer_scores = {
    
#     'ninja': 215,
#     'akita': 222,
#     'xenbo': 315,
#     'ramudu': 345

# }

# # Looping through all the keys in a dict.
# # for key in gamer_scores.keys():
# #     print(key.title())

# for key in gamer_scores.keys():
#     if key == 'ninja':
#         gamer_scores['ninja'] += 50

# print(gamer_scores)


# favorite_languages = {

#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'java',
#     'dorm': 'python'

# }

# # # Looping through only values in dict. using values()
# # for value in favorite_languages.values():
# #     print(value.title())

# # Set is collection of values in which each item is unique
# lang_values = set(favorite_languages.values())

# for language in sorted(lang_values):
#     print(language.upper())

# this_is_list = ['el1', 'el2'] 
# this_is_tuple = ('el1', 'el2')
# this_is_set  = {'el1', 'el2', 'el3'}
# this_is_dictionary = {
#     'no_1': 'el1',
#     'no_2': 'el2'
# }

# glossary = {
#     'tuples': 'stores collection of data which cannot modified',
#     'dictionaries': 'uses key/value pair to access',
#     'lists': 'Collection of values',
#     'boolean': 'conditional test',
#     'strings': 'sequence of characters'
# }

# for key, value in glossary.items():
#     print(f"{key.title()}: {value.title()}")


# rivers = {
#     'nile': 'egypt',
#     'brazil': 'amazon',
#     'missouri': 'united states',
#     'congo': 'africa'
# }

# for river, country in rivers.items():
#     print(f"The river {river.title()} flows through {country.title()}")

# print('\n')

# for river in rivers.keys():
#     print(river)

# print('\n')

# for country in rivers.values():
#     print(country)


# movies = {

#     'Venom': {
#         'title': 'Venom 2',
#         'subtitle': 'Let there be carnage',
#         'year_released': 2021,
#         'rating': 3.8,
#         'verdict': 'average',
#         'genre': 'fiction'
#     },

#     'shang-chi': {
#         'title': 'shang-chi',
#         'subtitle': 'The power of ten rings',
#         'year_released': 2021,
#         'rating': 4.6,
#         'verdict': 'hit',
#         'genre': 'fiction'
#     },

#     'james bond': {
#         'title': 'James Bond',
#         'subtitle': 'No Time to Die',
#         'year_released': 2021,
#         'rating': 4.5,
#         'verdict': 'average',
#         'genre': 'action'
#     }

# }

# for movie, data in movies.items():
#     print(f"{movie.upper()} \n {data}\n")


# persons = []

# person_0 = {
#     'name': 'ikaris',
#     'type': 'celestial',
#     'origin': None,
#     'age': 'eternal'
# }

# persons.append(person_0)

# person_1 = {
#     'name': 'sersei',
#     'type': 'celestial',
#     'origin': None,
#     'age': 'eternal'
# }

# persons.append(person_1)

# person_2 = {
#     'name': 'thena',
#     'type': 'celestial',
#     'origin': None,
#     'age': 'eternal'
# }

# persons.append(person_2)

# person_3 = {
#     'name': 'kingo',
#     'type': 'celestial',
#     'origin': None,
#     'age': 'eternal'
# }

# persons.append(person_3)

# person_4 = {
#     'name': 'makkari',
#     'type': 'celestial',
#     'origin': None,
#     'age': 'eternal'
# }

# persons.append(person_4)

# for person in persons:
#     name = person['name'].title()
#     type_of_person = person['type'].title()
#     age = person['age'].title()

#     print(f"{name} is a {type_of_person}, aged {age} years from the beginning of earth")


# pets = []

# pet_0 = {
#     'name': 'bono',
#     'type': 'dog',
#     'breed': 'beagle'
# }
# pets.append(pet_0)

# pet_1 = {
#     'name': 'sher',
#     'type': 'dog',
#     'breed': 'hound'
# } 
# pets.append(pet_1)

# pet_2 = {
#     'name': 'hami',
#     'type': 'dog',
#     'breed': 'husky'
# } 
# pets.append(pet_2)


# pet_3 = {
#     'name': 'sam',
#     'type': 'dog',
#     'breed': 'chow-chow'
# } 
# pets.append(pet_3)

# for pet in pets:
#     name = pet['name'].title()
#     animal_type = pet['type'].title()
#     breed = pet['breed'].title()

#     for key, value in pet.items():
#         print(f"{key.title()}: {value.title()}")
    
# favorite_places = {
#     'ikaris': ['taj mahal', 'ajanta', 'mt. fuji'],
#     'thena': ['tokyo national museum', 'peace park', 'golden gai'],
#     'makkari': ['nagoro','tokyo','senso-ji']
# }

# for key, value in favorite_places.items():
#     print(f"{key.title()} likes the following places:")

#     for place in value:
#         print(f"- {place.title()}")

#     print('\n')

    
# favorite_numbers = {
#     'ikaris': [1, 2, 99, 55],
#     'sersei': [22, 5, 88, 3],
#     'ajak': [3, 44, 77, 17],
#     'kingo': [92, 52, 62, 11]
# }

# for name, numbers in favorite_numbers.items():
#     print(f"{name.title()} likes the following numbers:")

#     for number in numbers:
#         print(f"-> {str(number)}")

#     print('\n')


# cities = {
#     'hyderabad': {
#         'country': 'India',
#         'population': '556600',
#         'located': 'telangana'
#     },

#     'bangalore': {
#         'country': 'India',
#         'population': '666600',
#         'located': 'karnataka'
#     },

#     'chennai': {
#         'country': 'India',
#         'population': '5800056',
#         'located': 'tamilnadu'
#     } 
# }

# for city, city_info in cities.items():
#     country = city_info['country'].title()
#     population = city_info['population']
#     location = city_info['located'].title()

#     print(f"\n{city.title()} is in {country}")
#     print(f" It has a population of about {str(population)}")
#     print(f" Located in {location}")

# # Dictonaries syntax
# #------------------------------------------------------------------------------------------------

# dimensions = {
#     'x': 200,
#     'y': 400
# }

# for key, value in dimensions.items():
#     print(key, value)

# dimensions = dict(x=200, y=400)

# d_points = [(key, value) for key, value in dimensions.items()]
# print(d_points)

# print(dimensions.get("x"))


# Dictionary Comphrension
# ------------------------------------------------------------------------------------------------
# dimensions = {key: key *34 for key in range(1, 5)}
# print(dimensions)

# squares = {key: key * key for key in range(1, 11)}
# print(squares)

# Comphrension way of writing logic works for lists, sets, dictionaries but not for tuples bcoz its immutable behaviour.
# We can iterate over tuples but they cannot be modified. They memory efficient when creating large datasets
#Its advisable to use generator expression(tuples) when working with larger data sets

from sys import getsizeof

cubes = (key * key * key for key in range(100))

# for key in cubes:
#     print(key)

print("gen. size of tuple: ", getsizeof(cubes))

cubes = [key * key * key for key in range(100)]
print("gen. size of list: ", getsizeof(cubes))