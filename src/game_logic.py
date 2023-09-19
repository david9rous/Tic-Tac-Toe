import random


def wincomb_horizontal(board: int):
    winning_combinations_horizontal = [[]]
    for i in range(board):
        winning_combinations_horizontal.append([])
        for j in range(i*board + 1, i*board + board + 1, board):
            for k in range(j, board + j):
                winning_combinations_horizontal[i].append(k)
    return winning_combinations_horizontal


def wincomb_vertical(board: int):
    winning_combinations_vertical = [[]]
    for i in range(1, board + 1):
        winning_combinations_vertical.append([])
        for j in range(i, board ** 2 + 1, board):
            winning_combinations_vertical[i].append(j)
    return winning_combinations_vertical


def wincomb_diagonal(board: int):
    winning_combinations_diagonal = [[]]
    for j in range(1, board ** 2 + 1, board + 1):
        winning_combinations_diagonal[0].append(j)
    winning_combinations_diagonal.append([])
    for j in range(board, board ** 2, board - 1):
        winning_combinations_diagonal[1].append(j)
    return winning_combinations_diagonal


def check_win(board, player):
    winning_combinations_vertical = wincomb_vertical(board)
    winning_combinations_horizontal = wincomb_horizontal(board)
    winning_combinations_diagonal = wincomb_diagonal(board)
    for i in winning_combinations_vertical:
        counter = 0
        for j in player:
            if j in i:
                counter += 1
            if counter == board:
                return True
    for i in winning_combinations_horizontal:
        counter = 0
        for j in player:
            if j in i:
                counter += 1
            if counter == board:
                return True
    for i in winning_combinations_diagonal:
        counter = 0
        for j in player:
            if j in i:
                counter += 1
            if counter == board:
                return True
    return False


def decide(board, cpu, player):
    winning_combinations_vertical = wincomb_vertical(board)
    winning_combinations_horizontal = wincomb_horizontal(board)
    winning_combinations_diagonal = wincomb_diagonal(board)
    opportunity = False
    winning_space = 0
    occupied = False
    for i in winning_combinations_vertical:
        counter = 0
        for x in player:
            if x in i:
                occupied = True
        if not occupied:
            for j in cpu:
                if j in i:
                    counter += 1
                if counter == board - 1:
                    opportunity = True
                    for k in i:
                        if k not in cpu:
                            winning_space = k
    for i in winning_combinations_horizontal:
        counter = 0
        for x in player:
            if x in i:
                occupied = True
        if not occupied:
            for j in cpu:
                if j in i:
                    counter += 1
                if counter == board - 1:
                    opportunity = True
                    for k in i:
                        if k not in cpu:
                            winning_space = k
    for i in winning_combinations_diagonal:
        counter = 0
        for x in player:
            if x in i:
                occupied = True
        if not occupied:
            for j in cpu:
                if j in i:
                    counter += 1
                if counter == board - 1:
                    opportunity = True
                    for k in i:
                        if k not in cpu:
                            winning_space = k
    if opportunity:
        return winning_space
    else:
        threats = {}
        max_threats = []
        threat_multiplier = 1
        for i in range(len(player)):
            for j in range(len(winning_combinations_vertical)):
                if player[i] in winning_combinations_vertical[j]:
                    for k in winning_combinations_vertical[j]:
                        if k not in threats:
                            threats.update({
                                k: 0
                            })
                        threat = threats[k]
                        if k in threats:
                            threat += 1
                        if k in player and k:
                            threat_multiplier += 1
                        threats[k] += threat * threat_multiplier
                        if k in player or k in cpu:
                            threats.pop(k)
                        max_threat = 0
                        for m in threats.values():
                            max_threat = max(m, max_threat)
                        for m in threats.values():
                            if m == max_threat:
                                max_threats.append(m)
        threat_multiplier = 1
        for i in range(len(player)):
            for j in range(len(winning_combinations_horizontal)):
                if player[i] in winning_combinations_horizontal[j]:
                    for k in winning_combinations_horizontal[j]:
                        if k not in threats:
                            threats.update({
                                k: 0
                            })
                        threat = threats[k]
                        if k in threats:
                            threat += 1
                        if k in player and k != player[i]:
                            threat_multiplier += 1
                        threats[k] += threat * threat_multiplier
                        if k in player or k in cpu:
                            threats.pop(k)
                        max_threat = 0
                        for m in threats.values():
                            max_threat = max(m, max_threat)
                        for m in threats.values():
                            if m == max_threat:
                                max_threats.append(m)
        threat_multiplier = 1
        for i in range(len(player)):
            for j in range(len(winning_combinations_diagonal)):
                if player[i] in winning_combinations_diagonal[j]:
                    for k in winning_combinations_diagonal[j]:
                        if k not in threats:
                            threats.update({
                                k: 0
                            })
                        threat = threats[k]
                        if k in threats:
                            threat += 1
                        if k in player and k != player[i]:
                            threat_multiplier += 1
                        threats[k] += threat * threat_multiplier
                        if k in player or k in cpu:
                            threats.pop(k)
                        max_threat = 0
                        for m in threats.values():
                            max_threat = max(m, max_threat)
                        for m in threats.values():
                            if m == max_threat:
                                max_threats.append(m)
        top_threats = []
        for i in threats:
            if threats[i] == max(threats.values()):
                top_threats.append(i)
        if len(top_threats) > 0:
            index_top = len(top_threats) - 1
        else:
            index_top = 0
        random_index = random.randint(0, index_top)
        return int(top_threats[random_index])
