f = open('dictionary2.txt')
lines = f.readlines()
for line in lines:
  line = line.strip()
  if line.startswith('p') and line.endswith('y'):
    print(line)
