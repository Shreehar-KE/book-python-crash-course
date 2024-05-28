"""
3-10. Every Function: Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you'd like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once.
"""

locations = ['svalbard', 'paris', 'maldives', 'venice', 'ha long bay']
print(locations)
print()
locations.append('santorini')
print(locations)
print()
locations.insert(1, 'switzerland')
print(locations)
print()
del locations[5]
print(locations)
print()
locations.insert(5, 'ha long bay')
print(locations)
print()
print(sorted(locations))
print()
print(locations)
print()
locations.sort()
print(locations)
print()
locations.reverse()
print(locations)
print()
print(len(locations))
print()
print(locations.pop())
print(locations)
print()
print(locations.pop(2))
print(locations)
print()
locations.remove('paris')
print(locations)
print()
