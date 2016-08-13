import os 
str = os.popen("pwd").read()
print str
str = os.popen("""
/Applications/MATLAB_R2013a.app/bin/matlab  -nojvm -nodesktop -nodisplay -r /Users/jzd/Documents/MATLAB/test""").read()
print str

