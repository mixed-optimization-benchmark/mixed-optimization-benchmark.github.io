import numpy as np

# Objective function
def f_obj(X) :
    """
    s01 objective

    Parameters
    ----------
    point: array_like
        point to evaluate
    """
    x1=X[:,0]
    x2=X[:,1]
    x3=X[:,2]
  #  caté 1
    c1=X[:,3]
    c2=X[:,4]
    c3=X[:,5]
    c4=X[:,6]
    c5=X[:,7]
    c6=X[:,8]
    
    
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
        "corr": "squared_exponential",
        "n_components": 5,
    }
    
    
    # design variables
    vartype=["cont","cont","cont",("cate",6)]
    xlimits = np.array([[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0]])
    design_variables={"vartype":vartype, "bounds": xlimits}
           
   # solution
    sol = {"value": -9, "tol": 1e-6}
    
    case = {
        "models": mod_obj , 
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
