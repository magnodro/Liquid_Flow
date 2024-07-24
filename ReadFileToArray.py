def parse_file_to_matrix(filename):
    matrix = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            char, x, y = line.strip().split()
            x, y = int(x), int(y)
            if len(matrix) <= y:
                matrix += [[] for _ in range(y - len(matrix) + 1)]
            if len(matrix[y]) <= x:
                matrix[y] += [' ' for _ in range(x - len(matrix[y]) + 1)]
            matrix[y][x] = char
    return matrix

def find_asterisk_and_neighbors(matrix):
    allowed_chars = set('═║╔╗╚╝╠╣╦╩')
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == '*':
                neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                letters = []
                for nx, ny in neighbors:
                    if 0 <= nx < len(row) and 0 <= ny < len(matrix) and matrix[ny][nx] not in allowed_chars and matrix[ny][nx] != '*':
                        letters.append(matrix[ny][nx])
                return letters
    return []

filename = r'C:\Users\Dro\Desktop\past.txt'  # Replace with your file path
matrix = parse_file_to_matrix(filename)
letters = find_asterisk_and_neighbors(matrix)
print(letters)