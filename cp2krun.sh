# cp2k allrun 
# Version 1.0
# By Yidongxu
mpirun -np 35 cp2k.popt formA_nodisorder.inp |tee formA_nodisorder.out
mpirun -np 35 cp2k.popt formD_nodisorder.inp |tee formD_nodisorder.out