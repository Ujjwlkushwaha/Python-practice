# CONTROL FLOW STATEMENTS - Control flow statements like break, continue, and pass help manage how loops behave in specific conditions.


# 1. BREAK STATEMNET - exit the control from loops

n = 10

for num in range(n):
    if num == 5:
        print("We got 5, Now stop the loop !")
        break   # stop the loop when condition matches
    else:
        print(f"{num} is not equal to 5 5, Just ignored ! !")



# 2. CONTINUE STATEMENT - The continue statement skips the current loop iteration and moves to the next one.

# ex -1
n = 10 

while( n != 0 ):
    if n == 5:
        print("I ignored number 5")
        n-=1

        continue # return the control to starting of the loop

    print(n)
    n-=1

# ex - 2

items = ["milk", "bread", "out of stock", "eggs"]

for item in items:
    if item == "out of stock":
        continue
    print("Buy:", item)


# 3. pass STATEMENT - The pass statement does nothing. It’s a placeholder when the syntax requires a statement but no action is needed.

tasks = ["email", "meeting", "call"]

for task in tasks:
    if task == "call":
        pass  # Logic to be added later
    print("Do:", task)