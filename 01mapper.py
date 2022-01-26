# Sai Nallapati


f = open("purchases.txt","r")  # open file, read-only
o = open("outputData.txt", "w") # open file, write
for line in f:  
    rowData = line.strip().split("    ") # DT: List of Lists
    print (rowData )
    print (len(rowData ))
    if len(rowData) == 6:
        date, time, location, dept, amount, payType = rowData
        #assign names
        print ("{0}\t{1}".format(location, amount))
        o.write("{0}\t{1}\n".format(location, amount))
f.close()
o.close()