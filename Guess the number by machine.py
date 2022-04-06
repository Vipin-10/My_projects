import random
def machine_guess(x):
    low = 0
    high = x
    feedback = ""
    while feedback != "correct" :
        if low != high :
            guess = random.randint(low , high)
        else :
            guess = low
        feedback = input(f"Is {guess} is low , high or correct ?")
        if feedback == "high" :
           high = guess - 1
        elif feedback == "low" :
            low = guess + 1
        else:
            feedback == "correct"

    print(f"Machine Guessed {guess} correctly")
machine_guess(1000)