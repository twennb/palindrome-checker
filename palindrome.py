"""A program that checks whether a word or sentence is a palindrome"""
# plan:
# get user input to check as palindrome
# see if input == backwards input
# if not, not a palindrome
# if yes, palindrome
# ask to check another input or exit
import sys


def get_user_input():
    """gets input from user that they wish to check for palindrome"""
    print("=================================")
    while True:
        validation_list = []
        palindrome_input = input(
            "Enter a word or message that you want to find out whether it is a palindrome or not\n-: ")
        for character in palindrome_input:
            if character.isalpha() or character.isspace():
                pass
            else:
                validation_list.append(character)
        if not validation_list:
            break
        print("Invalid input! Please only enter letters and spaces.")
    return palindrome_input.strip()


def reverse_input(palindrome_input):
    """reverses the user's input"""
    palindrome_reverse = palindrome_input[::-1]
    return palindrome_reverse.strip()


def check_palindrome(normal, reverse):
    """checks whether a passed input is the same backwards as forwards"""
    if normal.lower() == reverse.lower():
        print(f"\nYour input '{normal}' is a palindrome!")
    else:
        print(f"\nYour input '{normal}' is not a palindrome!")


def check_again():
    """asks the user if they want to check another input"""
    while True:
        user_choice = input(
            "Would you like to check a different input? (yes/no)\n-: ")
        if user_choice == "yes":
            main()
        elif user_choice == "no":
            print("\nGoodbye!\n")
            sys.exit()
        else:
            print("Invalid input!")


def main():
    """the main function"""
    potential_palindrome = get_user_input()
    reverse_palindrome = reverse_input(potential_palindrome)
    check_palindrome(potential_palindrome, reverse_palindrome)
    check_again()


if __name__ == "__main__":
    main()
