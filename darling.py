# darling 카운트
f = open("Darling.txt", 'r')
darling = f.readlines()
f.close()

contents = ""
for line in darling:
  contents = contents + line.strip() + "\n"

n_darling = contents.upper().count("DARLING")
print("Number of a World 'Darling'", n_darling)

# my 카운트
f = open("Darling.txt", 'r')
my = f.readlines()
f.close()

contents = ""
for line in my:
  contents = contents + line.strip() + "\n"

n_my = contents.upper().count("MY")
print("Number of a World 'my'", n_my)

# you 카운트
f = open("Darling.txt", 'r')
you = f.readlines()
f.close()

contents = ""
for line in you:
  contents = contents + line.strip() + "\n"

n_you = contents.upper().count("YOU")
print("Number of a World 'you'", n_you)