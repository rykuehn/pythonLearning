my_list = [4, 5, 6, "hi", "bye", [4,0]]
my_list.append(100) #only for one item
my_list.extend(["s", "d", "k"]) # for multiple items
my_list.append([0, 0, 0])

#for loop
for item in my_list:
  if type(item) is int:
    print(item)
#while loop
