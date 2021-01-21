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
    xtypes=[FLOAT,FLOAT,FLOAT,(ENUM,6)]
    xlimits = np.array([[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],['1','2','3','4','5','6']],dtype='object')
    mixint = MixedIntegerContext(xtypes, xlimits)
    X_=np.zeros((X.shape),dtype=object)
    i=0
    for x in X : 
        X_[i]=mixint.cast_to_mixed_integer(x)
        i+=1
    
    x1=X_[:,0].astype(float)
    x2=X_[:,1].astype(float)
    x3=X_[:,2].astype(float)
  #  caté 1
    c=X_[:,3]
    c1=(c=='1')
    c2=(c=='2')
    c3=(c=='3')
    c4=(c=='4')
    c5=(c=='5')
    c6=(c=='6')
    
    
    if (np.size(c1)==(np.sum(c1)+np.sum(c2)+np.sum(c3)+np.sum(c4)+np.sum(c5)+np.sum(c6))):
        y= c1*(x1**2+x2**2+x3**2-1)+c2*(x1**2+x2**2+(x3-2)**2)+c3*(x1+x2+x3-1)+\
           c4*(x1+x2-x3+1)+c5*(2*x1**3+6*x2**2+2*(5*x3-x1+1)**2)+c6*(x1**2-9*x3)
        
        
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
    xtypes=[FLOAT,FLOAT,FLOAT,(ENUM,6)]
    xlimits = np.array([[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],['1','2','3','4','5','6']],dtype='object')
    design_variables={"xtypes":xtypes, "bounds": xlimits}
           
   # solution
    sol = {"value": -249.43247170013404, "tol": 1e-6}
    
    case = {
        "models": mod_obj , 
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
