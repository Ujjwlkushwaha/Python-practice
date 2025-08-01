# Problem 1: Suggest a mode of transport based on distance

distance = float(input("Enter the distance to your destination (in km): "))

if distance <= 2:
    print("You can walk.")
elif distance <= 10:
    print("Use a bicycle or scooter.")
elif distance <= 50:
    print("Take a car or public transport.")
else:
    print("Consider a train or flight.")

    