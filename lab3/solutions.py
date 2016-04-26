import numpy as np


def constell_davenport(x,y):
    '''
    Determine which constellation a set of coordinates is located in. 
    Based on the algorithm from N. G. Roman 1987, PASP, 99, 695. Written by @jradavenport
    
    This version uses Numpy arrays, and can operate on either a single (x,y) coordinate, 
    or a list of coordinates.
    
    Parameters
    ----------
    x : float or float array
        Right Ascension (RA) of target, in decimal hours in the range [0, 24]
    y : float or float array
        Declination (Dec) of target, in decimal degrees in the range [-90, 90]

    Returns
    -------
    string or string array
        Abbreviation of constellation for each set of coordinates
    '''
    
    # read the data in every time (runtime overhead....)
    RAl, RAu, Decl = np.loadtxt('data/data.txt', delimiter=',', usecols=(0,1,2), unpack=True)
    names = np.loadtxt('data/data.txt', delimiter=',', usecols=(3,), unpack=True, dtype='str')
    
    # handle lists of coordinates
    if np.size(x) > 1:
        outname = []

        for k in range(np.size(x)):

            c1 = np.where((Decl <= y[k]))

            c2 = np.where((RAu[c1] > x[k]))

            c3 = np.where((RAl[c1][c2] <= x[k]))

            outname = np.append(outname, names[c1][c2][c3][0])

        return outname

    # handle old-fashioned single coordinate case
    else:
        c1 = np.where((Decl <= y))

        c2 = np.where((RAu[c1] > x))

        c3 = np.where((RAl[c1][c2] <= x))

        return names[c1][c2][c3][0]
    

def constell_christenson(ra,dec):
    '''
    This is a function to determine the constellation in which an object is located from its ra and dec
    Written by @hmchristenson 
    
    Parameters
    -------
    ra: float
        Right ascension
    dec: float
        Declination
        
    Returns
    -------
    output: string
        Name of the constellation in which the object is located
    '''
    RAl, RAu, Decl, = np.loadtxt('data/data.txt', delimiter=',', usecols=(0,1,2), unpack=True)
    names = np.loadtxt('data/data.txt', delimiter=',', usecols=(3,), unpack=True, dtype='str')
    
    count = 0

    while(Decl[count] > dec):
        count = count + 1
    dec_low = Decl[count]
    
    while(RAu[count] <= ra):
        count = count + 1
    ra_up = RAu[count]

    while(RAl[count] > ra or RAu[count] < ra):
        count = count + 1 
    ra_low = RAl[count]
       
    output = names[count]
    
    return output