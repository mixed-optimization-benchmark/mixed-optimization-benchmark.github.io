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
    x= X[:, 0].astype(float)
  #  caté 1
    c=X[:,1]
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
    c11=(c=='11')
    c12=(c=='12')
    c13=(c=='13')
    
    def H1(x,c) : 
        h=np.cos( 3.5*PI*x-c/20 )
        return h    
    def H2(x,c) : 
        h=np.cos( 3.5*PI*x-c/20+PI*(0.4+c/15) )
        return h    
    
    if (np.size(c1)==(np.sum(c1)+np.sum(c2)+np.sum(c3)+np.sum(c4)+np.sum(c5)+np.sum(c6)+np.sum(c7)+np.sum(c8)+np.sum(c9)+np.sum(c10)+np.sum(c11)+np.sum(c12)+np.sum(c13))):
     y= c1*H1(x,1)+c2*H1(x,2)+c3*H1(x,3)+c4*H1(x,4)+c5*H1(x,5)+c6*H1(x,6)+c7*H1(x,7)+c8*H1(x,8)+c9*H1(x,9)+\
        c10*H2(x,10)+c11*H2(x,11)+c12*H2(x,12)+c13*H2(x,13)
        
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
    vartype=["cont",("cate",13)]
    xlimits = np.array([ [0.0,1.0],["1","2","3","4","5","6","7","8","9","10","11","12","13"]])
    design_variables={"vartype":vartype, "bounds": xlimits}
           
   # solution
    sol = {"value": -1.0, "tol": 1e-6}
    
    case = {
        "models": mod_obj , 
        "vars":design_variables,
        "f_obj": f_obj,
        "sol": sol,
    }
    return case
