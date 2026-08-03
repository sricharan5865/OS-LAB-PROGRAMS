import os, shutil

repo_dir = r"C:\Users\sri charan\.gemini\antigravity\scratch\2520090137_OSSP\2520090137_Practical"

for i in range(1, 13):
    target_folder = os.path.join(repo_dir, f"Practical-{i:02d}")
    os.makedirs(target_folder, exist_ok=True)
    
    make_content = f"CC = gcc\nCFLAGS = -Wall -Wextra -std=c99 -pthread\nTARGET = practical{i}\n\nall: $(TARGET)\n\n$(TARGET): Practical{i}.c\n\t$(CC) $(CFLAGS) -o $(TARGET) Practical{i}.c\n\nclean:\n\trm -f $(TARGET) *.o\n"
    with open(os.path.join(target_folder, "Makefile"), "w", encoding="utf-8", newline="\n") as f:
        f.write(make_content)

    readme_content = f"# Practical-{i:02d}\n\nOSSP Practical Experiment {i}.\n"
    with open(os.path.join(target_folder, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(readme_content)

print("Makefiles and READMEs created for all Practical subfolders.")
