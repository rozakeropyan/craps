from random import randint

def main():
    while True:
        # Roll two dice
        number_1 = randint(1,6)
        number_2 = randint(1,6)
        sum = number_1 + number_2
        # Check if player wins instantly
        if (sum == 7 or sum == 11):
            print("The sum of dice is {} + {} = {}".format(number_1, number_2, sum))
            print("You Won")
            print("========")
            break
        # Check if player casino wins instantly
        elif sum in (2,3,12):
            print("The sum of dice is {} + {} = {}".format(number_1, number_2, sum))
            print("Casino wins")
            print("========")
            break
        # If neither instant win nor loss, set the goal number
        elif sum in (4,5,6,8,9,10):
            print("The sum of dice is {} + {} = {}".format(number_1, number_2, sum))
            print("Now your goal number is: {}".format(sum))
            # Keep rolling until player wins or loses
            while True:
                num1 = randint(1,6)
                num2 = randint(1,6)
                sum_2 = num1 + num2
                print("The sum of dice is {} + {} = {}".format(num1, num2, sum_2))
                # Check if player loses
                if (sum_2 == 7):
                    print("You lose")
                    print("========")
                    break
                # Check if player wins
                elif(sum == sum_2):
                    print("You won")
                    print("========")
                    break
        else:
            continue

main() # Call the main function to start the game


