# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Mon 16 Sep 2024 14:45:10


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

