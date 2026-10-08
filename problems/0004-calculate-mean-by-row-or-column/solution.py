def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    mean = []
    rows = len(matrix)
    cols = len(matrix[0])
    if mode == 'column':
        for i in range(cols):          
            col_sum = 0
            for j in range(rows):       
                col_sum += matrix[j][i]
            mean.append(col_sum / rows) 
        return mean       
    elif mode == 'row':
        for i in range(rows):           
            row_sum = 0
            for j in range(cols):   
                row_sum += matrix[i][j]
            mean.append(row_sum / cols) 
        return mean