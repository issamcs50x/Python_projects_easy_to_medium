import re

# open and reading the text file while handling the File Not Found case
def txt_read(txt_filename):
    try:
        with open(txt_filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

# Ensure that the user has entered a valid answer.
def validate_input(msg):
    while True:
        value = input(msg).strip().lower()
        if len(value) > 1:
            return value
        else:
            print("Invalid input")

# diplaying the text with placeholders
print("-" * 5, "Before", "-" * 5)
text = txt_read("madlibs.txt")
print(text)

# Split the text into placeholders and the rest of the texts
slices = re.split(r"\[|\]", text)
print(slices)

# Searching for placeholders: any word enclosed in square brackets
placeholders = re.findall(r"\[(\w+)\]", text)


# replacing placeholders with values
for index, slice in enumerate(slices):
    if slice in placeholders:
        value = validate_input(slice + ": ")
        slices[index] = value
    

# displaying the text again with real values
print("-" * 5, "After", "-" * 5)
print("".join(slices))


# simple implementation
story = "Last summer, [person_name] and their best friend [friend_name] decided to take a trip"

words = []
start_found = False
for i, char in enumerate(story):
    if char == "[":
        start_index = i + 1
        start_found = True
    elif char == "]" and start_found:
        words.append(story[start_index:i])
        start_found = False
    
madlibs = {placeholder:input(placeholder+": ") for placeholder in words}

for placeholder, answer in madlibs.items():
    story = story.replace(f"[{placeholder}]", answer,)

print(story)