import cx_Freeze

executables = [
    cx_Freeze.Executable(script="main.py", icon="recursos/funcoes/icone.ico")
]
cx_Freeze.setup(
    name = "Trabalho Corrida",                                                                
    options = {
        "build_exe":{
            "packages":["pygame"],
            "include_files":["recursos"]
        }
    }, executables =  executables
)