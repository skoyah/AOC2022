file = open('01_input.txt', 'r')

elf = [0, 0]

current_elf = 0
calories_count = 0

for line in file:
    content = line.strip()

    if content:
        calories_count += int(content)
    else:
        if calories_count > elf[1]:
            elf = [current_elf, calories_count]

        current_elf += 1
        calories_count = 0

file.close()

print(elf[1])
