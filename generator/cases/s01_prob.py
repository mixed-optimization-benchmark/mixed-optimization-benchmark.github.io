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
    if (np.size(c1)==(np.sum(c1)+np.sum(c2)+np.sum(c3)+np.sum(c4)+np.sum(c5)+np.sum(c6)+np.sum(c7)+np.sum(c8)+np.sum(c9)+np.sum(c10))):
        y= c1*(np.cos(3.6*PI*(x-2))+x-1 ) + c2*(2*np.cos(1.1*PI*np.exp(x))-x/2+2) +\
        c3*(np.cos(2*PI*x)+x/2) + c4*(x*(np.cos(3.4*PI*(x-1))-(x-1)/2)) +\
        c5*(-0.5*x*x) + c6*(2*np.power(np.cos(0.25*PI*np.exp(-np.power(x,4))),2)-x/2+1)+\
        c7*(x*(np.cos(3.4*PI*x))-x/2+1) + c8*(x*(-np.cos(7*0.5*PI*x)-x/2)+2) + c9*(-np.power(x,5)*0.5+1) +\
        c10*(-np.power(np.cos(5*PI*0.5*x),2)*np.sqrt(x)-0.5*np.log(x+0.5)-1.3 )
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
    xlimits = np.array([ [0.0,5.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0]])
    design_variables={"vartype":vartype, "bounds": xlimits}
           
   # solution
    sol = {"value": -1561.5, "tol": 1e-6}
    
    case = {
        "models": mod_obj , 
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
