# Implementing a stack

browsing_session = []

# pushing the items to stack
browsing_session.append('page1')
browsing_session.append('page2')
browsing_session.append('page3')
browsing_session.append('page4')
print(f"Visited pages: {browsing_session}")


# popped items from stack
browsing_session.pop()
browsing_session.pop()
browsing_session.pop()

print(f"Pages after exited pages: {browsing_session}")


# # peeking for top element
# top = browsing_session[-1]
# print(top)

# Checking whether stack is empty
if not browsing_session:
    print(browsing_session[-1])

