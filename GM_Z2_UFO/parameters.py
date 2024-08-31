# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Sat 31 Aug 2024 10:27:37



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

IxH5PWGA = Parameter(name = 'IxH5PWGA',
                     nature = 'external',
                     type = 'real',
                     value = 0.01,
                     texname = '\\text{IxH5PWGA}',
                     lhablock = 'IMxCHARGEDFORMFACTORS',
                     lhacode = [ 1 ])

IxH5PWGATILDE = Parameter(name = 'IxH5PWGATILDE',
                          nature = 'external',
                          type = 'real',
                          value = 0.,
                          texname = '\\text{IxH5PWGATILDE}',
                          lhablock = 'IMxCHARGEDFORMFACTORS',
                          lhacode = [ 2 ])

IxH3PWGA = Parameter(name = 'IxH3PWGA',
                     nature = 'external',
                     type = 'real',
                     value = 0.01,
                     texname = '\\text{IxH3PWGA}',
                     lhablock = 'IMxCHARGEDFORMFACTORS',
                     lhacode = [ 3 ])

IxH3PWGATILDE = Parameter(name = 'IxH3PWGATILDE',
                          nature = 'external',
                          type = 'real',
                          value = 0.01,
                          texname = '\\text{IxH3PWGATILDE}',
                          lhablock = 'IMxCHARGEDFORMFACTORS',
                          lhacode = [ 4 ])

H5NGAGA = Parameter(name = 'H5NGAGA',
                    nature = 'external',
                    type = 'real',
                    value = 0.01,
                    texname = '\\text{H5NGAGA}',
                    lhablock = 'NEUTRALFORMFACTORS',
                    lhacode = [ 1 ])

H5NZGA = Parameter(name = 'H5NZGA',
                   nature = 'external',
                   type = 'real',
                   value = 0.01,
                   texname = '\\text{H5NZGA}',
                   lhablock = 'NEUTRALFORMFACTORS',
                   lhacode = [ 2 ])

H3NGAGA = Parameter(name = 'H3NGAGA',
                    nature = 'external',
                    type = 'real',
                    value = 0.01,
                    texname = '\\text{H3NGAGA}',
                    lhablock = 'NEUTRALFORMFACTORS',
                    lhacode = [ 3 ])

H3NZGA = Parameter(name = 'H3NZGA',
                   nature = 'external',
                   type = 'real',
                   value = 0.01,
                   texname = '\\text{H3NZGA}',
                   lhablock = 'NEUTRALFORMFACTORS',
                   lhacode = [ 4 ])

H3NGG = Parameter(name = 'H3NGG',
                  nature = 'external',
                  type = 'real',
                  value = 0.01,
                  texname = '\\text{H3NGG}',
                  lhablock = 'NEUTRALFORMFACTORS',
                  lhacode = [ 5 ])

HHGAGA = Parameter(name = 'HHGAGA',
                   nature = 'external',
                   type = 'real',
                   value = 0.01,
                   texname = '\\text{HHGAGA}',
                   lhablock = 'NEUTRALFORMFACTORS',
                   lhacode = [ 6 ])

HHZGA = Parameter(name = 'HHZGA',
                  nature = 'external',
                  type = 'real',
                  value = 0.01,
                  texname = '\\text{HHZGA}',
                  lhablock = 'NEUTRALFORMFACTORS',
                  lhacode = [ 7 ])

HHGG = Parameter(name = 'HHGG',
                 nature = 'external',
                 type = 'real',
                 value = 0.01,
                 texname = '\\text{HHGG}',
                 lhablock = 'NEUTRALFORMFACTORS',
                 lhacode = [ 8 ])

HLGAGA = Parameter(name = 'HLGAGA',
                   nature = 'external',
                   type = 'real',
                   value = 0.01,
                   texname = '\\text{HLGAGA}',
                   lhablock = 'NEUTRALFORMFACTORS',
                   lhacode = [ 9 ])

HLZGA = Parameter(name = 'HLZGA',
                  nature = 'external',
                  type = 'real',
                  value = 0.01,
                  texname = '\\text{HLZGA}',
                  lhablock = 'NEUTRALFORMFACTORS',
                  lhacode = [ 10 ])

HLGG = Parameter(name = 'HLGG',
                 nature = 'external',
                 type = 'real',
                 value = 0.01,
                 texname = '\\text{HLGG}',
                 lhablock = 'NEUTRALFORMFACTORS',
                 lhacode = [ 11 ])

lam2 = Parameter(name = 'lam2',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\lambda _2',
                 lhablock = 'POTENTIALPARAM',
                 lhacode = [ 1 ])

lam3 = Parameter(name = 'lam3',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\lambda _3',
                 lhablock = 'POTENTIALPARAM',
                 lhacode = [ 2 ])

