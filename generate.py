import random
import string

num_letters = int(input("How much generate number: "))

def generate_random_letters(num_letters):
    letters = ''.join(random.choices(string.ascii_uppercase, k=num_letters))
    return letters

num_to_generate = int(input("Combination letter: "))

results = [generate_random_letters(3) for _ in range(num_to_generate)]

filename = "random_letters.txt"
with open(filename, "w") as file:
    file.write("\n".join(results))

print(f"Success Save to '{filename}'.")
