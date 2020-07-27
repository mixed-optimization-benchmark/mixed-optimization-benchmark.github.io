import os
import sys
import numpy as np
from  case_generator2 import _import_case
from smt.applications import EGO
from smt.surrogate_models import KPLS, KRG, KPLSK
from smt.utils.options_dictionary import OptionsDictionary
from smt.applications.application import SurrogateBasedApplication
from smt.utils.misc import compute_rms_error

ng=sys.argv[1]
print('Function ', ng)
dir_name='./results/'+ng+'/'
base_save=ng
suffix_xsave = '_xsave.npy'
suffix_ysave = '_ysave.npy'

try:
    os.mkdir(dir_name)
except OSError:
    pass
case=_import_case(ng)()

xlimits = case['vars']['bounds']
vartype=case['vars']['vartype']
f=case['f_obj']

tunnel=0
criterion = "EI"  #'EI' or 'SBO' or 'UCB'
qEI = "KB"
surr=  case["models"]["type"]

if surr== 'KPLS':
    n_comp=  case["models"]["n_components"]
    s=KPLS(print_global=False,n_comp=n_comp,vartype=vartype)
elif surr=='KRG' :
    s=KRG(print_global=False,vartype=vartype)


#20,5,50
n_optim=20
n_doe=5
n_iter = 50
print(n_iter)
for k in range(n_optim):
    y_save=np.zeros(n_iter)
    
    ego = EGO(n_doe=n_doe,n_iter=n_iter, criterion=criterion,xlimits=xlimits,qEI=qEI,tunnel=0, surrogate=s )
    x_optk, y_optk, ind_bestk, x_datak, y_datak, x_doek, y_doek = ego.optimize(fun=f)
    y_save=y_datak
    x_save=x_datak
    filename= os.path.join(dir_name, base_save+"_" + str(k) +"_optim"+ suffix_xsave)
    np.save(filename, x_save) 
    filename= os.path.join(dir_name, base_save+"_"+  str(k)  +"_optim" +suffix_ysave)
    np.save(filename, y_save) 
    
  
#filename= os.path.join(dir_name, base_save+"_"+"1" + suffix_ysave)
#§yl=np.load(filename) 

