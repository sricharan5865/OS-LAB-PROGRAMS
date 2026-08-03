// Skill 02: Linux Shell Usage & Directory Traversal
#include <stdio.h>
#include <unistd.h>

int main() {
    char cwd[1024];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        printf("Current Working Directory: %s\n", cwd);
    }
    return 0;
}