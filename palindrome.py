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
    # palindrome_input: the user's input from get_user_input()
    palindrome_reverse = palindrome_input[::-1]
    return palindrome_reverse.strip()


def clean_input(normal, reverse):
    """this function removes spaces in the input and makes everything lowercase to prepare for comparison"""
    # normal: the user's input
    # reverse: reversed input from reverse_input()
    cleaned_normal = normal.replace(" ", "")
    cleaned_reverse = reverse.replace(" ", "")

    return cleaned_normal.lower(), cleaned_reverse.lower()


def check_palindrome(normal, reverse, original):
    """checks whether a passed input is the same backwards as forwards"""
    # normal: the cleaned user input
    # reverse: the cleaned reverse user input
    # original: the actual user input
    if normal == reverse:
        print(f"\nYour input '{original}' is a palindrome!")
    else:
        print(f"\nYour input '{original}' is not a palindrome!")


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
    cleaned_normal, cleaned_reverse = clean_input(
        potential_palindrome, reverse_palindrome)
    check_palindrome(cleaned_normal, cleaned_reverse, potential_palindrome)
    check_again()


if __name__ == "__main__":
    main()
