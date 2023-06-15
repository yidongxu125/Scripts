@echo version 1.0
@echo by Dongxu Yi
for %%f in (.\gjf\*.out .\gjf\*.mol .\gjf\*.mol2) do (
    Multiwfn "%%f" < gjf.txt 
    move ".\%%~nf.gjf" .\gjf\
)
