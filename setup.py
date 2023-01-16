import cx_Freeze, sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py", base=base, targetName="SFTP-GUI")]

cx_Freeze.setup(
    name="SFTP-GUI",
    options={"build_exe": {"packages": ["tkinter"], "include_files": [
        "exl.ico", "reset.ico","pswrd.ico","sftp_module.py"
    ]}},
    version="1.0",
    description="DESCRIBE YOUR PROGRAM",
    executables=executables
)