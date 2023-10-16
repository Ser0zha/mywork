#include <stdio.h>
#define N 100

int main() {
    int n, i, quantity = 0, summa = 0, maximum = -1, flag = 0;
    int arr[N];
    printf("Enter Natural number:\n");
    if (!scanf_s("%d", &n)) {
        printf("ERROR: Invalid array size entered\n");
        return 0;
    }
    if (n > 100 || n <= 0) {
        printf("ERROR: Array size entered incorrectly");
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
    if (maximum == -1) {
        printf("ERROR: Upper bound number not found\n");
        return 0;
    }
    i = 0;
    for (; i < n; i++) {
        if (-10 <= arr[i] && arr[i] <= 10) {
            flag = 1;
            break;
        }
    }
    if (!flag || (i == n - 1) || (i > maximum)) {
        printf("ERROR: Number lower bounds not found");
        return 0;
    }
    for (; i <= maximum; i++) {
        summa += arr[i];
        quantity++;
    }
    printf("Your sum of array: %d\n", summa);
    printf("Quantity of elements: %d", quantity);
    return 0;
}
