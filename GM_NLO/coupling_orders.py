# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 10.4.1 for Mac OS X x86 (64-bit) (April 17, 2016)
# Date: Sat 15 Sep 2018 23:07:42


from object_library import all_orders, CouplingOrder


QCD = CouplingOrder(name = 'QCD',
                    expansion_order = 99,
                    hierarchy = 1,
                    perturbative_expansion = 1)

QED = CouplingOrder(name = 'QED',
                    expansion_order = 99,
                    hierarchy = 2)

Eff = CouplingOrder(name = 'Eff',
                    expansion_order = 99,
                    hierarchy = 3)

