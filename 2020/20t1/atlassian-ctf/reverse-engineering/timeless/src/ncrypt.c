#include <sodium/crypto_pwhash.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include "sha256.h"

void sha256(const void* src, int len, void* hash) {
    SHA256_CTX sha;
    sha256_init(&sha);
    sha256_update(&sha, src, len);
    sha256_final(&sha, hash);
}

// musl_srand and musl_rand are copied from musl-libc
// source: https://git.musl-libc.org/cgit/musl/tree/src/prng/rand.c?h=v1.1.22
// musl is licensed under the MIT license
static uint64_t musl_seed;
static void musl_srand(unsigned s) {
	musl_seed = s-1;
}

static int musl_rand(void) {
	musl_seed = 6364136223846793005ULL*musl_seed + 1;
	return musl_seed>>33;
}


uint8_t secure_rand8(void) {
    // generate 16 random values
    uint32_t random_values[16];
    for (int i = 0; i < 16; i++) {
        random_values[i] = musl_rand();
    }

    // calculate sha256 hash
    uint8_t random_hash[32];
    sha256(random_values, 16 * 4, random_hash);

    // xor each byte of hash together for final value
    uint8_t acc = 0;
    for (int i = 0; i < 32; i++) {
        acc ^= random_hash[i];
    }
    return acc;
}

static FILE* open_input_file(const char* name);
static FILE* open_output_file(const char* in_name, int is_encrypted,
        char* out_name);
static int determine_if_encrypted(FILE* in);
static void get_password(char* password);
static void encrypt(FILE* in, FILE* out, char* password);
static void decrypt(FILE* in, FILE* out, char* password, char* out_name);
static int process_chunk(FILE* in, FILE* out,
        uint32_t* checksum, int is_encrypted);

int main(int argc, char** argv) {
    // check args
    if (argc != 2) {
        printf("usage: %s <file>\n", argv[0]);
        return 0;
    }

    // open input file
    FILE* in = open_input_file(argv[1]);

    // determine if file is encrypted
    int is_encrypted = determine_if_encrypted(in);

    // open output file
    char out_name[FILENAME_MAX];
    FILE* out = open_output_file(argv[1], is_encrypted, out_name);

    // get password
    char password[256];
    get_password(password);

    if (is_encrypted) {
        decrypt(in, out, password, out_name);
    } else {
        encrypt(in, out, password);
    }

    // close files and return
    fclose(out);
    fclose(in);
    return 0;
}

FILE* open_input_file(const char* name) {
    FILE* in = fopen(name, "rb");
    if (in == NULL) {
        printf("error: failed to open '%s' for reading\n", name);
        exit(1);
    }
    return in;
}

static FILE* open_output_file(const char* in_name, int is_encrypted,
        char* out_name) {
    if (is_encrypted) {
        strncpy(out_name, in_name, FILENAME_MAX);
        int len = strlen(out_name);
        // strip .tl suffix if present
        if (strcmp(&out_name[len-3], ".tl") == 0) {
            out_name[len-3] = 0;
        } else {
            strcat(out_name, ".decoded");
        }
    } else {
        snprintf(out_name, FILENAME_MAX, "%s.tl", in_name);
    }
    if (access(out_name, F_OK) != -1) {
        printf("error: output file '%s' already exists\n", out_name);
        exit(1);
    }
    FILE* out = fopen(out_name, "wb");
    if (out == NULL) {
        printf("error: failed to open '%s' for writing\n", out_name);
        exit(1);
    }
    return out;
}

static int determine_if_encrypted(FILE* in) {
    char magic[4] = "";
    fread(magic, 1, 4, in);
    fseek(in, 0, SEEK_SET);
    return strncmp(magic, "TL00", 4) == 0;
}

static void get_password(char* password) {
    printf("password: ");
    fgets(password, 256, stdin);
}

static void encrypt(FILE* in, FILE* out, char* password) {
    // hash password
    uint8_t password_hash[32];
    sha256(password, strlen(password), password_hash);

    // write header
    fwrite("TL00", 4, 1, out);
    fseek(out, 8, SEEK_SET);

    // determine seed
    uint32_t seed = time(NULL);
    musl_srand(seed);

    // store encrypted seed
    uint32_t encrypted_seed = seed;
    for (int i = 0; i < 8; i++) {
        encrypted_seed ^= ((uint32_t*) password_hash)[i];
    }
    fwrite(&encrypted_seed, 4, 1, out);

    // process chunks
    uint32_t checksum = 0;
    while (process_chunk(in, out, &checksum, 0));

    // write checksum
    fseek(out, 4, SEEK_SET);
    fwrite(&checksum, 4, 1, out);
}

static void decrypt(FILE* in, FILE* out, char* password, char* out_name) {
    // hash password
    uint8_t password_hash[32];
    sha256(password, strlen(password), password_hash);

    // read checksum
    uint32_t stored_checksum;
    fseek(in, 4, SEEK_SET);
    fread(&stored_checksum, 4, 1, in);

    // determine seed
    uint32_t seed;
    fread(&seed, 4, 1, in);
    for (int i = 0; i < 8; i++) {
        seed ^= ((uint32_t*) password_hash)[i];
    }

    // initialize rand
    musl_srand(seed);

    // process chunks
    uint32_t checksum = 0;
    while (process_chunk(in, out, &checksum, 1));

    // check checksum
    if (checksum != stored_checksum) {
        printf("error: checksum failed (wrong password?)\n");
        remove(out_name);
        return;
    }
}

static int process_chunk(FILE* in, FILE* out,
        uint32_t* checksum, int is_encrypted) {
    // read input
    uint8_t in_buffer[1024];
    uint8_t out_buffer[1024];
    int bytes_read = fread(in_buffer, 1, 1024, in);

    // encrypt each byte in buffer
    for (int i = 0; i < bytes_read; i++) {
        out_buffer[i] = in_buffer[i] ^ secure_rand8();

        int decoded_byte = (is_encrypted ? out_buffer[i] : in_buffer[i]);
        *checksum = (*checksum + decoded_byte) & 0x7fffffff;
    }

    // write output
    fwrite(out_buffer, bytes_read, 1, out);

    // stop at eof
    return bytes_read == 1024;
}
