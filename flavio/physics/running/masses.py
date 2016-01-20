from math import log,pi
import numpy as np
from flavio.physics.running.functions import zeta

"""Functions for running of quark masses."""

def gamma0_qcd(nf):
    return 1.0
def gamma1_qcd(nf):
    return (202./3.-20.*nf/9.)/16.
def gamma2_qcd(nf):
    return (1249. + (-2216./27. - 160.*zeta(3)/3.)*nf-140.*nf*nf/81.)/64.
def gamma3_qcd(nf):
    return ((4603055./162. + 135680.*zeta(3)/27. - 8800.*zeta(5) +
          (-91723./27. - 34192.*zeta(3)/9. +
          880.*zeta(4) + 18400.*zeta(5)/9.)*nf +
          (5242./243. + 800.*zeta(3)/9. - 160.*zeta(4)/3.)*nf**2 +
          (-332./243. + 64.*zeta(3)/27.)*nf**3)/256.)

def gamma_qcd(mq, als, mu, f):
    """RHS of the QCD gamma function written in the form
    d/d\mu m = gamma
    """
    g0 = gamma0_qcd(f)*(als/pi)**1
    g1 = gamma1_qcd(f)*(als/pi)**2
    g2 = gamma2_qcd(f)*(als/pi)**3
    g3 = gamma3_qcd(f)*(als/pi)**4
    return -2*mq/mu*(g0 + g1 + g2 + g3)

def mq(mu, mu0, m0, par, nf=5):
    """Returns m^{(nf)} at the scale mu using 3-loop QCD RGEs"""
    # x[0] is m_q
    # x[1] is alpha_s
    ale_mz = par['alphae_MZ']
    def deriv(x, mu):
        deriv_m = gamma_qcd(x[0], x[1], mu, nf)
        deriv_as = beta_qcd(x[1], ale_mz , mu, nf)
        return np.array([deriv_m, deriv_as])
    as0 = alphas(mu0, par)
    x_0 = np.array([m0,as0])
    sol = odeint(deriv, x_0, [mu0,mu])
    return sol[1,0]


# OS to MSbar conversion according to RunDec

cf=4/3.
ca=3.
tr=1/2.
A4=0.5174790616738993863307581618988629456223774751413792582443193479770

def fMsFromOs1(mu, M):
     lmM=log((mu*mu)/(M*M))
     erg=  (-cf - (3.*cf*lmM)/4.)
     return erg

def fMsFromOs2(mu, M, nl):
     lmM=log((mu*mu)/(M*M))
     erg=  ((-1111.*ca*cf)/384. + (7.*cf*cf)/128. -
     (185.*ca*cf*lmM)/96. + (21.*cf*cf*lmM)/32. - (11.*ca*cf*lmM*lmM)/32. +
     (9.*cf*cf*lmM*lmM)/32. + (143.*cf*tr)/96. + (13.*cf*lmM*tr)/24. +
     (cf*lmM*lmM*tr)/8. +
     (71.*cf*nl*tr)/96. + (13.*cf*lmM*nl*tr)/24. + (cf*lmM*lmM*nl*tr)/8. +
     (ca*cf*zeta(2))/2 - (15.*cf*cf*zeta(2))/8. - (3.*ca*cf*log(2)*zeta(2))/2. +
     3.*cf*cf*log(2)*zeta(2) -
     cf*tr*zeta(2) + (cf*nl*tr*zeta(2))/2. + (3.*ca*cf*zeta(3))/8. -
     (3.*cf*cf*zeta(3))/4.)
     return erg

