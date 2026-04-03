import subprocess

result = subprocess.run(["python", "manage.py", "check"], capture_output=True, text=True)
with open("check_out_verify.txt", "w", encoding="utf-8") as f:
    f.write(result.stdout)
    f.write("\nSTDERR:\n")
    f.write(result.stderr)
