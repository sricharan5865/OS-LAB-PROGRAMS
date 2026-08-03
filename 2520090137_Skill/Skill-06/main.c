// Skill 06: Process Replacement using exec() family
#include <stdio.h>
#include <unistd.h>

int main() {
    char *args[] = {"ls", "-l", NULL};
    printf("Executing ls via execvp...\n");
    execvp(args[0], args);
    perror("execvp failed");
    return 0;
}