lam4 = Parameter(name = 'lam4',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\lambda _4',
                 lhablock = 'POTENTIALPARAM',
                 lhacode = [ 3 ])

RxH5PWGA = Parameter(name = 'RxH5PWGA',
                     nature = 'external',
                     type = 'real',
                     value = 0.01,
                     texname = '\\text{RxH5PWGA}',
                     lhablock = 'RExCHARGEDFORMFACTORS',
                     lhacode = [ 1 ])

RxH5PWGATILDE = Parameter(name = 'RxH5PWGATILDE',
                          nature = 'external',
                          type = 'real',
                          value = 0.,
                          texname = '\\text{RxH5PWGATILDE}',
                          lhablock = 'RExCHARGEDFORMFACTORS',
                          lhacode = [ 2 ])

RxH3PWGA = Parameter(name = 'RxH3PWGA',
                     nature = 'external',
                     type = 'real',
                     value = 0.01,
                     texname = '\\text{RxH3PWGA}',
                     lhablock = 'RExCHARGEDFORMFACTORS',
                     lhacode = [ 3 ])

RxH3PWGATILDE = Parameter(name = 'RxH3PWGATILDE',
                          nature = 'external',
                          type = 'real',
                          value = 0.01,
                          texname = '\\text{RxH3PWGATILDE}',
                          lhablock = 'RExCHARGEDFORMFACTORS',
                          lhacode = [ 4 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\text{aS}',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.0025499999999999997,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172.,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.0005110000000000001,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.0005110000000000001,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.10566,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.0025499999999999997,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.42,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MHL = Parameter(name = 'MHL',
                nature = 'external',
                type = 'real',
                value = 125,
                texname = '\\text{MHL}',
                lhablock = 'MASS',
                lhacode = [ 25 ])

MHH = Parameter(name = 'MHH',
                nature = 'external',
                type = 'real',
                value = 200.,
                texname = '\\text{MHH}',
                lhablock = 'MASS',
                lhacode = [ 252 ])

MH5 = Parameter(name = 'MH5',
                nature = 'external',
                type = 'real',
                value = 300.,
                texname = '\\text{MH5}',
                lhablock = 'MASS',
                lhacode = [ 257 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WHL = Parameter(name = 'WHL',
                nature = 'external',
                type = 'real',
                value = 0.00575308848,
                texname = '\\text{WHL}',
                lhablock = 'DECAY',
                lhacode = [ 25 ])

WHH = Parameter(name = 'WHH',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WHH}',
                lhablock = 'DECAY',
                lhacode = [ 252 ])

WH3p = Parameter(name = 'WH3p',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WH3p}',
                 lhablock = 'DECAY',
                 lhacode = [ 253 ])

WH3z = Parameter(name = 'WH3z',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WH3z}',
                 lhablock = 'DECAY',
                 lhacode = [ 254 ])

WH5pp = Parameter(name = 'WH5pp',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WH5pp}',
                  lhablock = 'DECAY',
                  lhacode = [ 255 ])

WH5p = Parameter(name = 'WH5p',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WH5p}',
                 lhablock = 'DECAY',
                 lhacode = [ 256 ])

WH5z = Parameter(name = 'WH5z',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WH5z}',
                 lhablock = 'DECAY',
                 lhacode = [ 257 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\text{aEW}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

v = Parameter(name = 'v',
              nature = 'internal',
              type = 'real',
              value = '1/(2**0.25*cmath.sqrt(Gf))',
              texname = 'v')

vphi = Parameter(name = 'vphi',
                 nature = 'internal',
                 type = 'real',
                 value = '1/(2**0.25*cmath.sqrt(Gf))',
                 texname = 'v_{\\phi }')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

MH3 = Parameter(name = 'MH3',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(MH5**2 + 2*MHH**2)/cmath.sqrt(3)',
                texname = 'M_3')

mu2sq = Parameter(name = 'mu2sq',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.5*MHL**2',
                  texname = '\\text{mu2sq}')

mu3sq = Parameter(name = 'mu3sq',
                  nature = 'internal',
                  type = 'real',
                  value = '(2*MH5**2 + MHH**2)/3. - 2*lam2*vphi**2',
                  texname = '\\text{mu3sq}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

lam1 = Parameter(name = 'lam1',
                 nature = 'internal',
                 type = 'real',
                 value = 'MHL**2/(8.*vphi**2)',
                 texname = '\\lambda _1')

lam5 = Parameter(name = 'lam5',
                 nature = 'internal',
                 type = 'real',
                 value = '(2*(MH5**2 - MHH**2))/(3.*vphi**2)',
                 texname = '\\lambda _5')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vphi',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vphi',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vphi',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vphi',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vphi',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vphi',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vphi',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vphi',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vphi',
                texname = '\\text{yup}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

