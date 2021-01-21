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
    PI = 3.14159265358979323846
    xtypes=[FLOAT,(ENUM,10)]
    xlimits = np.array([[0.0,1.0],["1","2","3","4","5","6","7","8","9","10"]],dtype='object')
    mixint = MixedIntegerContext(xtypes, xlimits)
    X_=np.zeros((X.shape),dtype=object)
    i=0
    for x in X : 
        X_[i]=mixint.cast_to_mixed_integer(x)
        i+=1
    
    x= X_[:, 0].astype(float)
  #  caté 1
    c=X_[:,1]
    c1=(c=='1')
    c2=(c=='2')
    c3=(c=='3')
    c4=(c=='4')
    c5=(c=='5')
    c6=(c=='6')
    c7=(c=='7')
    c8=(c=='8')
    c9=(c=='9')
    c10=(c=='10')
    def H1(x,c) : 
        h=(x+ 0.01*(x-1/2)**2)*c/10 
        return h    
    def H2(x,c) : 
        h=0.9*np.cos(2*PI*(x+(c-4)/20))*np.exp(-x)
        return h    
    def H3(x,c) : 
        h=-0.7*np.cos(2*PI*(x+(c-7)/20))*np.exp(-x)
        return h    
    
    
    if (np.size(c1)==(np.sum(c1)+np.sum(c2)+np.sum(c3)+np.sum(c4)+np.sum(c5)+np.sum(c6)+np.sum(c7)+np.sum(c8)+np.sum(c9)+np.sum(c10))):
     y= c1*H1(x,1)+c2*H1(x,2)+c3*H1(x,3)+c4*H1(x,4)+\
        c5*H2(x,5)+c6*H2(x,6)+c7*H2(x,7)+\
        c8*H3(x,8)+c9*H3(x,9)+c10*H3(x,10)
        
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
    xtypes=[FLOAT,(ENUM,10)]
    xlimits = np.array([[0.0,1.0],["1","2","3","4","5","6","7","8","9","10"]],dtype='object')
    design_variables={"xtypes":xtypes, "bounds": xlimits}
           
   # solution
    sol = {"value": -0.6657395614066074, "tol": 1e-6}
    
    case = {
        "models": mod_obj , 
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
