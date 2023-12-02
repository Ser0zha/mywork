#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct Word {
	char* inf; // Массив символов
	size_t n_elements; // Сколько букв
	struct Word* next;
} Word;

static Word* creat_word() {
    Word* word = (Word*)malloc(sizeof(Word));
    word->next = NULL;
    word->n_elements = 0;
    return word;
}

static int scan_word(Word* word, int *max) {
    *max = 0;
    char* str = (char*)malloc(word->n_elements + 1);
    char c;
    while (scanf("%c", &c) && (c != ' ' && c != ',')) {
        if ('0' <= c && c <= '9') {
            free(str);
            word->n_elements = 0;
            word->inf = 0;
            *max = -1;
            printf("Error");
            return 1;
        }
        if ((c == '.') || (c == '!') || (c == '?')) {
            str[word->n_elements] = 0;
            word->inf = str;
            return 1;
        }
        str[word->n_elements] = c;
        word->n_elements++;
        if (*max < word->n_elements)
            *max = word->n_elements;
        str = (char*)realloc(str, word->n_elements + 1);
        if (word->n_elements > 20) {
            free(str);
            word->n_elements = 0;
            word->inf = 0;
            printf("Error");
            return 1;
        }
    }
    str[word->n_elements] = 0;
    word->inf = str;
    return 0;
}
int scan_text(Word* word) {
    int maxi = 0, s = 1;
    Word* pWord = word;
    while (!scan_word(pWord, &maxi)) {
        s++;
        if (s > 30) {
            printf("Error");
            return -1;
        }
        pWord->next = creat_word();
        pWord = pWord->next;
    }
    return maxi;
}
void print_word_index(Word *word, int maxx) {
    Word *pList = word;
    short n = 0, f = 0;
    while (pList!=NULL) {
        if (pList->n_elements == maxx) {
            printf("%s ", pList->inf);
        }
        pList=pList->next;
        f++;
    }
    if (f = 0)
        printf("Not found");
}
void main() {
    int max;
	Word* word_list = creat_word();
	max = scan_text(word_list);
    if (max == -1)
        return 0;
	print_word_index(word_list, max);
}
