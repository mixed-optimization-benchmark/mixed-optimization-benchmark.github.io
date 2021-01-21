import numpy as np
from smt.applications.mixed_integer import (
    FLOAT,
    INT,
    ENUM,
    MixedIntegerSamplingMethod,
    MixedIntegerContext,
    cast_to_mixed_integer
)
# Objective function
def f_obj(X) :
    """
    s01 objective

    Parameters
    ----------
    point: array_like
        point to evaluate
    """
    
    xtypes = [FLOAT,FLOAT,FLOAT,FLOAT,FLOAT,FLOAT,FLOAT, (ENUM,5)]
    xlimits = np.array([ [-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],["1","2","3","4","5"]],dtype='object')
    mixint = MixedIntegerContext(xtypes, xlimits)
    X_=np.zeros((X.shape),dtype=object)
    i=0
    for x in X : 
        X_[i]=mixint.cast_to_mixed_integer(x)
        i+=1
    
    x1=X_[:,0].astype(float)
    x2=X_[:,1].astype(float)
    
    x3=X_[:,2].astype(float)
    x4=X_[:,3].astype(float)
    x5=X_[:,4].astype(float)
    x6=X_[:,5].astype(float)
    x7=X_[:,6].astype(float)
    
  #  caté 1
    c=X_[:,7]
    c1=(c=='1')
    c2=(c=='2')
    c3=(c=='3')
    c4=(c=='4')
    c5=(c=='5')
    
    if (np.size(c1)==(np.sum(c1)+np.sum(c2)+np.sum(c3)+np.sum(c4)+np.sum(c5))):
        y=1*(  (x1-10)**2  +5* (x2-12)**2+x3**4 +3*(x4-11)**2+10*x5**6+7*x6**2+2*x7**4-4*x6*x7 -10*x6-8*x7 ) +\
         c2*( 10*(2*x1**2+3*x2**4+x3+4*x4**2+5*x5-127) ) + \
         c3*( 10*(7*x1+3*x2+10*x3**2+x4-x5-282) )+ \
         c4*( 10*(23*x1+x2**2+6*x6**2-8*x7-196) ) + \
         c5*( 10*(4*x1**2+x2**2-3*x1*x2+ 2*x3**2+ 5*x6-11*x7) ) 
    return y
def get_case():
    """
    Get a dictionnary to run the G04 case

    Returns
    -------
    dic:
        'vars': list of design variables 
        'f_obj': function to evaluate the objective
        'sol': solution of the  problem
        'models': dictionary of settings for the default model

    """
    
         # default model
    mod_obj = {
        "type": "KPLS",
        "corr": "squar_exp",
        "n_components": 2,
    }
    
    
    # design variables
    xtypes = [FLOAT,FLOAT,FLOAT,FLOAT,FLOAT,FLOAT,FLOAT, (ENUM,5)]
    xlimits = np.array([ [-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],["1","2","3","4","5"]],dtype='object')
  
    design_variables={"xtypes":xtypes, "bounds": xlimits}
           
   # solution
    sol = {"value": -2389.627479486391, "tol": 1e-6}
    
    case = {
        "models": mod_obj , 
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
