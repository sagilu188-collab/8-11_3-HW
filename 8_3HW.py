import random
def get_lucky_numbers(amount: int) -> tuple[int]:
    lucky_list = []
    for i in range(amount):
        lucky_list.append(random.randint(1, 100))
    return tuple(lucky_list)


def input_until_lucky(lucky_numbers: tuple) -> int:
    attemps = 0
    gussed_correct = False
    print(f"(DEBUG) The lucky numbers are: {lucky_numbers}")

    while not gussed_correct:
        player_input = input("Enter a number between 1 and 100: ")
        try:
            guess = int(player_input)
            attemps += 1
            if guess in lucky_numbers:
                print("Lucky number:", guess)
                gussed_correct = True
            elif guess > 100 or guess < 1:
                print("invalid input:")
            else:
                print("failed")

        except ValueError:
            print("invalid input")
    return attemps


lucky_numbers = get_lucky_numbers(3)
total_attemps = input_until_lucky(lucky_numbers)
print(f"tottal attempts:{total_attemps} lucky numbers are {lucky_numbers}")

