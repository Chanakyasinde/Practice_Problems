class Restaurant:
    def __init__(self):
        self.menu = {}

    def add_item(self, name, price):
        self.menu[name] = price
        print("Item added/updated successfully")

    def remove_item(self, name):
        if name in self.menu:
            del self.menu[name]
            print("Item removed successfully")
        else:
            print("Item not found")

    def display_menu(self):
        if not self.menu:
            print("The menu is empty.")
        else:
            print("Menu:")
            for item, price in self.menu.items():
                print(f"{item}: {price}")

item1 = input().split()
item2 = input().split()
item3 = input().split()
item = input()

name1, price1 = item1[0], int(item1[1])
name2, price2 = item2[0], int(item2[1])
name3, price3 = item3[0], int(item3[1])

restaurant = Restaurant()
restaurant.add_item(name1, price1)
restaurant.add_item(name2, price2)
restaurant.add_item(name3, price3)
restaurant.remove_item(item)
restaurant.display_menu()
