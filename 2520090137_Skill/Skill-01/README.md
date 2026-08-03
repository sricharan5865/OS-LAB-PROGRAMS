# Skill Activity 01: Linux Environment & GCC Toolchain Setup

## Aim & Overview
Installing Linux VM/WSL, terminal orientation, filesystem hierarchy navigation, GCC compiler setup, and C compilation.

## Implementation (`main.c`)
```c
// Skill 01: GCC Configuration & Environment Verification
#include <stdio.h>

int main() {
    printf("GCC Compiler & Linux Environment Verified.\n");
    return 0;
}
```

## Compilation & Execution
```bash
make
./main
```

## Output & Verification
```text
$ gcc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
$ gcc main.c -o skill1
$ ./skill1
GCC Compiler & Linux Environment Verified.
```

## Key Learning Points
Verified GCC toolchain installation and environment setup for compiling system programming C binaries.
