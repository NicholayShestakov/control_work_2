from standart_matrix import Matrix


def test_init():
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    assert str(matrix) == "1 2 3\n4 5 6\n7 8 9\n10 11 12"


def test_init_incorrect():
    try:
        Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]])
    except Exception as e:
        assert str(e) == "Used list is not convertable into matrix."


def test_rotate_1():
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    matrix.rotate()
    assert str(matrix) == "3 6 9 12\n2 5 8 11\n1 4 7 10"


def test_rotate_2():
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    matrix.rotate(2)
    assert str(matrix) == "12 11 10\n9 8 7\n6 5 4\n3 2 1"


def test_rotate_3():
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    matrix.rotate(3)
    assert str(matrix) == "10 7 4 1\n11 8 5 2\n12 9 6 3"


def test_rotate_4():
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    matrix.rotate(4)
    assert str(matrix) == "1 2 3\n4 5 6\n7 8 9\n10 11 12"


def test_matrix_multiple_matrix():
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    matrix_2 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    assert (
        str(matrix_1 * matrix_2)
        == "38 44 50 56\n83 98 113 128\n128 152 176 200\n173 206 239 272"
    )
