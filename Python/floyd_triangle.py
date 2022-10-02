class FloydTriangle:

    @staticmethod
    def calculate_width_of_triangle(rows: int):
        last_row = rows - 1
        last_row_start_num = (pow(last_row, 2) + last_row + 2)//2
        last_row_end_num = last_row_start_num + rows
        width = 0
        for i in range(last_row_start_num, last_row_end_num+1):
            width += len(str(i)) + 1
        width -= 2
        return width

    @staticmethod
    def create(rows: int, start_num: int = 1, flip_horizontally: bool = False, flip_vertically: bool = False):
        print_num = start_num

        if not flip_horizontally and not flip_vertically:
            for row in range(1, rows+1):
                for _ in range(row):
                    print(print_num, end=" ")
                    print_num += 1
                print()
        elif flip_horizontally and not flip_vertically:
            width = FloydTriangle.calculate_width_of_triangle(rows)
            for row in range(1, rows+1):
                row_string = ""
                for _ in range(row):
                    row_string += str(print_num) + " "
                    print_num += 1
                print(row_string.rjust(width, " "))
        elif not flip_horizontally and flip_vertically:
            for row in range(rows-1, -1, -1):
                print_num = (pow(row, 2) + row + 2)//2
                for _ in range(row+1):
                    print(print_num, end=" ")
                    print_num += 1
                print()
        else:
            width = FloydTriangle.calculate_width_of_triangle(rows)
            for row in range(rows-1, -1, -1):
                row_string = ""
                print_num = (pow(row, 2) + row + 2)//2
                for _ in range(row+1):
                    row_string += str(print_num) + " "
                    print_num += 1
                print(row_string.rjust(width, " "))


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))

    print(f"[INFO] Normal Floyd Triangle of {rows} rows")
    FloydTriangle.create(rows)

    print(f"\n[INFO] Floyd Triangle of {rows} rows starting with 4")
    FloydTriangle.create(rows, start_num=4)

    print(f"\n[INFO] Horizontally flipped Floyd Triangle of {rows} rows")
    FloydTriangle().create(rows, flip_horizontally=True)

    print(f"\n[INFO] Vertically flipped Floyd Triangle of {rows} rows")
    FloydTriangle().create(rows, flip_vertically=True)

    print(
        f"\n[INFO] Horizontally and vertically flipped Floyd Triangle of {rows} rows")
    FloydTriangle().create(rows, flip_horizontally=True, flip_vertically=True)
