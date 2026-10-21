days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
prepared_meals = [100, 120, 90, 110, 100]
served_meals = [92, 100, 85, 90, 70]
threshold = 10

for i in range(len(days)):
    prepared = prepared_meals[i]
    served = served_meals[i]

    if prepared <= 0 or served < 0 or served > prepared:
        print(days[i], "- Invalid meal counts")
    else:
        leftovers = prepared - served
        waste_percent = leftovers / prepared * 100
        print(days[i], "leftovers:", leftovers,
              "wastage:", round(waste_percent, 2), "%")
        if waste_percent > threshold:
            print("  Warning: Wastage exceeded", threshold, "%")
