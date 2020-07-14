import os
import subprocess

namefun=['Branin_5','Set_1','Set_2','Wong1','Branin_1','Branin_2','Goldstein_1','Cos_1','Spiral','EVD52','Rosen-Suzuki']


namefun=['Rosen-Suzuki']
    
for name in namefun:
    runfile("optim_cases.py", args=name)
    #os.startfile("optim_scipy_cobyla_Gxx_casegenerator2.py ")
    
    
    
#for name in namefun:
#    runfile("model_cases.py", args=name)
    
    
    
       
  