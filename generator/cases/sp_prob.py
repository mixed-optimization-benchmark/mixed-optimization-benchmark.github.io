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
 
  #  caté 1
    c1=X[:,2]
    c2=X[:,3]
    
    
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
        "corr": "squared_exponential",
    }
    
     
    
    # design variables
    vartype=["cont","cont",("cate",2)]
    xlimits = np.array([[-5.0,5.0],[-5.0,5.0],[0.0,1.0],[0.0,1.0]])
    design_variables={"vartype":vartype, "bounds": xlimits}
           
   # solution
    sol = {"value": 0, "tol": 1e-6}
    
    case = {
        "models": mod_obj , 
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
