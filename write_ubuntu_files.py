import os

programs = {
"program1.c": """#include <stdio.h>
#include <unistd.h>

int main()
{
    printf("PID = %d\\n", getpid());
    return 0;
}""",

"program2.c": """#include <stdio.h>
#include <unistd.h>

int main()
{
    fork();
    printf("Hello\\n");
    return 0;
}""",

"program3.c": """#include <stdio.h>
#include <unistd.h>

int main()
{
    pid_t pid;
    pid = fork();
    if(pid == 0)
        printf("I am Child\\n");
    else
        printf("I am Parent\\n");
    return 0;
}""",

"program4.c": """#include <stdio.h>
#include <unistd.h>

int main()
{
    pid_t pid;
    pid = fork();
    if(pid == 0)
    {
        printf("Child PID = %d\\n", getpid());
        printf("Parent PID = %d\\n", getppid());
    }
    else
    {
        printf("Parent PID = %d\\n", getpid());
        printf("Child PID = %d\\n", pid);
    }
    return 0;
}""",

"program5.c": """#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    pid_t pid = fork();
    if(pid == 0)
    {
        printf("Child Executing\\n");
    }
    else
    {
        wait(NULL);
        printf("Parent Executing\\n");
    }
    return 0;
}""",

"program6.c": """#include <stdio.h>
#include <unistd.h>

int main()
{
    fork();
    fork();
    printf("PID = %d\\n", getpid());
    return 0;
}""",

"program7.c": """#include <stdio.h>
#include <unistd.h>

int main()
{
    pid_t pid = fork();
    if(pid == 0)
    {
        printf("Child executing ls...\\n");
        execl("/bin/ls","ls","-l",NULL);
    }
    else
    {
        printf("Parent Waiting...\\n");
    }
    return 0;
}""",

"program8.c": """#include <stdio.h>
#include <unistd.h>

int main()
{
    int i;
    for(i=0;i<3;i++)
        fork();
    printf("PID = %d\\n",getpid());
    return 0;
}""",

"program9.c": """#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    char cmd[50];

    printf("Enter Linux Command: ");
    scanf("%s", cmd);

    pid_t pid = fork();

    if(pid < 0)
    {
        printf("Fork Failed\\n");
        return 1;
    }
    else if(pid == 0)
    {
        printf("\\nChild Process\\n");
        printf("Child PID : %d\\n", getpid());
        printf("Parent PID: %d\\n", getppid());

        execlp(cmd, cmd, NULL);

        perror("Command Execution Failed");
        exit(1);
    }
    else
    {
        printf("\\nParent Process\\n");
        printf("Parent PID : %d\\n", getpid());
        printf("Child PID  : %d\\n", pid);

        wait(NULL);

        printf("\\nChild Process Completed\\n");
    }

    return 0;
}"""
}

wsl_path = r"\\wsl$\Ubuntu\home\sri_charan\Fork"
os.makedirs(wsl_path, exist_ok=True)

for name, code in programs.items():
    file_path = os.path.join(wsl_path, name)
    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(code)
    print("Wrote", name, "to", file_path)
