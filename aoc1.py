def getcals():
    with open("nums.txt") as f:
        elf_list = []
        elf = 0
        for line in [line.rstrip() for line in f.readlines()]:
            if line:
                elf += int(line)
            else:
                elf_list.append(elf)
                elf = 0
        print(max(elf_list))
        total = max(elf_list)
        elf_list.remove(max(elf_list))
        print(max(elf_list))
        total += max(elf_list)
        elf_list.remove(max(elf_list))
        print(max(elf_list))
        total += max(elf_list)

        print(total)


getcals()