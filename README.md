# Operating Systems and System Programming (OSSP) Course Portfolio
**Team Name**: 2520090137  
**GitHub Repository**: [sricharan5865/OS-LAB-PROGRAMS](https://github.com/sricharan5865/OS-LAB-PROGRAMS)

---

## 📁 Repository Structure

```
2520090137_OSSP/
├── 2520090137_Practical/
│   ├── Practical-01/ (Hardware Resources & OS Abstraction)
│   ├── Practical-02/ (File Copy Utility System Calls)
│   ├── Practical-03/ (Process States & Lifecycle)
│   ├── Practical-04/ (Parent-Child Sync waitpid)
│   ├── Practical-05/ (Unnamed Pipe IPC)
│   ├── Practical-06/ (Named Pipe FIFO IPC)
│   ├── Practical-07/ (Process Memory Layout Inspection)
│   ├── Practical-08/ (Dynamic Heap Allocation malloc/realloc)
│   ├── Practical-09/ (Buffered vs Low-Level I/O Performance)
│   ├── Practical-10/ (File Metadata & Inode Structure)
│   ├── Practical-11/ (Multi-Threading & Race Conditions)
│   └── Practical-12/ (Semaphore Thread Synchronization)
│
├── 2520090137_Skill/
│   ├── Skill-01/ (Linux VM & GCC Toolchain)
│   ├── Skill-02/ (Linux Shell Commands)
│   ├── Skill-03/ (Git Workflow & Repo Structure)
│   ├── Skill-04/ (Shell Architecture & Makefile Automation)
│   ├── Skill-05/ (Process Creation fork)
│   ├── Skill-06/ (Process Replacement execvp)
│   ├── Skill-07/ (Process Sync wait)
│   ├── Skill-08/ (Process Tree Hierarchy)
│   ├── Skill-09/ (System Call Tracing strace)
│   └── Skill-10/ (Interactive Mini Shell)
│
└── ForgeOS/ (Semester Project)
    ├── Shellforge/ (User-Space Unix Shell)
    └── NanoKernel/ (Kernel-Space Scheduler & PCB Module)
```

---

## 🚀 Practical Experiments Summary

| Folder | Topic / Practical Name | Key System Calls / APIs | Artifacts Included |
|---|---|---|---|
| `Practical-01` | Hardware Resources & OS Abstraction | `fork()`, `exec()`, `wait()` | C Code, Makefile, README, Screenshots, DOCX Report |
| `Practical-02` | File Copy Utility | `open()`, `read()`, `write()`, `close()` | C Code, Makefile, README, Screenshots, DOCX Report |
| `Practical-03` | Process States & Lifecycle | `fork()`, `getpid()`, `getppid()`, `sleep()` | C Code, Makefile, README, Screenshots, DOCX Report |
| `Practical-04` | Parent-Child Sync via waitpid() | `fork()`, `waitpid()`, `WEXITSTATUS()` | C Code, Makefile, README, Screenshots, DOCX Report |
| `Practical-05` | Unnamed Pipe IPC | `pipe()`, `read()`, `write()` | C Code, Makefile, README, Screenshots, DOCX Report |
| `Practical-06` | Named Pipe (FIFO) IPC | `mkfifo()`, `open()`, `read()` | C Code, Makefile, README, Screenshots, DOCX Report |
| `Practical-07` | Process Memory Layout | Pointer inspection (Text, BSS, Heap, Stack) | C Code, Makefile, README, Screenshots, DOCX Report |
| `Practical-08` | Dynamic Heap Memory | `malloc()`, `realloc()`, `free()` | C Code, Makefile, README, Screenshots, DOCX Report |
| `Practical-09` | Low-Level vs Buffered I/O | `write()` vs `fputs()`, stream buffers | C Code, Makefile, README, Screenshots, DOCX Report |
| `Practical-10` | File Metadata & Inode | `stat()`, `st_ino`, `st_nlink` | C Code, Makefile, README, Screenshots, DOCX Report |
| `Practical-11` | Multi-Threading & Concurrency | `pthread_create()`, `pthread_join()` | C Code, Makefile, README, Screenshots, DOCX Report |
| `Practical-12` | Semaphore Synchronization | `sem_init()`, `sem_wait()`, `sem_post()` | C Code, Makefile, README, Screenshots, DOCX Report |

---

## 🛠️ Skill Activities Summary

| Folder | Skill Activity Title | Core Concept | Artifacts |
|---|---|---|---|
| `Skill-01` | Linux Environment & GCC Setup | GCC Build Toolchain | C Code, Makefile, README, Screenshots, DOCX Report |
| `Skill-02` | Linux Shell Commands | Navigation & File Ops | C Code, Makefile, README, Screenshots, DOCX Report |
| `Skill-03` | Git Version Control | Commit & Staging Flow | C Code, Makefile, README, Screenshots, DOCX Report |
| `Skill-04` | Makefile Automation | Build Targets (`all`, `clean`) | C Code, Makefile, README, Screenshots, DOCX Report |
| `Skill-05` | Process Creation `fork()` | Address Space Cloning | C Code, Makefile, README, Screenshots, DOCX Report |
| `Skill-06` | Process Replacement `execvp()` | Context Swapping | C Code, Makefile, README, Screenshots, DOCX Report |
| `Skill-07` | Process Sync `wait()` | Parent Synchronization | C Code, Makefile, README, Screenshots, DOCX Report |
| `Skill-08` | Process Tree Analysis | Hierarchy & `pstree` | C Code, Makefile, README, Screenshots, DOCX Report |
| `Skill-09` | System Call Tracing | `strace` Diagnostics | C Code, Makefile, README, Screenshots, DOCX Report |
| `Skill-10` | Mini Shell Implementation | User Space Shell Loop | C Code, Makefile, README, Screenshots, DOCX Report |

---

## 💻 Course Semester Project: `ForgeOS`

1. **Shellforge (User Space)**: Built interactive Unix-style shell supporting built-in commands (`cd`, `exit`), executable resolution, and parent-child process management.
2. **NanoKernel (Kernel Space)**: Developed simulated kernel dispatcher managing Process Control Blocks (PCB) and priority scheduling.

---
