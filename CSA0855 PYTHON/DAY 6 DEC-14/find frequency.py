
elements = input("Enter elements separated by space: ").split()
frequency = {element: elements.count(element) for element in set(elements)}


for element, count in frequency.items():
    print(f"{element}: {count}")
