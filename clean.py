import os

imp_patterns = [".git*",
               "keep*",
               "*.tex",
               "*.jpg",
               "*.png",
               "*.bib",
               "clean.py"
               ]

def match(pattern, string):
    # print(pattern, string)
    if pattern == "*":
        return True  # if pattern is "*" match all
    if "*" not in pattern:
        return pattern == string  # if pattern doesn't have a "*" match them directly
    if pattern[0] == "*":
        if not len(string):
            return False
        if pattern[1] == string[0]:
            return match(pattern[2:], string[1:])
        else:
            return match(pattern, string[1:])
    else:
        return pattern[0] == string[0] and match(pattern[1:], string[1:])

def not_keep(file):
    for imp_pattern in imp_patterns:
        if match(imp_pattern, file):
            return False
    return True

with open(".gitignore") as f:
    gitignore = [x for x in f.read().split("\n") if len(x) and not x.startswith("#")]
def clean(path = ".", delete = True):
    global gitignore
    l = os.listdir(path)
    to_delete = [x for x in l if not os.path.isdir(x) and not_keep(x)]
    for i in to_delete:
        if delete: os.remove(f"{path}/{i}")
        g = f"{path}/{i}"[2:]
        if g not in gitignore:
            gitignore.append(g)
    # print(f"Deleted {len(to_delete)} files in {path}")
    dirs = [name for name in l if os.path.isdir(name) and ".git" not in name]
    # print("One batch done\n")
    for dir in dirs:
        # print(f"looking into {path}/{dir}")
        clean(f"{path}/{dir}", delete)

if __name__ == "__main__":
    
    # Deleting with permission
    if input("Delete unnecessary files? (y/n) ") == "y":
        clean()
        print("Deleted", len(gitignore), "files in Total")
    else: clean(delete = False)
    
    
    # making a .gitignore file
    if input("Make a .gitignore file? (y/n) ") == "y":
        gitignore = "\n".join(gitignore)
        with open(".gitignore", "w") as f:
            f.write(gitignore)
    print(gitignore)