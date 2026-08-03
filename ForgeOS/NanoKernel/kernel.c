#include <stdio.h>

void nanokernel_init(void) {
    printf("[NanoKernel] Initializing ForgeOS core kernel space components...\n");
}

int main(void) {
    nanokernel_init();
    printf("[NanoKernel] Core system booted successfully.\n");
    return 0;
}
