
def min_path_sum(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    # Создаем таблицу DP
    # dp[i][j] будет хранить минимальную сумму пути до ячейки (i, j)
    dp = [[0] * cols for _ in range(rows)]
    
    # Инициализируем начальную ячейку
    dp[0][0] = grid[0][0]
    
    # Заполняем первый столбец
    # В ячейки первого столбца можно попасть только сверху
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        
    # Заполняем первую строку
    # В ячейки первой строки можно попасть только слева
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]
        
    # Заполняем остальную таблицу
    for i in range(1, rows):
        for j in range(1, cols):
            # Значение ячейки = свое значение + минимум из (сверху, слева)
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
            
    # Нижняя правая ячейка содержит минимальную сумму пути
    return dp[rows-1][cols-1]

# Пример использования
if __name__ == "__main__":
    # Пример 1
    grid1 = [[1,3,1], [1,5,1], [4,2,1]]
    result1 = min_path_sum(grid1)
    print(f"Grid 1: {grid1}")
    print(f"Результат: {result1}") # Ожидается: 7

    # Пример 2
    grid2 = [[1,2,3], [4,5,6]]
    result2 = min_path_sum(grid2)
    print(f"Grid 2: {grid2}")
    print(f"Результат: {result2}") # Ожидается: 12