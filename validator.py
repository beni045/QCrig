import logging
from configparser import ConfigParser

logger = logging.getLogger(__name__)

# The below data and functions serve to compare and validate values obtained from mechanical testing to expected data
parser = ConfigParser()
parser.read('config.ini')

boundaries = {k:float(v) for k, v in parser._sections['qc_thresholds'].items()} 
lengths = {float(k):float(v) for k, v in parser._sections['length_conversions'].items()} 
compressions = {float(k):float(v) for k, v in parser._sections['compressions'].items()} 

length_boundary = boundaries['length_boundary']
compression_boundary_lower = boundaries['compression_boundary_lower']
compression_boundary_upper = boundaries['compression_boundary_upper']
weight_boundary = boundaries['weight_boundary']
arch_height_boundary = boundaries['arch_height_boundary']


# Compares the measured length to the expected length, within a margin of error
def validate_length(target_size, actual_size):
    if (abs(target_size - actual_size) < length_boundary):
        logger.info('validate_length PASS')
        return True
    else:
        logger.info('validate_length FAIL')
        return False

# Compares the compression of the arch to the expected compression, with margin of error
def validate_compressions(actual_compression):
    if (actual_compression < compression_boundary_lower):
        logger.info('validate_compressions FAIL')
        return False
    
    else:
        logger.info('validate_compressions PASS')
        
        if(actual_compression > compression_boundary_upper):
            logger.warning('Warning: Compression value abnormaly high')
            
        return True
        
# Compares the weight of the sole to the expected weight of the sole, with margin of error
def validate_weight(expected_weight, actual_weight):
    if (expected_weight*(1-weight_boundary) < actual_weight < expected_weight*(1+weight_boundary)):
        logger.info('validate_weight PASS')
        return True
    else:
        logger.info('validate_weight FAIL')
        return False

# Compares the actual arch height to the expected arch height, with margin of error
def validate_arch_height(expected_height, actual_height):
    if (expected_height*(1-arch_height_boundary) < actual_height < expected_height*(1+arch_height_boundary)):
        logger.info('validate_arch_height PASS')
        return True
    else:
        logger.info('validate_arch_height FAIL')
        return False