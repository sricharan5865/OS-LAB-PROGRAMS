import os, shutil

repo_dir = r"C:\Users\sri charan\.gemini\antigravity\scratch\2520090137_OSSP"
prac_root = os.path.join(repo_dir, "2520090137_Practical")

# Remove extra Practical-13 to Practical-24 folders
for i in range(13, 25):
    folder_path = os.path.join(prac_root, f"Practical-{i:02d}")
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Removed old folder: {folder_path}")

print("Cleaned up practical directory to exactly 12 practicals.")
