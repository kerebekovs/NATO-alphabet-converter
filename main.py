import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

new_data = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_nato():
    word = input('Plese type the word: ').upper()

    try:
        res = [new_data[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet')
        generate_nato()
    else:
        print(res)

generate_nato()