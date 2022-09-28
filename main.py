secret_number=5
trial_counter=0
trial_limit=3
while trial_counter <trial_limit:
    Guessing_number=int(input("Guess:"))
    trial_counter = trial_counter + 1
    if Guessing_number == secret_number:
        print("you won")
        break

else:
     print("trial limit reached")




