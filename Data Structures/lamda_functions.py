list = [
    ('Product1', 15),
    ('Product2', 20),
    ('Product3', 2),
    ('Product4', 6),
    
]

# def sort_list(item):
#     return item[1]


# list.sort(key=sort_list)
# print(list)

list.sort(key=lambda item:item[1])
print(list)