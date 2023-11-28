#include <stdio.h>
#include <stdlib.h>

struct list {
	int inf;
	struct list* next;
};

struct list* input(struct list* F, int* index1, int* index2, int* k) {
	struct list* P, * T;
	int index_all = 1, flag = 1;
	F = P = T = NULL;
	printf("Enter your value:");
	while (1) {
		T = (struct list*)malloc(sizeof(struct list));
		T->next = NULL;
		if (!scanf_s("%d", &T->inf))
			break;
		if (F == NULL) {
			F = T;
			P = T;
		}
		else {
			P->next = T;
			P = T;
			index_all++;
		}
		if (T->inf % 2 == 0) {
			++*k;
			*index2 = index_all;
			if (flag && *index2) {
				*index1 = *index2;
				flag = 0;
			}
		}
	}
	return F;
}
struct list* deleted(struct list* F, int* index1, int* index2) {
	struct list* PU, * U;
	int b = 1;
	PU = F;
	if (*index1 == 1 && *index1 == *index2) {
		U = F;
		F = F->next;
		free(U);
		return F;
	}
	while (PU->next != NULL) {
		U = PU->next;
		b++;
		if ((b == *index2) || (b == *index1)) {
			PU->next = U->next;
			free(U);
		}
		else {
			PU = U;
		}
	}
	if ((*index1 == 1) && (*index1 != *index2)) {
		U = F;
		F = F->next;
		free(U);
	}
	return F;
}
void main() {
	struct list* F, * P, * T, * U;
	int k = 0, index1 = 0, index2 = 0, b = 1;
	F = P = T = U = NULL;
	F = input(F, &index1, &index2, &k);
	if (F == NULL) {
		printf("NULL");
		return;
	}
	F = deleted(F, &index1, &index2);
	printf(">>> ");
	for (T = F; T != NULL; T = T->next)
		printf("%d ", T->inf);
	for (T = F; F != NULL; T = F) {
		F = F->next;
		free(T);
	}
}
