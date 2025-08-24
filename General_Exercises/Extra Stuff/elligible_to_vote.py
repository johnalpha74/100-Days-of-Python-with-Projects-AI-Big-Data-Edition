'''
Author: John Alpha
Purpose: This code checks if a user is eligible to vote based on their age and citizenship status.
Date: 2023-10-01
Version: 1.0
# eligible_to_vote.py
'''

def is_eligible_to_vote(age, is_citizen):
    """
    Check if a user is eligible to vote based on their age and citizenship status.
    
    Parameters:
    age (int): The age of the user.
    is_citizen (bool): True if the user is a citizen, False otherwise.
    
    Returns:
    bool: True if the user is eligible to vote, False otherwise.
    """
    if age >= 18 and is_citizen:
        return True
    else:
        return False
def main():
    """
    Main function to interact with the user and check voting eligibility.
    """
    try:
        age = int(input("Please enter your age: "))
        is_citizen_input = input("Are you a citizen? (yes/no): ").strip().lower()
        is_citizen = is_citizen_input == 'yes'
        
        if is_eligible_to_vote(age, is_citizen):
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        