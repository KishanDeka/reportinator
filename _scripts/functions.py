import numpy
from numpy import exp
## exponential
# def expo(x,a,b,c):
#     return a*(exp(bx))+ c
## linear
def lin(p,p_sigma):
    list(p)
    list(p_sigma)
    return "the equation we get after fitting is: $({:.3g} \\pm {:.3g})x + ({:.3g} \\pm {:.3g})$".format(p[1], p_sigma[1], p[0], p_sigma[0])
## polynomial
def pol2(p,p_sigma):
    list(p)
    list(p_sigma)
    return "the equation we get after fitting is: $({:.3g} \\pm {:.3g})x^2 + ({:.3g} \\pm {:.3g})x + ({:.3g} \\pm {:.3g})$".format(p[2], p_sigma[2], p[1], p_sigma[1], p[0], p_sigma[0])
def pol3(p,p_sigma):
    list(p)
    list(p_sigma)
    return "the equation we get after fitting is: $({:.3g} \\pm {:.3g})x^3 + ({:.3g} \\pm {:.3g})x^2 + ({:.3g} \\pm {:.3g})x + ({:.3g} \\pm {:.3g})$".format(p[3], p_sigma[3], p[2], p_sigma[2], p[1], p_sigma[1], p[0], p_sigma[0])
def pol4(p,p_sigma):
    list(p)
    list(p_sigma)
    return "the equation we get after fitting is: $({:.3g} \\pm {:.3g})x^4 + ({:.3g} \\pm {:.3g})x^3 + ({:.3g} \\pm {:.3g})x^2 + ({:.3g} \\pm {:.3g})x + ({:.3g} \\pm {:.3g})$".format(p[4], p_sigma[4], p[3], p_sigma[3], p[2], p_sigma[2], p[1], p_sigma[1], p[0], p_sigma[0])
def pol5(p,p_sigma):
    list(p)
    list(p_sigma)
    return "the equation we get after fitting is: $({:.3g} \\pm {:.3g})x^5 + ({:.3g} \\pm {:.3g})x^4 + ({:.3g} \\pm {:.3g})x^3 + ({:.3g} \\pm {:.3g})x^2 + ({:.3g} \\pm {:.3g})x + ({:.3g} \\pm {:.3g})$".format(p[5], p_sigma[5], p[4], p_sigma[4], p[3], p_sigma[3], p[2], p_sigma[2], p[1], p_sigma[1], p[0], p_sigma[0])

## logarithm
# def log(x,a,b,c):
#     return a*(np.log(b*x)) + c