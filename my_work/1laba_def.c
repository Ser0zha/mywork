#include <stdio.h>
#define N 100

int algorithm(int n, int x1, int max, int array[], int* quantity) {
    int i = 0, summa = 0;
    if (max == -1) {
        for (i = x1; i < n; i++) {
            summa += array[i];
            ++*quantity;
        }
    }
    else {
        for (i = x1; i <= max; i++) {
            summa += array[i];
            ++*quantity;
        }
    }
    return summa;
}

int main() {
    int n = 0, i, quantity = 0, summa = 0, maximum = -1, element = 0, t, arr[N], value = -1;
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
        if (-10 <= arr[i] && arr[i] <= 10) {
            element = i;
            value = arr[i];
            break;
        }
    }
    if (value == -1) {
        printf("No such elements found!");
    }
    else {
        for (i = element; (i + 1) < n; i++) {
            if ((i * i) == arr[i]) {
                maximum = i;
            }
        }
        printf("Your sum of array: %d\nQuantity of elements : %d", algorithm(n, element, maximum, arr, &quantity), quantity);
    }
    return 0;
}
