import os
import sys
import numpy as np
from  case_generator2 import _import_case
from smt.applications import EGO
from smt.surrogate_models import KPLS, KRG, KPLSK
from smt.utils.options_dictionary import OptionsDictionary
from smt.applications.application import SurrogateBasedApplication
from smt.utils.misc import compute_rms_error
from smt.sampling_methods import LHS

ng=sys.argv[1]
print('Function ', ng)
dir_name='./results/'+ng+'/'
base_save=ng
suffix_xdoe = '_xdoe.npy'
suffix_ydoe = '_ydoe.npy'
suffix_xval = '_xval.npy'
suffix_yvaltrue = '_yvaltrue.npy'
suffix_yvalest = '_yvalestimated.npy'


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



#nb_doe=20
#for DOE in [30,50,100,200,300]:   

nb_doe=1
for DOE in [30]:   

    for k in range(nb_doe) :
        n_doe=2*DOE
        d=LHS(xlimits=s._relax_limits(xlimits), criterion="ese")
        x_data=d(n_doe)
        x_data=s._project_values(x_data)
        y_data = f(s._assign_labels(x_data,xlimits))
        x_doe=x_data[0:int(n_doe/2)]
        y_doe=y_data[0:int(n_doe/2)]
        filename= os.path.join(dir_name, base_save+"_" + str(k) +"_modval_DOE" +str(DOE)+ suffix_xdoe)
        np.save(filename, x_doe) 
        filename= os.path.join(dir_name, base_save+"_"+  str(k)  +"_modval_DOE" +str(DOE)+ suffix_ydoe)
        np.save(filename, y_doe) 
        # half the point for the validation
        x_val=x_data[int(n_doe/2):]
        y_val_true=y_data[int(n_doe/2):]
        filename= os.path.join(dir_name, base_save+"_" + str(k) +"_modval_DOE" +str(DOE)+suffix_xval)
        np.save(filename, x_val) 
        filename= os.path.join(dir_name, base_save+"_"+  str(k)  +"_modval_DOE" +str(DOE)+suffix_yvaltrue)
        np.save(filename, y_val_true) 
        
              
        s.set_training_values(x_doe, y_doe)
        s.train()
        y_gp =s.predict_values(x_val)
        filename= os.path.join(dir_name, base_save+"_"+  str(k)  +"_modval_DOE" +str(DOE)+suffix_yvalest)
        np.save(filename, y_gp) 
        
        
   




