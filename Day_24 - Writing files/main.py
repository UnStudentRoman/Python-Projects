# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Getting the names
with open("./Input/Names/invited_names.txt") as names:
    name_list = names.read().splitlines()

# Getting the letter format
with open("./Input/Letters/starting_letter_2.docx", encoding="UTF-8") as letter:
    letter_text = letter.read()

# Generating letters
for name in name_list:
    letter_named = letter_text.replace("[name]", f"{name}")
    with open(f"./Output/ReadyToSend/Letter_for_{name}.docx", mode="w") as final_letter:
        final_letter.write(letter_named)
