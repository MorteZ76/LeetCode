def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    print len(a)
    result = []
    for row in range(len(a)) :
        
        new_row = []
        for col in range (len(a[0])):
            new_row.append(a[col][row])
        result.append(new_row)
    return result
        

    # Your code here
    pass