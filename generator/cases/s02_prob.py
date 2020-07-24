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
    PI = 3.14159265358979323846 
    x= X[:, 0]
  #  caté 1
    c1=X[:,1]
    c2=X[:,2]
    c3=X[:,3]
    c4=X[:,4]
    c5=X[:,5]
    c6=X[:,6]
    c7=X[:,7]
    c8=X[:,8]
    c9=X[:,9]
    c10=X[:,10]
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
        "corr": "squared_exponential",
        "n_components": 5,
    }
    
    
    # design variables
    vartype=["cont",("cate",10)]
    xlimits = np.array([[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0]])
    design_variables={"vartype":vartype, "bounds": xlimits}
           
   # solution
    sol = {"value": -0.6657395614066074, "tol": 1e-6}
    
    case = {
        "models": mod_obj , 
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
