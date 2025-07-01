s = "mcdonald's burger"
print(s.title())  # Output: "Mcdonald'S Burger"  s is also become in capital letter.

def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))    # Avoid title() quirks.
s = solve(s)
print(s)
#After that "S" will become to "s"...............................