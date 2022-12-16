from collections import defaultdict
from datetime import datetime


def processData(dataset):
    f = open(f'data/{dataset}.txt', 'r')
    contents = f.read().splitlines()

    lines = defaultdict(list)

    for i in range(len(contents)):
        nodesByDate = contents[i].split()
        interactionDate = datetime.fromtimestamp(int(nodesByDate[-1]))
        interactionDate = int(interactionDate.year)
        line = nodesByDate[0] + " " + nodesByDate[1] + '\n'
        lines[interactionDate].append(line)

    for j in lines.keys():
        f = open(f'data/{dataset}_{j}.txt', 'w')
        f.writelines(lines[j])
        f.close()


processData("mathoverflow")
processData("stackoverflow")
