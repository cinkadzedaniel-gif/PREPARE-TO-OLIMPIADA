import sys

def solve():
    line = sys.stdin.readline()

    if not line:
        return

    n = int(line.strip())

    for i in range(n):
        current_line = sys.stdin.readline().strip()

        print(f"Оброблено рядок {i + 1}: {current_line}")


if __name__ == "__main__":
    solve()