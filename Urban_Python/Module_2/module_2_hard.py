import random


def get_first_pillar():
    num = random.choice(list(range(3, 21)))
    return num


def check_password(n):
    pass_dict = {}
    pass_dict.update(
        {3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645, 10: 141923283746, 11: 11029384756})
    pass_dict.update(
        {12: 12131511124210394857, 13: 112211310495867, 14: 1611325212343114105968, 15: 1214114232133124115106978})
    pass_dict.update(
        {16: 1317115262143531341251161079, 17: 11621531441351261171089, 18: 12151811724272163631545414513612711810})
    pass_dict.update({19: 118217316415514613712811910, 20: 13141911923282183731746416515614713812911})
    password = pass_dict.get(n)
    return password


first_pillar = get_first_pillar()
print("First pillar: ", first_pillar)

pair_list = []
result = ''

num_1 = list(range(1, first_pillar))
num_2 = list(range(1, first_pillar))

for i in num_1:
    for j in num_2:
        if i >= j:
            continue
        else:
            if first_pillar % (i + j) == 0:
                pair_list.append([i, j])
                result += str(i) + str(j)

print("Pairs: ", pair_list)
print("Second pillar:", result)
if int(result) == check_password(first_pillar): print("Password matches!")