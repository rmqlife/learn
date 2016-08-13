import os
import sys

def load_files(root='data', suffix=".png"):
    for r, dirs, files in os.walk(root):
        for f in files:
            if f.lower().endswith(suffix):
                yield os.path.join(r, f)

def rename(paths, root='data_new'):
	num=0
	if not os.path.exists(root):
		os.mkdir(root)

	for path in paths:
		ext = os.path.splitext(path)[1].lower()
		new_path= os.path.join(root,str(num)+ext)
		yield new_path
		num=num+1

def copy_all(paths,new_paths):
	import shutil
	assert len(paths)==len(new_paths)
	for i in range(len(paths)):
		shutil.copy(paths[i],new_paths[i])

paths=list(load_files())
new_paths=list(rename(paths))
# print new_paths
copy_all(paths,new_paths)

