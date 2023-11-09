#!/usr/bin/env python3
import os
import csv
import datetime

with open('software.csv') as f:
	for line in f:
		print(line)


with open('software.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		print('Name:{}, Users: {}'.format(row['name'],row['users']))


friends= [["Renatinha","Lol"],["Mathews","Escola"],["Mouras","Escola"],["Sivi","Alfabetização"]]

with open('friends.csv','w') as f:
	writer = csv.writer(f)
	writer.writerows(friends)

relacoes=[{'name':'Renatinha','relacao':'Namorada'},{'name':'Sivi','relacao':'Amizade'},{'name':'Ruan','relacao':'Professor'}]
keys=['name','relacao']

with open('relacoes.csv','w') as f:
	writer = csv.DictWriter(f,fieldnames=keys)
	writer.writeheader()
	writer.writerows(relacoes)




