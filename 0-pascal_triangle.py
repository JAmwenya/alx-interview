#!/usr/bin/python3
def pascal_triangle(n):
    try:
        triangle = []
        row = []
        i = 0
        j = 0
        #check if n is an integer
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if n <= 0:
            return []
        #initialize triangle
        triangle = [[1]]
        for i in range(1, n):
            row = [1] + [triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)] + [1]
            triangle.append(row)
        
        return triangle
    except TypeError as e:
        print(e)
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
