import numpy as np
import sys

# First come, first served
# Tasks are assigned to the first team that requests them, 
# as long as those tasks aren't worked on by enough teams already

input_file = "default_input.csv"
if len(sys.argv) > 1:
	input_file = sys.argv[1]

data = np.genfromtxt(input_file, delimiter=', ', skip_header = 1, dtype='str', usecols=(0, 1, 2, 3))

teams = {}
tasks = set([])

for i, line in enumerate(data):
	current_tasks = []
	for j, word in enumerate(data[i]):
		if j != 0:
			current_tasks.append(word)
			tasks |= {word}
	teams[line[0]] = current_tasks

tasks = list(tasks)
task_count = []
for i in tasks:
	task_count.append(0)
per_team = round(len(data) / len(tasks))

assignment = {}
dissapointment = 0

for t, v in teams.items():
	for i in range(0, 3):
		if task_count[tasks.index(v[i])] < per_team:
			task_count[tasks.index(v[i])] += 1
			assignment[t] = v[i]

			dissapointment += i
			
			break

# print(tasks)
# print(task_count)
# print("--------")
# print(teams)
# print("--------")
print(assignment)
print("--------")
print("Dissapointment:  {d}".format(d=dissapointment))