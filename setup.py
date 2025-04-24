from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["fitz", "PyPDF2", "openpyxl"],
    "include_files": [("gui/assets", "gui/assets")],
    "excludes": [],
    "includes": ["fitz"],  # ← ¡esto es importante!
}

setup(
    name="DIMEx",
    version="1.0",
    description="Visor PDF y Excel",
    options={"build_exe": build_exe_options},
    executables=[Executable("DIMEx.py", base="Win32GUI", icon="gui/assets/logo.png")]
)
