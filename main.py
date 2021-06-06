
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

# is_continue = True
# while is_continue:
#     word = input("Enter a word: ").upper()
#     if word == "EXIT" or word == 'QUIT':
#         is_continue = False
#     else:
#         output_list = [nato_dict[letter] for letter in word]
#         print(output_list)


def generate_nato_dict():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_nato_dict()
    else:
        print(output_list)


generate_nato_dict()
