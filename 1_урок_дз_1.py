duration = int(input())
time = [86400, 3600, 60, 1]
words = ["дн", "час", "мин", "сек"]
all_time = []
for i in range(4):
    if duration >= time[i]:
        all_time.append(str(duration // time[i]))
        all_time.append(words[i])
        duration -= (duration // time[i]) * time[i]

print(" ".join(all_time))