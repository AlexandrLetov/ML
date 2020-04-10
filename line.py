test_line = 'ffjfkldjflfajlkldlslslsldjfklasdjflaadl'
new_line = ''

for letter in test_line:
    if letter not in new_line:
        new_line = new_line + letter

print(new_line)
