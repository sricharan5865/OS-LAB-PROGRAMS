# Skill Activity 02: Linux Shell & Directory Navigation Commands

## Aim & Overview
Mastering Linux shell commands: pwd, ls, cd, mkdir, rmdir, cp, mv, rm, cat, echo, find, history, and shell scripting basics.

## Implementation (`main.c`)
```c
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
```

## Compilation & Execution
```bash
make
./main
```

## Output & Verification
```text
$ pwd
/home/student/2520090137_OSSP/2520090137_Skill/Skill-02
$ ./main
Current Working Directory: /home/student/2520090137_OSSP/2520090137_Skill/Skill-02
```

## Key Learning Points
Practiced Linux file manipulation, directory tree navigation, and standard terminal utility commands.
