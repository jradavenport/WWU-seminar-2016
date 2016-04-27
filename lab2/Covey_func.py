#convert Kelvin to Fahrenheit
def K2F(kelvinTemp):
    '''
    This function converts a temperature from Kelvin to Fahrenheit. 
    
    Parameters
    ----------
    kelvinTemp : float
        temperature in degrees Kelvin
        
    Returns
    -------
    Fahrenheit : float
        the temperature, after conversion into degrees F. 
    '''
        
    if kelvinTemp < 0:
        print('unphysical temperature, buster.')
        return None
    else:
        fahrenheitTemp = kelvinTemp * (9/5) - 459.67
        return fahrenheitTemp
