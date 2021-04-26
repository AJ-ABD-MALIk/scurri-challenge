'''
Created on Apr 22, 2021

@author: sogunfowora
'''

import re


def format_postcode(postcode):
    '''
    Correct postcode formatting issues if necessary
    :param postcode: (str)

    :returns result: (dict)
    '''
    postcode_entered = postcode
    # Remove all space characters in postcode and capitalise
    pattern = re.compile(r'\s+')
    postcode = re.sub(pattern, '', postcode).upper()
    if len(postcode) == 6 or len(postcode) == 7:
        inward_code = postcode[-3:]
        outward_code = postcode[:-3].strip()
        
        formatted_postcode = ' '.join([outward_code, inward_code])
        result = {'postcode': postcode_entered, 'formatted_postcode': formatted_postcode, 'format_status': True}
    
    else:
        result = {'postcode': postcode_entered, 'format_status': False, 'message': 'Invalid Postcode'}
    
    return result
  
  

def validate_postcode(postcode):
    '''
    Validate postcode after formatting
    :param postcode: (str)

    :returns validation_result: (str)
    '''
    pattern = '^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$'
    
    # Validation
    validation_result = 'Valid Postcode' if re.search(pattern, postcode) else 'Invalid Postcode'
    
    
    return validation_result

