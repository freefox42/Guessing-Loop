secret = "lala"
guess = ""
count = 0
limit = 3
out = False

while guess != secret and not(out):
    if count < limit:
        guess = input("Guess: ")
        count += 1
    else:
        out = True
if out:
    print("LOSE!")
else:
    print("WIN!")