import sys
import os
from cx_Freeze import setup, Executable
import matplotlib

# Dependencies are automatically detected, but it might need fine tuning.

build_exe_options = {
    "packages": ["os", "sys","pickle","datetime","numpy","matplotlib","PIL","math"], 
    "include_files":["includes\images\oldLogoSDJ.jpeg"],
    "includes": ["tkinter"], 
    "optimize": 1
}


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "MonSuperProgramme",
    version = "1.7.5",
    description = "Calcule les coeficients d'une equation du second degre",
    options = {"build_exe": build_exe_options},
    executables = [Executable("IHMSecondaryEquation.py", base = base)]
)