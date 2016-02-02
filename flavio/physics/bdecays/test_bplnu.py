import unittest
import numpy as np
from .bplnu import *
from flavio.physics.bdecays.formfactors.b_v import bsz_parameters
from flavio.physics.eft import WilsonCoefficients


s = 1.519267515435317e+24

par = {
    ('mass','e'): 0.510998928e-3,
    ('mass','mu'): 105.6583715e-3,
    ('mass','tau'): 1.77686,
    ('mass','B+'): 5.27929,
    ('mass','B0'): 5.27961,
    ('mass','D0'): 1.86484,
    ('mass','rho+'): 0.077526,
    ('mass','rho0'): 0.077526,
    ('lifetime','B+'): 1638.e-15*s,
    ('lifetime','B0'): 152.e-14*s,
    'alpha_e': 1/127.940,
    'alpha_s': 0.1185,
    ('mass','Z'): 91.1876,
    ('mass','b'): 4.17,
    ('mass','t'): 173.21,
    ('mass','c'): 1.275,
    'Gmu': 1.1663787e-5,
    'Vus': 0.22,
    'Vub': 3.7e-3,
    'Vcb': 4.1e-2,
    'gamma': 1.22,
# table XII of 1505.03925v1
    ('formfactor','B->D','a0_f0'): 0.647,
    ('formfactor','B->D','a1_f0'): 0.27,
    ('formfactor','B->D','a2_f0'): -0.09,
    ('formfactor','B->D','a0_f+'): 0.836,
    ('formfactor','B->D','a1_f+'): -2.66,
    ('formfactor','B->D','a2_f+'): -0.07,
    ('formfactor','B->D','a0_fT'): 0,
    ('formfactor','B->D','a1_fT'): 0,
    ('formfactor','B->D','a2_fT'): 0,
}

wc_obj = WilsonCoefficients()

class TestBVll(unittest.TestCase):
    def test_brhoee(self):
        # just some trivial tests to see if calling the functions raises an error
        q2 = 3.5
        dBRdq2(q2, wc_obj, par, 'B+', 'D0', 'e')
