from argparse import ArgumentParser

parcer = ArgumentParser()

parcer.add_argument("cfg", help="The path to the configuration file")
parcer.add_argument("text", help="The path to the file being processed")

args = parcer.parse_args()

with open(args.cfg, 'r') as file:
    config = file.readlines()
    config = [line.strip() for line in config]

with open(args.text, 'r') as file:
    text = file.readlines()
    text = [line.strip() for line in text]

pairs = {}
for pair in config:
    p = pair.strip().split("=")
    pairs[p[0]] = p[1]

data = []
for line in text:
    count = 0
    string = line
    for i in range(len(string)):
        for subs in pairs:
            if string[i:].startswith(subs):
                string = string[:i] + pairs[subs] + string[i+len(subs):]
                count += len(subs)
    data.append([line, string, count])

data = sorted(data, key=lambda x: x[2], reverse=True)

for line in data:
    print(str(line[2]) + " : ", end="")
    print(str(line[0]) + " -> ", end="")
    print(line[1])






