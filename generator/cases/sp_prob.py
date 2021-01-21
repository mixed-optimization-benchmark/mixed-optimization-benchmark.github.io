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
    
    xtypes=[FLOAT,FLOAT,(ENUM,2)]
    xlimits = np.array([[-5.0,5.0],[-5.0,5.0],["1","2"]],dtype='object')
    mixint = MixedIntegerContext(xtypes, xlimits)
    X_=np.zeros((X.shape),dtype=object)
    i=0
    for x in X : 
        X_[i]=mixint.cast_to_mixed_integer(x)
        i+=1
    
    
    x1=X_[:,0].astype(float)
    x2=X_[:,1].astype(float)
 
  #  caté 1
    c=X_[:,2]
    c1= (c=='1')
    c2=(c=='2')
    
    
    if (np.size(c1)==(np.sum(c1)+np.sum(c2))):
        y=0.005*(x1**2+x2**2)+\
          c1*( (x1-np.sqrt(x1**2+x2**2)*np.cos(np.sqrt(x1**2+x2**2)))**2 )+\
          c2*( (x2-np.sqrt(x1**2+x2**2)*np.sin(np.sqrt(x1**2+x2**2)))**2 )
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
        "type": "KRG",
        "corr": "squar_exp",
    }
    
     
    
    # design variables
    xtypes=[FLOAT,FLOAT,(ENUM,2)]
    xlimits = np.array([[-5.0,5.0],[-5.0,5.0],["1","2"]],dtype='object')
    design_variables={"xtypes":xtypes, "bounds": xlimits}
           
   # solution
    sol = {"value": 0, "tol": 1e-6}
    
    case = {
        "models": mod_obj , 
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
