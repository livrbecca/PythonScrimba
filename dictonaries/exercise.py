# Exercise

freelancers = {'name': 'freelancing Shop', 'brian': 70, 'black knight': 20,
               'biccus diccus': 100, 'grim reaper': 500, 'minstrel': -15}
antiques = {'name': 'Antique Shop', 'french castle': 400,
            'wooden grail': 3, 'scythe': 150, 'catapult': 75, 'german joke': 5}
pet_shop = {'name': 'Pet Shop', 'blue parrot': 10,
            'white rabbit': 5, 'newt': 2}

# create an empty shopping cart
cart = {}
purse = 1000
buy_items1 = ""

# loop through stores/dicts


for shop in (freelancers, antiques, pet_shop):
    buy_item = input(
        f'Welcome to {shop["name"]}! what do you want to buy: {shop}: ').lower()
    if buy_item == "exit":
        continue
    if buy_item not in shop:
        continue
    # ask isabel where / how the money value is being picked up
    buy_items1 = buy_items1 + f'{buy_item}:{shop[buy_item]} gold pieces, '
    cart.update({buy_item: shop.pop(buy_item)})
    buy_items = ", ".join(list(cart.keys()))
    total_sum = sum(cart.values())
print(f'You Purchased {buy_items1} Your total is {total_sum} gold pieces. Your change is {purse - total_sum} gold pieces. Have a nice day of mayhem!')
