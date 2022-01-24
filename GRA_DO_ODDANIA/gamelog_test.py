import os
from gamelog import gamelog_parse, topn, mysort

def test_gamelog_parse():
    f = open('testlog.txt', 'w')
    f.write('alice 1\n')
    f.close()

    wins, plays = gamelog_parse('testlog.txt')
    assert wins == {'alice': 1}
    assert plays == {'alice': 1}

    f = open('testlog.txt', 'w')
    f.write('alice 1\n')
    f.write('bob 1\n')
    f.close()

    wins, plays = gamelog_parse('testlog.txt')
    assert wins == {'alice': 1, 'bob': 1}
    assert plays == {'alice': 1, 'bob': 1}

    f = open('testlog.txt', 'w')
    f.write('alice 1\n')
    f.write('bob 0\n')
    f.write('alice 1\n')
    f.close()

    wins, plays = gamelog_parse('testlog.txt')
    assert wins == {'alice': 2, 'bob': 0}
    assert plays == {'alice': 2, 'bob': 1}

    f = open('testlog.txt', 'w')
    f.write('Alice 1\n')
    f.write('alice 1\n')
    f.close()

    wins, plays = gamelog_parse('testlog.txt')
    assert wins == {'alice': 2}
    assert plays == {'alice': 2}

    os.remove('testlog.txt')


def test_topn():
    wins = {}
    plays = {}
    top10 = topn(wins, plays, 10)
    assert top10 == []

    wins = {'alice': 1}
    plays = {'alice': 1}
    top10 = topn(wins, plays, 10)
    assert top10 == [{'player': 'alice', 'pcnt_won': 100}]

    wins = {'alice': 1}
    plays = {'alice': 2}
    top10 = topn(wins, plays, 10)
    assert top10 == [{'player': 'alice', 'pcnt_won': 50}]

    wins = {'alice': 1, 'bob': 0}
    plays = {'alice': 1, 'bob': 1}
    top10 = topn(wins, plays, 10)
    assert top10 == [
        {'player': 'alice', 'pcnt_won': 100},
        {'player': 'bob', 'pcnt_won': 0},
    ]

    wins = {'alice': 1, 'bob': 0}
    plays = {'alice': 1, 'bob': 1}
    top1 = topn(wins, plays, 1)
    assert top1 == [
        {'player': 'alice', 'pcnt_won': 100},
    ]


def test_mysort():
    score = [
        {'player': 'alice', 'pcnt_won': 0},
        {'player': 'bob', 'pcnt_won': 10},
        {'player': 'charlie', 'pcnt_won': 20},
    ]
    mysort(score)
    assert score == [
        {'player': 'charlie', 'pcnt_won': 20},
        {'player': 'bob', 'pcnt_won': 10},
        {'player': 'alice', 'pcnt_won': 0},
    ]
