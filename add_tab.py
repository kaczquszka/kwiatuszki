 
with open("answers.csv", "r") as infile, open("answers_tab.csv", "w") as outfile:
    for line in infile:
        line = line.rstrip('\n')
        spliited = line.rsplit(None,1)
        line = "\t".join(spliited)
        outfile.write(line+"\n")