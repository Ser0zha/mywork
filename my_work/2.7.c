//Sortirovka array*
#include <stdio.h>
#define N 100

int main() {
    int n, i, j = 1, arr[N], tmp, flag = 1, max = 0;
    scanf_s("%d", &n);
    for (i = 0; i < n; i++)
        scanf_s"%d", &arr[i]);
    while (flag) {
        flag = 0;
        for (i = 0; i < n - max; i++) {
            if (arr[i] < 0) {
                for (j = i + 1; j < n; j++) {
                    if (arr[i] < arr[j]) {
                        tmp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = tmp;
                        flag = 1;
                    }
                }
            }
        }
        max += 1;
        for (i = 0; i < n - max; i++) {
            if (arr[i] >= 0) {
                for (j = i + 1; j < n; j++) {
                    if (arr[j] >= 0) {
                        if (arr[i] > arr[j]) {
                            tmp = arr[i];
                            arr[i] = arr[j];
                            arr[j] = tmp;
                            flag = 1;
                        }
                    }
                }
            }
        }
    }
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}
