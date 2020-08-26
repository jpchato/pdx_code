'''
Create a dictionary of fruits. The name of each fruit will be the key and the value will be its price.

1.1
Using the fruits dictionary:

Display the price of a fruit
Add a fruit to the dictionary, print the dictionary to verify its creation
Remove a fruit from the dictionary, print the dictionary to verify its deletion

1.2
Loop through the dictionary and display each item and its price.

1.3
Create another dictionary to represent a shopping_basket.

The keys of this dictionary will be fruit names and the values will be the quantity of each item in the shopping_basket.

Loop through the shopping_basket and add up the grand_total. With each iteration of the loop, also print out how many of each fruit are in the shopping_basket and the sub_total for that fruit.

Display all the sub_totals and the grand_total to look like a receipt in the terminal.
'''



def display_fruit():
    fruits = {'apple': 0.50, 'banana': 0.60, 'orange': 0.70}
    print('The fruits in the list are ' + str(fruits.keys()))
    print('The price of an apple is ' + str(fruits.get('apple')))
    fruits.update({'peaches': 0.99})
    print(fruits)
    fruits.pop('banana')
    print('banana has been removed from the list')
    print(fruits)

    for fruit in fruits.items():
        print(fruit)

    shopping_basket = {'apple': 1, 'peaches': 2, 'orange': 3}
    total = 0
    for fruit in shopping_basket:
        quantity = shopping_basket[fruit]
        sub_total = quantity * fruits[fruit]
        total += sub_total
        print(f'{quantity} {fruit.capitalize()}s: ${sub_total}')
    print(f'The total is: ${total}')
        
        
    

if __name__ == "__main__":
    display_fruit()