import graphics as gr

window = gr.GraphWin('Fractal rectangle', 600, 600)
ALPHA = 0.3


def fractal_rectangle(A, B, C, D, deep=10):
    """
    Рекурсивная функция, которая рисует фрактал из квадратов.
    :param A: точка A квадрата.
    :param B: точка B квадрата.
    :param C: точка C квадрата.
    :param D: точка D квадрата.
    :param deep: глубина фрактала, количество квадратов в глубину.
    :return: Рекурсивная функция. Начинает возвращать, когда прорисует последний квадрат.
    """
    if deep < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    newA = (A[0] * (1 - ALPHA) + B[0] * ALPHA, A[1] * (1 - ALPHA) + B[1] * ALPHA)
    newB = (B[0] * (1 - ALPHA) + C[0] * ALPHA, B[1] * (1 - ALPHA) + C[1] * ALPHA)
    newC = (C[0] * (1 - ALPHA) + D[0] * ALPHA, C[1] * (1 - ALPHA) + D[1] * ALPHA)
    newD = (D[0] * (1 - ALPHA) + A[0] * ALPHA, D[1] * (1 - ALPHA) + A[1] * ALPHA)
    fractal_rectangle(newA, newB, newC, newD, deep - 1)


fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500))

window.getMouse()
window.close()
