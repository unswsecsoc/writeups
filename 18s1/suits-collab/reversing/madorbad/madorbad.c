
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int oOoooOOo (char c) {
    return (c ^ 248) == 190;
}
int oOooOOoo (char c) {
    return (c ^ 43) == 103;
}
int oOoooooO (char c) {
    return (c ^ 160) == 225;
}
int oOoooOOO (char c) {
    return (c ^ 17) == 86;
}
int oOOOOoOO (char c) {
    return (c ^ 16) == 107;
}
int oOOOoOoo (char c) {
    return (c ^ 82) == 38;
}
int oOOoOooo (char c) {
    return (c ^ 7) == 111;
}
int oOOooooO (char c) {
    return (c ^ 25) == 120;
}
int oOOoOOOo (char c) {
    return (c ^ 56) == 86;
}
int oOOoOoOO (char c) {
    return (c ^ 19) == 120;
}
int oOoOOOOO (char c) {
    return (c ^ 232) == 183;
}
int oOOooOOO (char c) {
    return (c ^ 24) == 127;
}
int oOOoOOOO (char c) {
    return (c ^ 21) == 122;
}
int oOOooOoo (char c) {
    return (c ^ 182) == 210;
}
int oOOoOooO (char c) {
    return (c ^ 121) == 16;
}
int oOOooOoO (char c) {
    return (c ^ 188) == 217;
}
int oOOOooOo (char c) {
    return (c ^ 198) == 180;
}
int oOOOooOO (char c) {
    return (c ^ 75) == 56;
}
int oOOOoooo (char c) {
    return (c ^ 228) == 148;
}
int oOOOOooO (char c) {
    return (c ^ 70) == 63;
}
int oOOoOOoo (char c) {
    return (c ^ 82) == 62;
}
int oOOOOooo (char c) {
    return (c ^ 247) == 143;
}
int oOOooOOo (char c) {
    return (c ^ 80) == 54;
}
int ooOoOOoO (char c) {
    return (c ^ 203) == 230;
}
int ooOoOooo (char c) {
    return (c ^ 139) == 163;
}
int ooOOoooo (char c) {
    return (c ^ 205) == 253;
}
int oOoOOoOO (char c) {
    return (c ^ 54) == 109;
}
int oOOOOOoO (char c) {
    return (c ^ 232) == 149;
}
int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: ./madorbad <string>");
        fflush(stdout);
    }

    char* word = argv[1];
    printf("You're input is %s\n", word);
    if (strlen(word) != 58) {
        printf("Incorrect Length\n");
        fflush(stdout);
    }

    if (!oOoooOOo(word[19 ^ 19]))
        goto fail;
    if (!oOooOOoo(word[74 ^ 75]))
        goto fail;
    if (!oOoooooO(word[155 ^ 153]))
        goto fail;
    if (!oOoooOOO(word[254 ^ 253]))
        goto fail;
    if (!oOOOOoOO(word[246 ^ 242]))
        goto fail;
    if (!oOOOoOoo(word[151 ^ 146]))
        goto fail;
    if (!oOOoOooo(word[164 ^ 162]))
        goto fail;
    if (!oOOooooO(word[20 ^ 19]))
        goto fail;
    if (!oOOoOOOo(word[188 ^ 180]))
        goto fail;
    if (!oOOoOoOO(word[33 ^ 40]))
        goto fail;
    if (!oOoOOOOO(word[138 ^ 128]))
        goto fail;
    if (!oOOooOOO(word[32 ^ 43]))
        goto fail;
    if (!oOOoOOOO(word[206 ^ 194]))
        goto fail;
    if (!oOOooOoo(word[215 ^ 218]))
        goto fail;
    if (!oOoOOOOO(word[90 ^ 84]))
        goto fail;
    if (!oOOoOooO(word[189 ^ 178]))
        goto fail;
    if (!oOoOOOOO(word[99 ^ 115]))
        goto fail;
    if (!oOOooOOO(word[11 ^ 26]))
        goto fail;
    if (!oOOooOoO(word[105 ^ 123]))
        goto fail;
    if (!oOOoOOOo(word[42 ^ 57]))
        goto fail;
    if (!oOOooOoO(word[167 ^ 179]))
        goto fail;
    if (!oOOOooOo(word[154 ^ 143]))
        goto fail;
    if (!oOOooooO(word[165 ^ 179]))
        goto fail;
    if (!oOOOoOoo(word[177 ^ 166]))
        goto fail;
    if (!oOOooOoO(word[238 ^ 246]))
        goto fail;
    if (!oOOooOoo(word[224 ^ 249]))
        goto fail;
    if (!oOoOOOOO(word[21 ^ 15]))
        goto fail;
    if (!oOOOoOoo(word[56 ^ 35]))
        goto fail;
    if (!oOOoOooo(word[18 ^ 14]))
        goto fail;
    if (!oOOoOooO(word[41 ^ 52]))
        goto fail;
    if (!oOOOooOO(word[239 ^ 241]))
        goto fail;
    if (!oOoOOOOO(word[129 ^ 158]))
        goto fail;
    if (!oOOoOooO(word[169 ^ 137]))
        goto fail;
    if (!oOOoOOOo(word[132 ^ 165]))
        goto fail;
    if (!oOoOOOOO(word[14 ^ 44]))
        goto fail;
    if (!oOOOoooo(word[116 ^ 87]))
        goto fail;
    if (!oOOOOooO(word[26 ^ 62]))
        goto fail;
    if (!oOOOoOoo(word[82 ^ 119]))
        goto fail;
    if (!oOOoOooo(word[15 ^ 41]))
        goto fail;
    if (!oOOoOOOO(word[248 ^ 223]))
        goto fail;
    if (!oOOoOOOo(word[108 ^ 68]))
        goto fail;
    if (!oOoOOOOO(word[58 ^ 19]))
        goto fail;
    if (!oOOoOOoo(word[204 ^ 230]))
        goto fail;
    if (!oOOoOOOO(word[62 ^ 21]))
        goto fail;
    if (!oOOoOOoo(word[209 ^ 253]))
        goto fail;
    if (!oOoOOOOO(word[248 ^ 213]))
        goto fail;
    if (!oOOOOooo(word[3 ^ 45]))
        goto fail;
    if (!oOOooOoo(word[240 ^ 223]))
        goto fail;
    if (!oOOoOOoo(word[217 ^ 233]))
        goto fail;
    if (!oOOooOOo(word[85 ^ 100]))
        goto fail;
    if (!oOOoOooo(word[67 ^ 113]))
        goto fail;
    if (!ooOoOOoO(word[81 ^ 98]))
        goto fail;
    if (!ooOoOooo(word[131 ^ 183]))
        goto fail;
    if (!ooOOoooo(word[196 ^ 241]))
        goto fail;
    if (!oOoOOoOO(word[88 ^ 110]))
        goto fail;
    if (!oOOooooO(word[106 ^ 93]))
        goto fail;
    if (!oOOooOOo(word[181 ^ 141]))
        goto fail;
    if (!oOOOOOoO(word[187 ^ 130]))
        goto fail;
    printf(":>\n");
    return 0;

fail:
    printf(":<\n");
    exit(-1);
}

