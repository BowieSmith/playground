def m_sum(m1, m2):
    '''Sum two matrices'''
    return [[sum([m1[row][col], m2[row][col]]) for col in range(len(m1[0]))] for row in range(len(m1))]

def m_print(m):
    '''Pretty print matrix'''
    for row in m:
        print(row)

def m_dot(v1, v2):
    '''Dot product of two vectors'''
    return sum(e[0] * e[1] for e in zip(v1,v2))

def m_tran(m):
    '''Transpose matrix'''
    return [[row[col] for row in m] for col in range(len(m[0]))]

def m_mult(m1, m2):
    '''Multiple two matrices'''
    return m_tran([[m_dot(row1, row2) for row1 in m1] for row2 in m_tran(m2)])
