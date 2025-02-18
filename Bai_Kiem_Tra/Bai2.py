character_statistic = {}

word = 'Thay Minh Dep Trai'
for character in word:
    if character in character_statistic:
        character_statistic[character] += 1
    else:
        character_statistic[character] = 1
print(character_statistic)