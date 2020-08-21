street = input('What street do you live on ?')
city = input('What city do you live in?')
state = input('What state do you live in?')
zip = input('What\'s your zip code?')

street_upper = street.title()
city_upper = city.title()
state_upper = state.title()

response = ('{street}\n{city}\n + ',' + {state}\n{zip}')
print(f'''
{street_upper}
{city_upper}, {state_upper}
{zip}
'''
)