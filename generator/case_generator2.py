try:
    from mpi4py import MPI

    MPI_AVAILABLE = True
except ImportError:
    MPI_AVAILABLE = False

     
# List of available cases
# GEN_CASES = ['Michalewicz', 'Mod_Branin', 'Six_Hump', 'G07', 'GTCD', 'Mopta_12D', \
# 'Ackley', 'Griewank', 'G01', 'G01', 'G02', 'G03', 'G04', 'G05', 'G06', \
# 'G08', 'G09', 'G10', 'G11', 'G13', 'G14', 'G15', 'G16', 'G17', \
# 'G18', 'G21', 'G22', 'G23', 'G24', 'Hesse', 'PVD4', 'SR7', 'WB4']


def _import_case(case, options={}):
    """
    Import the right case

    Parameters
    ----------
    case: str
        name of the case, see GEN_CASES.
    options: dict
        SEGO options
    """
    if case is None:
        case = "Branin_5"
    elif case == "Branin_1":
        from cases.b01_prob import get_case
    elif case == "Branin_2":
        from cases.b02_prob import get_case       
    elif case == "Branin_5":
        from cases.b05_prob import get_case
    elif case == "Goldstein_1":
        from cases.g01_prob import get_case
    elif case == "Set_1":
        from cases.s01_prob import get_case      
    elif case == "Set_2":
        from cases.s02_prob import get_case  
    elif case == "Cos_1":
        from cases.c01_prob import get_case     
    elif case == "Wong1":
        from cases.w1_prob import get_case    
    elif case == "Spiral":
        from cases.sp_prob import get_case            
    elif case == "EVD52":
        from cases.evd_prob import get_case 
    elif case == "Rosen-Suzuki":
        from cases.rs_prob import get_case 
    else:
        raise ValueError("%s is not implemented" % (case))
    return get_case

