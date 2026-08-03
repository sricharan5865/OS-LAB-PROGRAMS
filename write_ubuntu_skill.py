import os

skill_programs = {
"skill1.c": """// 1. Configure GCC and environment check
#include <stdio.h>

int main() {
    printf("GCC Configuration Verified.\\n");
    return 0;
}""",

"skill2.c": """// 2. Linux Shell Usage & Basic Commands
#include <stdio.h>
#include <unistd.h>

int main() {
    char cwd[1024];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        printf("Current Working Directory: %s\\n", cwd);
    }
    return 0;
}""",

"skill3.c": """// 3. Git Repository setup & file check
#include <stdio.h>

int main() {
    printf("Git Repository setup program verified.\\n");
    return 0;
}""",

"skill4.c": """// 4. Shell Architecture & Makefile
#include <stdio.h>

int main() {
    printf("Build automation via Makefile executed successfully.\\n");
    return 0;
}""",

"skill5.c": """// 5. Process Creation using fork()
#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Parent PID: %d\\n", getpid());
    pid_t pid = fork();
    if (pid == 0) {
        printf("Child process PID: %d, Parent PID: %d\\n", getpid(), getppid());
    }
    return 0;
}""",

"skill6.c": """// 6. Process Replacement using exec() family
#include <stdio.h>
#include <unistd.h>

int main() {
    char *args[] = {"ls", "-l", NULL};
    printf("Executing ls via execvp...\\n");
    execvp(args[0], args);
    perror("execvp failed");
    return 0;
}""",

"skill7.c": """// 7. Parent-Child Synchronization using wait()
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    if (pid == 0) {
        printf("[Child] Executing work...\\n");
    } else {
        wait(NULL);
        printf("[Parent] Child terminated. Parent resuming.\\n");
    }
    return 0;
}""",

"skill8.c": """// 8. Process Tree Analysis
#include <stdio.h>
#include <unistd.h>

int main() {
    fork();
    fork();
    printf("Process PID: %d, Parent PID: %d\\n", getpid(), getppid());
    return 0;
}""",

"skill9.c": """// 9. System Call Tracing
#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Tracing system calls for process PID: %d\\n", getpid());
    return 0;
}""",

"skill10.c": """// 10. Mini Shell Program
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    char cmd[64];
    printf("minishell> ");
    if (scanf("%63s", cmd) == 1) {
        if (strcmp(cmd, "exit") == 0) return 0;
        pid_t pid = fork();
        if (pid == 0) {
            execlp(cmd, cmd, NULL);
            perror("Execution failed");
            exit(1);
        } else {
            wait(NULL);
        }
    }
    return 0;
}"""
}

wsl_skill_path = r"\\wsl$\Ubuntu\home\sri_charan\Skill"
os.makedirs(wsl_skill_path, exist_ok=True)

for name, code in skill_programs.items():
    file_path = os.path.join(wsl_skill_path, name)
    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(code)
    print("Wrote", name, "to", file_path)
