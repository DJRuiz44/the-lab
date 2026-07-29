guests = ["Einstein", "Socrates", "Jesus"]
print(f'Dinner will be fantastic with {guests[0]}, {guests[1]}, and {guests[2]}')

print(guests.pop(0))
print(guests)

guests.append("Captain Falcon")
print("A new challenger is approaching!!!!")
print(f'{guests[-1]} has entered the battle!')

print("New dinner guests")
print(guests)

print("3 new spots just opened up")
print("Lets sit everyone out evenly")
guests.insert(0, "Dom Mazetti") 
guests.insert(2, "Frenzi") 
guests.insert(len(guests)-1, "Thrall") 

print(f'WOW we have {len(guests)} guests coming to dinner')

print("New guests list")
print(guests)

print("Whoops I only have two seats")

while len(guests) > 2:
    guest_removed = guests.pop(0)
    if guest_removed == "Jesus":
        guests.append(guest_removed)
        print("Sorry this is a must have")

print(guests)
del guests[0]
print(guests)
print("Amen")
