from tkinter.messagebox import YES
from IPython.display import clear_output as co 


class Cart:
    def __init__(self):
        self.items = []

    def choices_list():
        for i in choices:
         print(i)    

    choices = []

    def add_items(self, item_added):
       self.items.append(item_added)

    # add_to_cart = input("Would you like to add items to your cart? Yes or No ").lower()
    # Stores user input into a list
    # if add_to_cart == 'yes':
    # add_items = input("Which items would you like to add?").lower()

        #   add_items = input("Which items would you like to add?").lower()
    # while add_items == 'yes':
    #     print("Would you like to add more items? Yes or No ").lower()
    #     #  add_items == 'yes':
    #     add_items.append()
        #   break
        # print("Would you like to add more items?")
        #   add_items = (choices).append
    # else:
    #     print("Thank you for shopping with us!")
# done = True
# User can add or delete items
    def delete_items(self, item_name):
        for the_item in self.items:
            if the_item.name == item_name:
                self.items.remove(the_item)
# delete_items = input("Would you like to delete any items? Yes or No ").lower()                                                                                                                                                   
# if  delete_items == 'y':
#         print("Which items would you like to delele? ")
#         delete_items.pop()
                
   
# delete_choices = input("Which items would you like to delete?").lower()
# delete.items.remove
#     print("Your itmes have been deleted.")

#     # delete_choices.remove

#             if delete_items == 'n':
#              done = True