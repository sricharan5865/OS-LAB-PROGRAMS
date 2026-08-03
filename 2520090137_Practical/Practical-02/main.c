// Command execution script for hardware & OS service investigation
// uname -a, lscpu, lsblk, ps -ef, top
#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("--- OS & Hardware Services Information ---\n");
    system("uname -a");
    system("lscpu | head -n 10");
    system("lsblk");
    return 0;
}