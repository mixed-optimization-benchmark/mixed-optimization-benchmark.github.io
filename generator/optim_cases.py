import os
import sys
import numpy as np
from  case_generator2 import _import_case
from smt.applications import EGO
from smt.surrogate_models import KPLS, KRG, KPLSK
from smt.utils.options_dictionary import OptionsDictionary
from smt.applications.application import SurrogateBasedApplication
from smt.utils.misc import compute_rms_error
from smt.applications.mixed_integer import (
    FLOAT,
    INT,
    ENUM,
    MixedIntegerSamplingMethod,
    MixedIntegerContext,
    cast_to_mixed_integer
)
from smt.sampling_methods import LHS

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
xtypes=case['vars']['xtypes']
f=case['f_obj']

criterion = "EI"  #'EI' or 'SBO' or 'UCB'
qEI = "KB"

surr=  case["models"]["type"]
corr=  case["models"]["corr"]
if surr== 'KPLS':
    n_comp=  case["models"]["n_components"]
    s=KPLS(print_global=False,n_comp=n_comp,corr=corr,eval_noise=True)
elif surr=='KRG' :
    s=KRG(print_global=False,corr=corr)

n_doe=3

#20,5,50
n_optim=2
n_iter = 20
for k in range(n_optim):
    mixint = MixedIntegerContext(xtypes, xlimits)
    sampling = mixint.build_sampling_method(LHS, criterion="ese")
    x_doe=sampling(n_doe)
    y_doe=f(x_doe)
    y_save=np.zeros(n_iter)
    ego = EGO(xdoe=x_doe,ydoe=y_doe, n_iter=n_iter, criterion=criterion,xlimits=xlimits,
    xtypes=xtypes, surrogate=s, random_state=42)
    x_optk, y_optk, ind_bestk, x_datak, y_datak = ego.optimize(fun=f)
    y_save=y_datak
    x_save=x_datak
    filename= os.path.join(dir_name, base_save+"_" + str(k) +"_optim"+ suffix_xsave)
    np.save(filename, x_save) 
    filename= os.path.join(dir_name, base_save+"_"+  str(k)  +"_optim" +suffix_ysave)
    np.save(filename, y_save) 
    

#filename= os.path.join(dir_name, base_save+"_"+"1" + suffix_ysave)
#§yl=np.load(filename) 

