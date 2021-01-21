import numpy as np
from smt.applications.mixed_integer import (
    FLOAT,
    INT,
    ENUM,
    MixedIntegerSamplingMethod,
    cast_to_mixed_integer
)
# Objective function
def f_obj(X) :
    """
    B05 objective

    Parameters
    ----------
    point: array_like
        point to evaluate
    """
    fail = False
    x1=X[:,0]
    x2=X[:,1]
    if (x1 == np.floor(x1)).all: 
        PI = 3.14159265358979323846
        a = 1
        b = 5.1/(4*np.power(PI,2))
        c = 5/PI
        r = 6   
        s = 10
        t = 1/(8*PI)
        y=  a*(x2 - b*x1**2 + c*x1 -r)**2 + s*(1-t)*np.cos(x1) + s
    else : 
        print("type error")
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
    xtypes = [INT, FLOAT]
    xlimits = np.array([[-5, 10],[0.0,15.0]])
    design_variables={"xtypes":xtypes, "bounds": xlimits}
   # solution
    sol = {"value": 0.49398053, "tol": 1e-6}
    case = {
        "models": mod_obj ,
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
