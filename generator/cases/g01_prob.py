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
    x1= X[:, 0]
    x2= X[:, 1]
  #  caté 1
    c1=X[:,2]
    c2=X[:,3]
    c3=X[:,4]

  #  caté 2   
    c4=X[:,5]
    c5=X[:,6]
    c6=X[:,7]
  
           
    def H(x1,x2,x3,x4) : 
        h=53.3108+0.184901*x1-5.02914*x1**3*10**(-6)+7.72522*x1**4*10**(-8)-\
           0.0870775*x2-0.106959*x3+7.98772*x3**3*10**(-6)+0.00242482*x4+\
           1.32851*x4**3*10**(-6)-0.00146393*x1*x2-0.00301588*x1*x3-\
           0.00272291*x1*x4+0.0017004*x2*x3+0.0038428*x2*x4-0.000198969*x3*x4+\
           1.86025*x1*x2*x3*10**(-5)-1.88719*x1*x2*x4*10**(-6)+\
           2.50923*x1*x3*x4*10**(-5)-5.62199*x2*x3*x4*10**(-5)
        return h
 
    
    if (np.size(c1)==(np.sum(c1)+np.sum(c2)+np.sum(c3))) and (np.size(c4)==(np.sum(c5)+np.sum(c6)+np.sum(c4))) :
                  
        y= c4*( c1*H(x1,x2,20,20)+c2*H(x1,x2,50,20)+c3*H(x1,x2,80,20) ) +\
           c5*( c1*H(x1,x2,20,50)+c2*H(x1,x2,50,50)+c3*H(x1,x2,80,50) ) +\
           c6*( c1*H(x1,x2,20,80)+c2*H(x1,x2,50,80)+c3*H(x1,x2,80,80) )            
    return y        
        
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
    vartype=["cont","cont",("cate",3),("cate",3)]
    xlimits = np.array([ [0.0,100.0],[0.0,100.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0]])
    design_variables={"vartype":vartype, "bounds": xlimits}
           
    
   # solution
    sol = {"value": 38.08499454, "tol": 1e-6}
    
    case = {
        "models": mod_obj , 
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
