import requests
import random

def start():
    print('Continuing or not (y/n)')
    while True:
        flag = input()
        if flag == 'y':
            return True
        if flag == 'n':
            return False


def get_number():
    url = 'https://python666.cn/cls/number/guess/'
    try:
        r = requests.get(url)
        res = int(r.text)
    except:
        res = random.randint(1, 100)
    return res


def play():
    print('play...')
    print('target is initialing...')
    target = get_number()
    count = 1
    while True:
        while True:
            print("Please keyboard your  {}'s round answer (1-100) (type: int)".format(count))
            try:
                num = int(input())
                if num <= 100 and num >= 1:
                    break
                else:
                    print('input must in [1, 100]')
            except Exception as e:
                print('error: {}'.format(e))
                print('retry your answer')

        if num == target:
            print('equals')
            break
        elif num > target:
            print('your num bigger')
        else:
            print('your num smaller')
        count += 1
    return count


def update_log(player_dict, player, count):
    if player not in player_dict:
        print('append new user')
        player_dict[player] = [1, count, count, count]
        with open('user.txt', 'a', encoding='utf-8') as fw:
            string = '\t'.join([player, str(1), str(count), str(count), str(count)])
            fw.write(string + '\n')
    else:
        print('modified user info')
        times = int(player_dict[player][0])
        total = int(player_dict[player][1])
        min_  = int(player_dict[player][2])
        mean  = float(player_dict[player][3])

        player_dict[player] = [str(times+1), str(total+count), str(min(min_, count)), str((total+count)/float(times+1))]

        with open('user.txt', 'w', encoding='utf-8') as fw:
            for k, v in player_dict.items():
                s = v
                s.insert(0, k)
                s = '\t'.join(v)
                fw.writelines(s + '\n')


if __name__ == '__main__':
    player = input('Please input your name, ')
    player_dict = {}
    try:
        with open('user.txt', 'r', encoding='utf-8') as fr:
            lines = fr.readlines()
    except:
        open('user.txt', 'w', encoding='utf-8')     # create user.txt
        lines = []

    for line in lines:
        user_info = line.strip().split('\t')
        player_dict[user_info[0]] = user_info[1:]

    if player in player_dict:
        print('{}, play {} times, minimum times {}, mean times {}'.format(player,
                                                                          player_dict[player][0],
                                                                          player_dict[player][2],
                                                                          player_dict[player][3]))
    else:
        print('{}, play 0 times, minimum times 0, mean times 0'.format(player))

    while True:
        if not start():
            print('See you again')
            break
        count = play()
        update_log(player_dict, player, count)
