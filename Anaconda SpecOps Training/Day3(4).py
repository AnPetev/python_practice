file = open('input.txt', 'r')
for line in file:
      output = line.title()
rewrite = open('output.txt', 'w')
rewrite.write(output)
      