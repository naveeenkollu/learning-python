class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Name of the restaurant is {self.name} and serves best {self.cuisine} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")

    def customers_served(self):
        print(f"No. of customers served: {self.number_served}\n")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, customers):
        self.number_served += customers

# # 9.1
# restaurant = Restaurant('Malgudi', 'South Indian')
# print(restaurant.name)
# print(restaurant.cuisine)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# # 9.2
# restaurant_1 = Restaurant('Kohinoor', 'Indian')
# restaurant_1.describe_restaurant()

# restaurant_2 = Restaurant('Taj Vivanta', 'Indo-Asian')
# restaurant_2.describe_restaurant()

# restaurant_3 = Restaurant('Taj Krishna', 'Indo-Asian')
# restaurant_3.describe_restaurant()


# 9.4
restaurant = Restaurant('Hyatt', 'Indo-Mexican')
print(f"Number of customers served: {restaurant.number_served}")
restaurant.number_served = 5
print(f"Number of customers served: {restaurant.number_served}")


restaurant.set_number_served(10)
restaurant.customers_served()

restaurant.increment_number_served(8)
restaurant.customers_served()