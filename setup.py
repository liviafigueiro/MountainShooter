from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pygame"],
    "include_files": ["asset"],
    "excludes": ["tkinter"],
}

executables = [
    Executable(
        "main.py",
        base="gui",  # remove o console preto
    )
]

setup(
    name="MountainShooter",
    version="1.0",
    description="Mountain Shooter Game",
    options={"build_exe": build_exe_options},
    executables=executables
)