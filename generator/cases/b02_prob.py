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
    x1= X[:, 0].astype(float)
    x2= X[:, 1].astype(float)
    x3= X[:, 2].astype(float)
    x4= X[:, 3].astype(float)
    x5= X[:, 4].astype(float)
    x6= X[:, 5].astype(float)
    x7= X[:, 6].astype(float)
    x8= X[:, 7].astype(float)
    x9= X[:, 8].astype(float)
    x10= X[:,9].astype(float)
    #  caté 1
    cate1=X[:,10]
    c1=(cate1=="1")
    c2=(cate1=="2")
  #  caté 2   
    cate2=X[:,11]
    c3=(cate2=="1")
    c4=(cate2=="2")
  
    def H(x1,x2) : 
        h=(((15*x2-5/(4*PI**2)*(15*x1-5)**2+ 5/PI*(15*x1-5) -6)**2 +\
          10*(1-1/(8*PI))*np.cos(15*x1-5) + 10)- 54.8104)/51.9496
        
        return h
        
    h=H(x1,x2)+H(x3,x4)+H(x5,x6)+H(x7,x8)+H(x9,x10)
    
    if (np.size(c1)==(np.sum(c1)+np.sum(c2))) and (np.size(c3)==(np.sum(c3)+np.sum(c4))) :
        y= c1*c3*(h)+ c1*c4*(0.4*h+1.1)+ c2*c3*(-0.75*h+5.2)+c2*c4*(-0.5*h-2.1)
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
    vartype=["cont","cont","cont","cont","cont","cont","cont","cont","cont","cont",("cate",2),("cate",2)]
    xlimits = np.array([[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],[0.0,1.0],["1","2"],["1","2"]] )
    design_variables={"vartype":vartype, "bounds": xlimits}
           
   # solution
    sol = {"value": -14.186036350718284, "tol": 1e-6}
    #don't know 
    
    case = {
        "models": mod_obj , 
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
