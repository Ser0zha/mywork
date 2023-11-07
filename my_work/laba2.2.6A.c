#include <stdio.h>
#define N 20

void printM(int mat[][N], int n, int m) {
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++)
            printf("%d ", mat[i][j]);
        printf("\n");
    }
    return;
}
int funout(int Amat[][N], int Bmat[][N], int Sizen, int Sizem) {
    int i, j, elements, maxi;
    maxi = funindicator(Amat, Sizen, Sizem);
    if (maxi == -2) {
        return 0;
    }
    for (i = 0; i < Sizen; i++) {
        for (j = 0; j < maxi; j++) {
            elements = Amat[i][j];
            Bmat[i][j] = elements;
        }
        if (maxi != (Sizem - 1)) {
            for (j = maxi + 1; j < Sizem; j++) {
                elements = Amat[i][j];
                Bmat[i][j - 1] = elements;
            }
        }
    }
    return Bmat;
}
int funindicator(int mat[][N], int n, int m) {
    int i, j, k = 0, max = -2;
    for (j = m - 1; j >= 0; j--) {
        for (i = 0; i < n; i++) {
            if ((mat[i][j] >= 0) && (mat[i][j] > mat[i + 1][j])) {
                k += 1;
            }
        }
        if (k == n) {
            max = j;
            break;
        }
        if (k < n) {
            k = 0;
        }
    }
    return max;
    if (max == -2) {
        return 0;
    }
}

int main() {
    int n = 0, m = 0, A[N][N], B[N][N], t, i, j, k = 0, max = -2;

    printf("Enter array size: ");
    t = scanf_s("%d %d", &n, &m);
    if (!t || (n, m) > N || (n, m) < 1 || n == m) {
        printf("ERROR: Invalid array size entered");
        return 0;
    }

    printf("Enter your matrix: \n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            if (!scanf_s("%d", &A[i][j])) {
                printf("ERROR: Invalid array value entered\n");
                return 0;
            }
        }
    }
    if (!(funout(A, B, n, m))) {
        printf("No such column found!");
        return 0;
    }
    printf("Matrix A:\n");
    printM(A, n, m);
    printf("Matrix B:\n");
    printM(B, n, (m - 1));
    return 0;
}
