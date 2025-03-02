def print_spiral_order(matrix):
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    spiral_order = []

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            spiral_order.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            spiral_order.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral_order.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral_order.append(matrix[i][left])
            left += 1

    print(" ".join(map(str, spiral_order)))





print_spiral_order(matrix)
