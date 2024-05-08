from itertools import permutations

def main():

    user_input = input("Enter a string of characters: ")

   
    perm = permutations(user_input)
    print("\nPermutations:")
    for p in list(perm):
        print("".join(p))


main()
