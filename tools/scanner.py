import os

def scan(path):
    files=[]
    for root,dirs,names in os.walk(path):
        dirs[:]=[d for d in dirs if d not in {".git",".venv","__pycache__","node_modules"}]
        for n in names:
            files.append(os.path.relpath(os.path.join(root,n),path))
    return files

def scan_target(path):
    files=scan(path)
    source=[]
    for rel in files:
        if os.path.splitext(rel)[1].lower() in {".js",".ts",".py",".java",".sql",".json",".yml",".yaml",".md",".txt"}:
            try:
                with open(os.path.join(path,rel),"r",encoding="utf-8",errors="ignore") as f:
                    source.append((rel,f.read()))
            except OSError:
                pass
    return {"files":files,"source":source}
