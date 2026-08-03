#include <stdio.h>

int main() {
    FILE *f = fopen("sample.txt", "w");
    if (f) {
        fputs("Hello World from OSSP Practical System Call Tracing\n", f);
        fclose(f);
    }
    printf("sample.txt prepared. Run: strace cat sample.txt\n");
    return 0;
}