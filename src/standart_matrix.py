class Matrix:
    def __init__(self, list_matrix: list[list[int]]) -> None:
        """Matrix class with methods for work with matrix."""
        for row in list_matrix:
            if len(row) != len(list_matrix[0]):
                raise Exception("Used list is not convertable into matrix.")
        self.matrix = list_matrix
        self.height = len(list_matrix)
        self.length = len(list_matrix[0])

    def rotate(self, times: int = 1) -> None:
        """Rotates matrix on -90 degrees 'times' times."""
        times %= 4
        if times == 0:
            return

        rotated_matrix = [[] for _ in range(self.length)]
        for row in self.matrix:
            for index, value in enumerate(row):
                rotated_matrix[self.length - index - 1].append(value)

        temp = self.height
        self.height = self.length
        self.length = temp

        self.matrix = rotated_matrix
        self.rotate(times - 1)

    def __str__(self):
        # Преобразование матрицы в читаемый вид с помощью нечитаемой строчки.
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.length != other.height:
                raise Exception("Matrixes is not multiplable.")

            result_list = [[0 for _ in range(self.height)] for _ in range(other.length)]
            other.rotate(3)

            for i in range(self.height):
                for j in range(self.height):
                    result_list[i][j] = sum(
                        self.matrix[i][k] * other.matrix[j][self.length - k - 1]
                        for k in range(self.length)
                    )

            return Matrix(result_list)
