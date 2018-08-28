#include <stdio.h>
#include <unistd.h>
#include <time.h>

void hairy () {
   printf("YER A WIZARD HARRY!!1!\n");
   system("/bin/cat flag");
}

int main(int argc, const char *argv[]) {

   setbuf(stdout, NULL);  //because xinetd and netcat
   srand(time(NULL));

   volatile int wizard = rand();
   char name[6] = {};

   printf("Enter your name:");
   scanf("%5s", &name);

   printf("Welcome to the Hackademy, ");
   printf(name);
   printf("\nTo prove yourself worthy of being a wizard, you must first answer this question correctly.\n"
         "What number am I thinking of?\n");

   int lolfuck = 0;
   scanf("%d", &lolfuck);

   if (wizard == lolfuck) {
      hairy();
   } else {
      printf("Not quite!\n");
      printf("answer is %d", wizard);
   }

   return 0;
}
