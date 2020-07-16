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
    x4=X[:,3]
    x5=X[:,4]
    x6=X[:,5]
    x7=X[:,6]
    
  #  caté 1
    c1=X[:,7]
    c2=X[:,8]
    c3=X[:,9]
    c4=X[:,10]
    c5=X[:,11]
    
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
        "corr": "squared_exponential",
        "n_components": 5,
    }
    
    
    # design variables
    vartype=["cont","cont","cont","cont","cont","cont","cont",("cate",5)]
    xlimits = np.array([ [-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[-5.0,5.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0]])
    design_variables={"vartype":vartype, "bounds": xlimits}
           
   # solution
    sol = {"value": -1793.0129033, "tol": 1e-6}
    
    case = {
        "models": mod_obj , 
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
