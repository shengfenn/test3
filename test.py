print('hello')
smallest = None
for value in [12,45,90,67,23,10,38,89,90,38]:
  if smallest is None:
    smallest = value
  elif value<smallest:
    smallest = value
print(smallest)
