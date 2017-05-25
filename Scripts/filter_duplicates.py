inFile = open('words_u_v_w_x_y_z.csv', 'r')
outFile = open('words_u_w_w_x_y_z.all.csv', 'w')
listLines = []
for line in inFile:
    words = line.split('[')
    if words[0] in listLines:
        continue
    else:
        listLines.append(words[0])
        outFile.write(line)
        
        
outFile.close()

inFile.close()
