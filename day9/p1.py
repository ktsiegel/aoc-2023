from sys import argv

def history(line):
    values = [int(x) for x in line.split(" ")]
    all_differences = [values]
    while True:
        differences = []
        has_non_zero = False
        last = all_differences[len(all_differences)-1]
        for i in range(len(last)-1):
            first = last[i]
            second = last[i+1]
            diff = second - first
            differences.append(diff)
            if diff != 0:
                has_non_zero = True
        all_differences.append(differences)
        if not has_non_zero:
            break


    j = len(all_differences) - 1
    all_differences[j].append(0)
    j -= 1

    while j >= 0:
        all_differences[j].append(all_differences[j][len(all_differences[j])-1]+all_differences[j+1][len(all_differences[j+1])-1])
        j -= 1

    return all_differences[0][len(all_differences[0])-1]
        


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    total = 0
    for line in input:
        total += history(line)

    print(total)
        

if __name__ == "__main__":
    main(argv[1])

        