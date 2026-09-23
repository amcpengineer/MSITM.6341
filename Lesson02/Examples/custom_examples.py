fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.append("apple")
fruits.remove("banana")
print("List:", fruits)

# Example of a list
l1 = ['RAG', 'is', 'awesome']
print(f"Original list: {l1}")

# Adding an item
l1.append('!')
print(f"List after adding '!': {l1}")

# Removing an item
l1.remove('awesome')
print(f"List after removing 'awesome': {l1}")

# .remove and .append change the list and have no return
result = l1.append("this is a test")
print(result)
print(l1)