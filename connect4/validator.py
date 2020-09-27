
mark={0:"R", 1:"Y"}


def check_validity(count,column,board):
    if column>=len(board[0]) or column<0 or board[-1][column]:
        return "invalid"
    else:
        row=0
        while board[row][column]:
            row+=1
        board[row][column]=mark[count%2]
        return "valid"


def check_winner(board):
    
    # check each row
    for i in board:
        op=check_row_column(i)
        if op: return "{} wins".format(op)
    
    #check each column
    for i in range(len(board[0])):
        op=check_row_column([ board[r][i] for r in range(len(board)) ])
        if op: return "{} wins".format(op)
    
    op=check_diagonal(board)
    if op: return "{} wins".format(op)


def check_row_column(row):
    mid=row[len(row)//2]
    if not mid: return

    index=row.index(mid)
    count=0
    while count<4 and index<len(row):
        if row[index]==mid:
            count+=1
        else:
            return
        index+=1
    
    if count==4 : return mid


def check_diagonal(board):

    for i in range(len(board)//2):
        for j in range(len(board[0])):
        
        
            if not board[i][j]:
                continue
            
            #check right diagonal
            if j+3<len(board[0]):
                
                count=1
                val=board[i][j]
                k,l=i,j
                while count<4:
                    k+=1
                    l+=1
                    if board[k][l]==val: count+=1
                    else: break
                if count==4: 
                    return val
            
            #check left diagonal
            if j-3>=0:
                count=1
                val=board[i][j]
                k,l=i,j
                while count<4:
                    k+=1
                    l-=1
                    if board[k][l]==val: count+=1
                    else:break
                
                if count==4: 
                    return val


         
