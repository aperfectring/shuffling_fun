#!/usr/bin/python3

import sys

out_shuffle = [0, 26, 1, 27, 2, 28, 3, 29, 4, 30, 5, 31, 6, 32, 7, 33, 8, 34, 9, 35, 10, 36, 11, 37, 12, 38, 13, 39, 14, 40, 15, 41, 16, 42, 17, 43, 18, 44, 19, 45, 20, 46, 21, 47, 22, 48, 23, 49, 24, 50, 25, 51]
in_shuffle = [26, 0, 27, 1, 28, 2, 29, 3, 30, 4, 31, 5, 32, 6, 33, 7, 34, 8, 35, 9, 36, 10, 37, 11, 38, 12, 39, 13, 40, 14, 41, 15, 42, 16, 43, 17, 44, 18, 45, 19, 46, 20, 47, 21, 48, 22, 49, 23, 50, 24, 51, 25]

steps = []

def build_step(step_no):
    if (step_no == 0):
        if (len(steps) > 0):
            return
        for i in range(0,52):
            steps.append([])
            steps[i].append([i])
        return

    if (len(steps) < 52):
        build_step(step_no-1)

    if (len(steps[step_no-1]) < 1):
        build_step(step_no-1)

    for i in range(0,52):
        steps[i].append([])
        for j in steps[i][step_no-1]:
            steps[i][step_no].append(j)

            if out_shuffle[j] not in steps[i][step_no-1]:
                steps[i][step_no].append(out_shuffle[j])

            if in_shuffle[j] not in steps[i][step_no-1]:
                steps[i][step_no].append(in_shuffle[j])
    return

def min_step_len():
    min_len = 1000

    for i in range(0,52):
        this_len = len(steps[0][-1])
        if this_len < min_len:
            min_len = this_len

    return min_len

def find_num_steps(start_pos, end_pos):
    int_start_pos = int(start_pos)
    int_end_pos = int(end_pos)

    for i in range(0,len(steps[int_end_pos])):
        if int_start_pos in steps[int_end_pos][i]:
            print("Number of shuffles: " + str(i))
            return i

def find_step_pattern(start_pos, end_pos):
    num_steps = find_num_steps(start_pos, end_pos)
    int_start_pos = int(start_pos)
    int_end_pos = int(end_pos)

    step_string = ""
    prev_pos = int_start_pos
    for i in range(num_steps-1, -1, -1):
        for potential_pos in steps[int_end_pos][i]:
            if out_shuffle[potential_pos] == prev_pos:
                step_string = step_string + "O"
                prev_pos = potential_pos
                continue

            if in_shuffle[potential_pos] == prev_pos:
                step_string = step_string + "I"
                prev_pos = potential_pos
                continue

    print("Shuffle pattern: " + step_string)


build_step(0)

step = 0
while 1:
    build_step(step)
    min_len = min_step_len()

    if min_len >= 52:
        break

    step = step + 1

print("Maximum number of shuffles to get any card from one position to another: " + str(step))

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " <start position> <end position>")
    print("Note: positions are 0-based")
    exit(1)

start_pos = sys.argv[1]
end_pos = sys.argv[2]

print("start pos: " + start_pos + " end pos: " + end_pos)
find_step_pattern(start_pos, end_pos)

