#include<stdio.h>

int main()
{
    int a, b, t;
    scanf_s("%d%d", &a, &b);
    t = a;
    a = b;
    b = t;
    printf("a=%d b=%d", a, b);
    return 0;
}