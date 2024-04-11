from random import randint

def main():
    while True:
        number_1 = randint(1,6)
        number_2 = randint(1,6)
        sum = number_1 + number_2
        if (sum == 7 or sum == 11):
            print("The sum of dice is {} + {} = {}".format(number_1, number_2, sum))
            print("You Won")
            print("========")
            break
        elif sum in (2,3,12):
            print("The sum of dice is {} + {} = {}".format(number_1, number_2, sum))
            print("Casino wins")
            print("========")
            break
        elif sum in (4,5,6,8,9,10):
            print("The sum of dice is {} + {} = {}".format(number_1, number_2, sum))
            print("Now your goal number is: {}".format(sum))
            while True:
                num1 = randint(1,6)
                num2 = randint(1,6)
                sum_2 = num1 + num2
                print("The sum of dice is {} + {} = {}".format(num1, num2, sum_2))
                if (sum_2 == 7):
                    print("You lose")
                    print("========")
                    break
                elif(sum == sum_2):
                    print("You won")
                    print("========")
                    break
        else:
            continue

main()


