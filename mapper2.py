# Nallapati 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 8) : 
    InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country = datalist

    # print intermediate key-value pairs to standard output
    print(CustomerID,"\t",UnitPrice)