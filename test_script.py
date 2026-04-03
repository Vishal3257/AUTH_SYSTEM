import subprocess

# Run pip install
result1 = subprocess.run(["python", "-m", "pip", "install", "setuptools", "--user"], capture_output=True, text=True)
with open("pip_out.txt", "w", encoding="utf-8") as f:
    f.write("STDOUT:\n")
    f.write(result1.stdout)
    f.write("\nSTDERR:\n")
    f.write(result1.stderr)

# Run manage.py check
result2 = subprocess.run(["python", "manage.py", "check"], capture_output=True, text=True)
with open("check_out.txt", "w", encoding="utf-8") as f:
    f.write("STDOUT:\n")
    f.write(result2.stdout)
    f.write("\nSTDERR:\n")
    f.write(result2.stderr)

import sys
with open("python_info.txt", "w", encoding="utf-8") as f:
    f.write(sys.executable)
    f.write("\n")
    f.write(sys.version)

