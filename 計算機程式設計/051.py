inp = input().split('|')
banned = inp[1].split(',')
paragraph = inp[0].lower()
paragraph_check = ''
for i in range(len(paragraph)):
    if paragraph[i].isalpha() or paragraph[i] == ' ':
        paragraph_check += paragraph[i]
paragraph = paragraph_check.split()
paragraph_max = ''
n_max = 0
for i in range(len(paragraph)):
    if paragraph[i] in banned:
        continue
    else:
        if paragraph.count(paragraph[i]) > n_max:
            n_max = paragraph.count(paragraph[i])
            paragraph_max = paragraph[i]
print(paragraph_max)