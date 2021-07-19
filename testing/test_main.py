try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

from AutoFeedback.randomclass import randomvar
import unittest
from main import *

class helper :
   def test_queue( N, lam, expr ) :
       times = my_queue( N, lam, expr )
       mean, mean2 = sum(times) / N, sum(times*times) / N
       var = ( N / (N-1) )*( mean2 - mean*mean )
       return ( mean - 1/(expr-lam) ) / np.sqrt(var/N)      

class UnitTests(unittest.TestCase) :
    def test_queue(self) :
        inputs, var = [], []
        for i in range(1,3) : 
            N=i*50
            for j in range(1,3) : 
               lam=0.2*j
               inputs.append((N,lam,1,))
               myvar1 = randomvar( 0, variance=1, isinteger=False )
               var.append(myvar1)
        assert( check_func("test_queue", inputs, var, modname=helper) )
