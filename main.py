import art
from game_data import data
import random
from replit import clear

#Hien thi doi tuong A va B
def display_format(obj1, obj2):
    """
    Display information of object 1 and 2 into printable format.
    """
    print(f"Compare A: {obj1['name']}, a {obj1['description']}, from {obj1['country']}.")
    print(art.vs)
    print(f"Against B: {obj2['name']}, a {obj2['description']}, from {obj2['country']}.")


#Chon ngau nhien doi tuong trong database   
def generator_obj():
    """
    Return a random object from game_data. 
    """
    obj = random.choice(data)
    return obj


def compare(obj1, obj2):
    """
    Compare follower_count of two object. Return Follower_count higher.
    """
    A_followers = obj1['follower_count']
    B_followers = obj2['follower_count']
    if A_followers > B_followers:
        return obj1
    else:
        return obj2


def main():
    print(art.logo)
    A = generator_obj()
    B = generator_obj()
    while A == B:
        B = generator_obj()
    list_used = [A, B]#Danh sach doi tuong da duoc dung. 
    score = 0
    is_lose = False
    while not is_lose:
        display_format(A, B)
        winner = compare(A, B)
        user_choose = input("Who has more follwers? Type 'A' or 'B': ").upper()
        clear()
        print(art.logo)
        if (winner == A and user_choose == "A") or (winner == B and user_choose == "B"):
            score += 1
            A = winner
            is_old = True
            while is_old:
                B = generator_obj()
                if B not in list_used:
                    is_old = False
            list_used.append(B)
            print(f"You're right. Current score: {score}.")
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {score}")
            is_lose = True


if __name__ == "__main__":
    main()