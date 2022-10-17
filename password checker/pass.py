password = input("Enter your password\n")
score = 0

# check if password has both uppercase and lowercase characters
lowercase = False
uppercase = False

for character in password:
    if character in "abcdefghijklmnopqrstuvwxyz":
        lowercase = True
    elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase = True

# check if password  has number or not
num = False
for character in password:
    if character in "0123456789":
        num = True

# check if password has any special character or not
spl = False
for character in password:
    if character in "!@#$%^&*=-+_?":
        spl = True

if lowercase == True and uppercase == True:
    score += 10
if num == True and (lowercase == True or uppercase == True):
    score += 10
if spl == True:
    score += 5
if len(password) >= 8:
    score += 5

print("Score: " + str(score) + " out of  30")