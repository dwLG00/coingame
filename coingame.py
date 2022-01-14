import random
import numpy as np

def game(p1, p2):
	seq = []
	while True:
		roll = random.choice(['H', 'T'])
		seq.append(roll)
		if len(seq) >= 3:
			if ''.join(seq[-3:]) == p1:
				return ('p1', seq)
			elif ''.join(seq[-3:]) == p2:
				return ('p2', seq)

def batch(p1, p2, batch=100):
	p1_wins, p2_wins = 0, 0
	for _ in range(batch):
		winner, _ = game(p1, p2)
		if winner == 'p1':
			p1_wins += 1
		elif winner == 'p2':
			p2_wins += 1
	return (p1_wins, p2_wins)


def matrix(bat=100):
	choicelist = ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']
	array = np.zeros((8, 8))

	for i, p1 in enumerate(choicelist):
		for j, p2 in enumerate(choicelist):
			p1_wins, p2_wins = batch(p1, p2, batch=bat)
			array[i, j] = p1_wins / bat

	return array
