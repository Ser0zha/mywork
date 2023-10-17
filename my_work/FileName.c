#include <stdio.h>
#define N 100

int main() {
    int n = 0, i, quantity = 0, summa = 0, maximum = -1, flag = 0, t, arr[N];
    printf("Enter Natural number:\n");
    t = scanf_s("%d", &n);
    if (t == 0 || n >= N || n <= 0) {
        printf("ERROR: Invalid array size entered\n");
        return 0;
    }
    for (i = 0; i < n; i++) {
        if (!scanf_s("%d", &arr[i])) {
            printf("ERROR: Invalid array value entered\n");
            return 0;
        }
    }
    for (i = 0; i < n; i++) {
        if ((i * i) == arr[i]) {
           maximum = i;
        }
    }
    i = 0;
    for (; i < n; i++) {
        if (-10 <= arr[i] && arr[i] <= 10) {
            flag = 1;
            break;
        }
    }
    if (maximum == -1) {
        for (; i <= n - 1; i++) {
            summa += arr[i];
            quantity++;
        }
    }
    else {
        for (; i <= maximum; i++) {
            summa += arr[i];
            quantity++;
        }
    }
    printf("Your sum of array: %d\n", summa);
    printf("Quantity of elements: %d", quantity);
    return 0;
}