def fMsFromOs3(mu, M, nl):
     lmM=log((mu*mu)/(M*M))
     erg=  ((lmM*lmM*(-2341.*ca*ca*cf + 1962.*ca*cf*cf - 243.*cf*cf*cf
     + 1492.*ca*cf*tr -
      468.*cf*cf*tr + 1492.*ca*cf*nl*tr - 468.*cf*cf*nl*tr - 208.*cf*tr*tr -
      416.*cf*nl*tr*tr - 208.*cf*nl*nl*tr*tr))/1152. +
     (lmM*lmM*lmM*(-242.*ca*ca*cf + 297.*ca*cf*cf - 81.*cf*cf*cf +
     176.*ca*cf*tr - 108.*cf*cf*tr + 176.*ca*cf*nl*tr - 108.*cf*cf*nl*tr -
     32.*cf*tr*tr - 64.*cf*nl*tr*tr - 32.*cf*nl*nl*tr*tr))/1152. +
     (lmM*(-105944.*ca*ca*cf + 52317.*ca*cf*cf - 13203.*cf*cf*cf +
     74624.*ca*cf*tr -
     5436.*cf*cf*tr + 55616.*ca*cf*nl*tr + 2340.*cf*cf*nl*tr -
     12608.*cf*tr*tr -
     18304.*cf*nl*tr*tr - 5696.*cf*nl*nl*tr*tr + 12672.*ca*ca*cf*zeta(2) -
     52704.*ca*cf*cf*zeta(2) + 19440.*cf*cf*cf*zeta(2) -
     38016.*ca*ca*cf*log(2)*zeta(2) +
     91584.*ca*cf*cf*log(2)*zeta(2) - 31104.*cf*cf*cf*log(2)*zeta(2) -
     29952.*ca*cf*tr*zeta(2) +
     27648.*cf*cf*tr*zeta(2) + 13824.*ca*cf*log(2)*tr*zeta(2) -
     27648.*cf*cf*log(2)*tr*zeta(2) +
     8064.*ca*cf*nl*tr*zeta(2) + 12096.*cf*cf*nl*tr*zeta(2) +
     13824.*ca*cf*log(2)*nl*tr*zeta(2) -
     27648.*cf*cf*log(2)*nl*tr*zeta(2) + 9216.*cf*tr*tr*zeta(2) +
     4608.*cf*nl*tr*tr*zeta(2) -
     4608.*cf*nl*nl*tr*tr*zeta(2) + 9504.*ca*ca*cf*zeta(3) -
     22896.*ca*cf*cf*zeta(3) +
     7776.*cf*cf*cf*zeta(3) + 6912.*ca*cf*tr*zeta(3) - 3456.*cf*cf*tr*zeta(3) +
     6912.*ca*cf*nl*tr*zeta(3) - 3456.*cf*cf*nl*tr*zeta(3)))/13824.)
     return erg

def fZmM(nl):
     erg=  (-9478333./93312. + 55.*log(2)*log(2)*log(2)*log(2)/162. +
            (-644201./6480. + 587.*log(2)/27. + 44.*log(2)*log(2)/27.)*zeta(2) -
            61.*zeta(3)/27. + 3475*zeta(4)/432. + 1439.*zeta(2)*zeta(3)/72. -
            1975.*zeta(5)/216. + 220.*A4/27. + nl*(246643./23328. -
            log(2)*log(2)*log(2)*log(2)/81. +(967./108. + 22.*log(2)/27. -
            4.*log(2)*log(2)/27.)*zeta(2) + 241.*zeta(3)/72. - 305.*zeta(4)/108. -
            8.*A4/27.) + nl*nl*(-2353./23328. - 13.*zeta(2)/54 - 7.*zeta(3)/54.))
     return erg

def mOS2mMS(mOS, Nf, asmu, Mu, nl):
    s = np.zeros(4)
    s[0]= 1.
    s[1]=asmu*(fMsFromOs1(Mu, mOS))/pi
    s[2]=asmu**2*fMsFromOs2(Mu, mOS, Nf-1)/pi**2 # omitting the fDelta piece
    s[3]=asmu**3*(fMsFromOs3(Mu, mOS,Nf-1)+ fZmM(Nf-1))/pi**3
    erg=0.0
    if(nl==0):
        erg=1
    else:
       erg=s[:nl+1].sum()
    return mOS*erg

def mtMS(mu, par):
    """Returns QCD MSbar top mass at the scale mu starting from pole mass."""
    # OS to MSbar conversion at scale 170 GeV
    mtpole = par['Mt']
    mt170 = mOS2mMS(mtpole, 5, alphas(170, par), 170, 3)
    # running from 170 to mu
    mt = mq(mu, 170, mt170, par)
    return mt
