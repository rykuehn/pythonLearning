shopping_list = [];
print("What should we pick up at the store?");
print("enter DONE when complete");

while True:
  new_item=input("> ");
  if new_item == "DONE":
    break
  shopping_list.append(new_item);

print("Here is your list");
print(shopping_list)