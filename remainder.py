import time

print("What shall I remind you Leon?")

text = str(input())

print("In how many minutes?")

local_time = float(input())

local_time *= 60

time.sleep(local_time)

print(text)