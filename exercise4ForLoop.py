# create list and print if greater than 6 and is number 

list1 = ["Tom", 2, "Sigma", "Apple", 8, 23, "lion", 3, "Wood"]

for item in list1:
    if str(item).isnumeric() and item > 6:
        print(item)

