#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAZE_SIZE 17
char display[MAZE_SIZE][MAZE_SIZE];
#define GOLD_X 14
#define GOLD_Y 5
char labyrinth[MAZE_SIZE][MAZE_SIZE] = {
    "#################",
    "# # # # #      ##",
    "# ### ### #######",
    "#       # #     #",
    "#######   # #####",
    "#     # ###  #$##",
    "## ##   #   #####",
    "##    # # #  # ##",
    "####### #### # ##",
    "##    #      # ##",
    "#  # ## ###### ##",
    "# ##    #    # ##",
    "# ####### ####  #",
    "#    #       ## #",
    "## # # # ###  # #",
    "####   #    #   #",
    "#################",
};
  
char *data = "DATA__la_symbol_ptr";

int main (int argc, char *argv[]) {

    setbuf(stdout, NULL);

    for (int y = 0; y < MAZE_SIZE; y++) {
        for (int x = 0; x < MAZE_SIZE; x++) {
            display[y][x] = ' ';
        }
    }
    display[GOLD_Y][GOLD_X] = '$';
    char move[8];
    move[7] = 1;
    move[6] = 1;

    int player_x = move[6]; int player_y = move[7];
    
    while (player_x != GOLD_X || player_y != GOLD_Y) {
        display[player_y-1][player_x]   = labyrinth[player_y-1][player_x]; 
        display[player_y-1][player_x-1] = labyrinth[player_y-1][player_x-1]; 
        display[player_y-1][player_x+1] = labyrinth[player_y-1][player_x+1]; 
        display[player_y+1][player_x]   = labyrinth[player_y+1][player_x]; 
        display[player_y+1][player_x-1] = labyrinth[player_y+1][player_x-1]; 
        display[player_y+1][player_x+1] = labyrinth[player_y+1][player_x+1]; 
        display[player_y]  [player_x]   = labyrinth[player_y]  [player_x]; 
        display[player_y]  [player_x-1] = labyrinth[player_y]  [player_x-1]; 
        display[player_y]  [player_x+1] = labyrinth[player_y]  [player_x+1]; 
        for (int y = 0; y < MAZE_SIZE; y++) {
            for (int x = 0; x < MAZE_SIZE; x++) {
                if (x == player_x && y == player_y) {
                    printf("@");
                } else {
                    printf("%c", display[y][x]);
                }
            }
            printf("\n");
        }
        printf("Enter a direction to move (north, south, east or west):");
        int counter = 0;
        int c;
        while ((c = getchar()) != EOF) {
            if (c == '\n') break;
            move[counter] = c;
            counter++;
        }
        if (c == EOF) {
            printf("Bye!\n");
            exit(0);
        }
        player_x = move[6]; player_y = move[7];
        move[counter] = '\0';
        if (strcmp(move,"north") == 0) {
            if (labyrinth[player_y-1][player_x] == '#') {
                printf("That way is blocked!\n");
            } else player_y--;
        } else if (strcmp(move,"west") == 0) {
            if (labyrinth[player_y][player_x-1] == '#') {
                printf("That way is blocked!\n");
            } else player_x--;
        } else if (strcmp(move,"east") == 0) {
            if (labyrinth[player_y][player_x+1] == '#') {
                printf("That way is blocked!\n");
            } else player_x++;
        } else if (strcmp(move,"south") == 0) {
            if (labyrinth[player_y+1][player_x] == '#') {
                printf("That way is blocked!\n");
            } else player_y++;
        } else {
            printf("Invalid move!\n");
        }
        move[6] = (char)player_x;
        move[7] = (char)player_y;
    }
    const char *s = getenv("FLAG");
    if(s == NULL) s = "";
    printf("To get the real amulet you have to play the real NetHack :P \n All you get here is a flag:\n %s \n", s);
    return 0;
}
