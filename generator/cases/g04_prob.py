# -*- coding: utf-8 -*-
"""
Created on Fri Apr 06 16:49:25 2018

@author: rpriem
"""
from segomoe.constraint import Constraint

# Objective function
def f_obj(point):
    """
    G04 objective

    Parameters
    ----------
    point: array_like
        point to evaluate
    """
    fail = False
    return (
        5.3578547 * point[2] ** 2.0
        + 0.8356891 * point[0] * point[4]
        + 37.293239 * point[0]
        - 40792.141,
        fail,
    )


# Constraints
def G04_c1(point):
    """
    G04 constraint 1

    Parameters
    ----------
    point: array_like
        point to evaluate
    """
    fail = False
    return (
        (
            85.334407
            + 0.0056858 * point[1] * point[4]
            + 0.0006262 * point[0] * point[3]
            - 0.0022053 * point[2] * point[4]
            - 92.0
        ),
        fail,
    )


def G04_c2(point):
    """
    G04 constraint 2

    Parameters
    ----------
    point: array_like
        point to evaluate
    """
    fail = False
    return (
        (
            -85.334407
            - 0.0056858 * point[1] * point[4]
            - 0.0006262 * point[0] * point[3]
            + 0.0022053 * point[2] * point[4]
        ),
        fail,
    )


def G04_c3(point):
    """
    G04 constraint 3

    Parameters
    ----------
    point: array_like
        point to evaluate
    """
    fail = False
    return (
        (
            80.51249
            + 0.0071317 * point[1] * point[4]
            + 0.0029955 * point[0] * point[1]
            + 0.0021813 * point[2] ** 2
            - 110.0
        ),
        fail,
    )


def G04_c4(point):
    """
    G04 constraint 4

    Parameters
    ----------
    point: array_like
        point to evaluate
    """
    fail = False
    return (
        (
            -80.51249
            - 0.0071317 * point[1] * point[4]
            - 0.0029955 * point[0] * point[1]
            - 0.0021813 * point[2] ** 2
            + 90.0
        ),
        fail,
    )


def G04_c5(point):
    """
    G04 constraint 5

    Parameters
    ----------
    point: array_like
        point to evaluate
    """
    fail = False
    return (
        (
            9.300961
            + 0.0047026 * point[2] * point[4]
            + 0.0012547 * point[0] * point[2]
            + 0.0019085 * point[2] * point[3]
            - 25.0
        ),
        fail,
    )


def G04_c6(point):
    """
    G04 constraint 6

    Parameters
    ----------
    point: array_like
        point to evaluate
    """
    fail = False
    return (
        (
            -9.300961
            - 0.0047026 * point[2] * point[4]
            - 0.0012547 * point[0] * point[2]
            - 0.0019085 * point[2] * point[3]
            + 20.0
        ),
        fail,
    )


# Grouped eval
def f_grouped(point):
    """
    G04 grouped version

    Parameters
    ----------
    point: array_like
        point to evaluate
    """
    return (
        [
            f_obj(point)[0],
            G04_c1(point)[0],
            G04_c2(point)[0],
            G04_c3(point)[0],
            G04_c4(point)[0],
            G04_c5(point)[0],
            G04_c6(point)[0],
        ],
        False,
    )


def get_case():
    """
    Get a dictionnary to run the G04 case

    Returns
    -------
    dic:
        'vars': list of design variables
        'models': dictionary of settings for the default model
        'f_obj': function to evaluate the objective
        'con': list of constraints
        'sol': solution of the problem
    """
    # design variables
    lower = [78.0, 33.0] + [27.0 for i in range(3)]
    upper = [102.0] + [45 for i in range(4)]
    design_variables = [
        {"name": "x_" + str(i), "lb": lower[i], "ub": upper[i]} for i in range(5)
    ]

    n_components = 3

    # constraints
    con_fun = [G04_c1, G04_c2, G04_c3, G04_c4, G04_c5, G04_c6]
    con = [
        Constraint("<", 0.0, name=("G04_c" + str(i)), f=g, tol=1e-4)
        for i, g in enumerate(con_fun)
    ]

    # default model
    mod_obj = {
        "type": "KrigPLSK",
        "corr": "squared_exponential",
        "regr": "constant",
        "theta0": [1.0] * n_components,
        "thetaL": [0.1] * n_components,
        "thetaU": [10.0] * n_components,
        "n_components": n_components,
        "normalize": True,
    }
    # solution
    sol = {"value": -30665.539, "tol": 1e-3}

    case = {
        "vars": design_variables,
        "models": {"obj": mod_obj, "con": mod_obj},
        "f_obj": f_obj,
        "f_grouped": f_grouped,
        "con": con,
        "sol": sol,
    }
    return case
