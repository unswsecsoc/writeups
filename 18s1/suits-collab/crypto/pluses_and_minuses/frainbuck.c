#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int length = 0;
    printf("Enter max character length: ");
    scanf("%d", &length);
    char* flag = malloc(sizeof(char) * length);
    printf("Enter word: ");
    scanf("%s", flag);

    int i = 0;
    char current = 0;
    for (i = 0; i < length; i++) {
        char letter = flag[i];
        if (letter == 0) { break; } //automatically stop if null character
        while (current != letter) {
            if (current > letter) {
                printf("-");
                current--;
            } else {
                printf("+");
                current++;
            }
        }
        if (i < length - 1 && flag[i+1] != 0) { printf("."); }
    }
    printf("\n");
    return EXIT_SUCCESS;
}
