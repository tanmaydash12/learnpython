def funcargs(*args):
   for item in args:
       print(item, end=" ")



list2 = ["Tan", "Guddu", "Paaji", "Chinu"]

funcargs(*list2)