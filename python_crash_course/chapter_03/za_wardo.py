to_visit = ["Pamplona", "Makinaw", "Kyoto", "Fuji", "Everest"]

print(to_visit)
print(f'Sorted: {sorted(to_visit)}')
print(to_visit)
to_visit.reverse()
print("ZA WARDO!!!!!!!!!! \n THIS CHANGE WAS IN PLACE")
print(to_visit)

to_visit.sort()
print("Sort() callign in place as well")
print(to_visit)

print("Attempting reversal")
to_visit.sort(reverse=True)
print(to_visit)
