#include <stdio.h>
#define N 101
int input_string(char* s) {
	char chr;
	int i = 0;
	printf("Enter your string: ");
	scanf_s("%c", &chr);
	while (1) {
		while (('a' <= chr && chr <= 'z') || ('0' <= chr && chr <= '9') || (chr == (',', ';'))) {
			s[i] = chr;
			i++;
			if (i > N - 1) {
				printf("Ñontent is full");
				return 0;
			}
			scanf_s("%c", &chr);
		}
		if (chr == ' ' && i != 0) {
			s[i] = ' ';
			i++;
			if (i > N - 1) {
				printf("Ñontent is full");
				return 0;
			}
		}
		while (chr == ' ')
			scanf_s("%c", &chr);
		if (chr == '.') {
			s[i] = '\0';
			break;
		}
	}
	return 1;
}
void quantityChar(char* s, int* k) {
	int i;
	for (i = 0; i < 26; i++) {
		k[i] = 0;
	}
	for (i = 0; s[i] != '\0'; i++) {
		k[s[i] - 'a']++;
	}
}
void print(int* k) {
	char ch;
	for (ch = 'a'; ch <= 'z'; ch++)
		if (k[ch - 'a'])
			printf("%c -> %d\n", ch, k[ch - 'a']);
}
void main() {
	char str[N];
	int kol[26];
	if (!(input_string(str))) {
		printf("Error");
		return;
	}
	quantityChar(str, kol);
	print(kol);
}