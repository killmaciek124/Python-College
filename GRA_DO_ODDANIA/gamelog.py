
def print_ranking(filepath):
    wins, plays = gamelog_parse(filepath)   
    top10 = topn(wins, plays, 10)
    print()
    print('RANKING')
    print()
    for player in top10:
        print('%s %d%%' % (player['player'], player['pcnt_won']))


def gamelog_parse(filepath):
    wins = {}
    plays = {}
    f = open(filepath)
    for line in f.readlines():
        player, has_won = line.split()
        player = player.lower()
        if player not in wins:
            wins[player] = 0
            plays[player] = 0
        wins[player] += int(has_won)
        plays[player] += 1
    f.close()
    return wins, plays


def gamelog_add(filepath, player, won):
    f = open(filepath, 'a')
    f.write('%s %d\n' % (player.lower(), int(won)))
    f.close()


def topn(wins, plays, n):
    score = []
    for player, num_won in wins.items():
        score.append({
            'player':   player,
            'pcnt_won': 100 * num_won / plays[player],
        })
    mysort(score)
    return score[:n]


def mysort(L):
    for i in range(1, len(L)):
        j = i-1 
        key = L[i]['pcnt_won']
        tmp = L[i]
        while j >= 0 and not L[j]['pcnt_won'] > key:
           L[j+1] = L[j]
           j -= 1
        L[j+1] = tmp
