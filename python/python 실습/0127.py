# 1974. 스도쿠 검증

def check_sudoku() :
    
    sudoku = []
    for _ in range(9) :
        row = list(map(int, input().split()))
        sudoku.append(row)

    for i in range(9) :
        if len(set(sudoku[i])) != 9 :
            return 0

    for j in range(9) :
        col = []
        for i in range(9) :
            col.append(sudoku[i][j])
        if len(set(col)) != 9 :
            return 0

    
    for i in range(0, 9, 3) : 
        for j in range(0, 9, 3) : 
            square = []
            for r in range(3) :
                for c in range(3) :
                    square.append(sudoku[i + r][j + c])
            if len(set(square)) != 9 :
                return 0

    return 1

T = int(input())
for t in range(1, T + 1) :
    result = check_sudoku()
    print(f"#{t} {result}")
                    


