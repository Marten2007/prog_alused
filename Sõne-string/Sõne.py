#1. Sõna-tüüpi muutujate deklareerimine
first_name = "James"
last_name = "Bond"

#2. Sõnade kujundamine - names
full_name = first_name + " " + last_name
self_description_sentence = f"My name is {last_name}, {first_name} {last_name}."

#3. Sõnade kujundamine - cake string
cake = "vahukoormarjadtäidispõhi"
print(cake.replace("täidis", "täidis\n").replace("marjad", "marjad\n").replace("vahukoor", "vahukoor\n"))

#4. Sõnade tükeldamine
original_string = "Programming is fun!"
backwards = original_string [::-1]
every_other = original_string [::2]
first_word_reversed = original_string.split()[0][::-1]

# Printimine
"""
print("1. Sõna-tüüpi muutujad:")
print(f"first_name: {first_name}"
print(f"last_name: {last_name}\n")

print("2. Sõnade kujundamine - names:")
print(f"full_name: {full_name}")
print(f"self_description_sentance: {self_description_sentance}\n")

print("3. Sõnade kujundamine - cake string:")
print(cake.replace("täidis", "täidis\n").replace("põhi", "põhi").replace("marjad"), "marjad\n").replace("vahukoor", "vahukoor"))

print("\n4. Sõnade tükeldamine:")
print(f"original_string: {original_string}")
print(f"backwards: {backwards}")
print(f"every_other: {every_other}")
print(f"first_word_reversed: {first_word_reversed}")
"""