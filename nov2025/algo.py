def to_csv_text(array):
    #receive a list of list
    #return a string back
    
    #splitlines the list
    #and add together
    
    #add it into one list
    #for each row, convert number to a string and join with a comma
    #join back with a string and a \n
    
    csv_rows=[]
    for row in array:
        csv_rows.append(','.join(map(str,row)))
    return '\n'.join(csv_rows)