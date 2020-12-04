from commenUtils import get_input_data


def simple_solution_part_1(slope: tuple[int, int]) -> int:
    grid: list[list[str]] = get_input_data()
    height: int = len(grid)
    width = len(grid[0])
    pos: list[int, int] = [0, 0]
    tree_count: int = 0
    while pos[0] < height:
        if grid[pos[0]][pos[1]] == "#":
            tree_count += 1
        pos[0] += slope[1]
        pos[1] = (pos[1] + slope[0]) % width
    return tree_count


def simple_solution_part_2() -> int:
    slopes: list[tuple[int, int]] = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_counts: list[int] = []
    for slope in slopes:
        tree_counts.append(simple_solution_part_1(slope))
    product: int = 1
    for tree_count in tree_counts:
        product *= tree_count
    return product


if __name__ == '__main__':
    print(simple_solution_part_1((3, 1)))
    print(simple_solution_part_2())
