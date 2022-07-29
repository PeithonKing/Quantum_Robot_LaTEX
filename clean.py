from os import listdir, remove

with open(".gitignore") as f:
    imp_patterns = [".git"] + [x[1:] for x in f.read().split()[1:]]

def search(exps, s):
    exps = list(exps)
    s = list(s)
    while len(exps) and len(s):
        # print("".join(exps), "\t\t", "".join(s))
        if exps[0] == "*":
            if len(exps) == 1:
                return True
            if s[0] == exps[1]:
                exps.pop(0)
                exps.pop(0)
            s.pop(0)
                
        else:
            if s[0] == exps[0]:
                exps.pop(0)
                s.pop(0)
            else:
                return False
    if not len(exps) or exps == ["*"]:
        return True
    return False

def not_keep(file):
    for imp_pattern in imp_patterns:
        if search(imp_pattern, file):
            return False
    return True

to_delete = [x for x in listdir() if not_keep(x)]

for i in to_delete: remove(i)

print(f"removed {len(to_delete)} files")