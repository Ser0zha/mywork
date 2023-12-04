#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define charlimit 20
#define strlimit 30

typedef struct Word {
    char* inf; // Массив символов
    size_t n_elements; // Сколько букв
    struct Word* next;
} Word;

static Word* creat_word() {
    Word* word;
    if (!(word = (Word*)malloc(sizeof(Word)))) {
        printf("Error, memory!");
        return NULL;
    }
    word->next = NULL;
    word->n_elements = 0;
    return word;
}

static int scan_word(Word* word, int* max, int *ss) {
    *max = 0;
    char* str;
    char c;
    if (!(str = (char*)malloc(word->n_elements + 1))) {
        printf("Error, memory!");
        return NULL;
    } 
    while (scanf("%c", &c) && (c != ' ')) {
        if ('0' <= c && c <= '9') {
            free(str);
            word->n_elements = 0;
            word->inf = 0;
            *max = -1;
            printf("Error, u can`t use number!");
            return 1;
        }
        if ((c == '.') || (c == '!') || (c == '?')) {
            str[word->n_elements] = 0;
            word->inf = str;
            return 1;
        }
        if (!(('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z'))) {
            printf("U cannot use prohibited characters!");
            return 1;
        }
        str[word->n_elements] = c;
        word->n_elements++;
        if (*max < word->n_elements)
            *max = word->n_elements;
        ss++;
        if (!(str = (char*)realloc(str, word->n_elements + 1))) {
            printf("Error, memory!");
            return NULL;
        }
        if (word->n_elements > charlimit) {
            free(str);
            word->n_elements = 0;
            word->inf = 0;
            printf("Error, word is full!");
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
    while (!scan_word(pWord, &maxi, &s)) {
        if (s > strlimit) {
            printf("Error, sentence is full!");
            return -1;
        }
        pWord->next = creat_word();
        pWord = pWord->next;
    }
    return maxi;
}
void free_word(Word* first_word) {
    Word* pList = first_word, * freeList;
    while (pList != NULL) {
        free(pList->inf);
        freeList = pList;
        pList = pList->next;
        free(freeList);
    }
}
void print_word_index(Word* word, int maxx) {
    Word* pList = word;
    short n = 0;
    while (pList != NULL) {
        if (pList->n_elements == maxx) {
            printf("%s ", pList->inf);
        }
        pList = pList->next;
    }
}
void main() {
    int max;
    printf("Enter sentence: ");
    Word* word_list = creat_word();
    max = scan_text(word_list);
    if (max == -1)
        return;
    else if (max == 0) {
        printf("NULL");
        return;
    }
    printf("Max words: ");
    print_word_index(word_list, max);
    free_word(word_list);
}
