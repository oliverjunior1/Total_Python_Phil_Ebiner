capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

for x, y in zip(capitals, countries):
    print(f"The capital of {y} is {x}")