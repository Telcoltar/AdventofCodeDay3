def get_input_data() -> list[list[str]]:
    f = open("inputData.txt", "r")
    grid: list[list[str]] = []
    for line in f:
        line_of_symbols: list[str] = []
        for symbol in line.strip():
            line_of_symbols.append(symbol)
        grid.append(line_of_symbols)
    return grid
