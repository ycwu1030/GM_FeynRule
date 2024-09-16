# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Mon 16 Sep 2024 14:45:11


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.G, P.G, P.G ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV8, L.VVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.G] ] ],
               couplings = {(0,0,0):C.R2GC_624_211,(0,0,1):C.R2GC_626_214,(0,1,0):C.R2GC_627_215,(0,1,1):C.R2GC_627_216,(0,3,0):C.R2GC_627_215,(0,3,1):C.R2GC_629_218,(0,5,0):C.R2GC_624_211,(0,5,1):C.R2GC_625_213,(0,6,0):C.R2GC_624_211,(0,6,1):C.R2GC_624_212,(0,7,0):C.R2GC_627_215,(0,7,1):C.R2GC_628_217,(0,2,1):C.R2GC_493_106,(0,4,1):C.R2GC_492_105})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.G, P.G, P.G, P.G ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.G] ] ],
               couplings = {(2,0,0):C.R2GC_496_111,(2,0,1):C.R2GC_496_112,(0,0,0):C.R2GC_496_111,(0,0,1):C.R2GC_496_112,(4,0,0):C.R2GC_494_107,(4,0,1):C.R2GC_494_108,(3,0,0):C.R2GC_494_107,(3,0,1):C.R2GC_494_108,(8,0,0):C.R2GC_495_109,(8,0,1):C.R2GC_495_110,(6,0,0):C.R2GC_499_116,(6,0,1):C.R2GC_635_224,(7,0,0):C.R2GC_500_117,(7,0,1):C.R2GC_633_223,(5,0,0):C.R2GC_494_107,(5,0,1):C.R2GC_494_108,(1,0,0):C.R2GC_494_107,(1,0,1):C.R2GC_494_108,(11,0,0):C.R2GC_498_114,(11,0,1):C.R2GC_498_115,(10,0,0):C.R2GC_498_114,(10,0,1):C.R2GC_498_115,(9,0,1):C.R2GC_497_113,(0,1,0):C.R2GC_496_111,(0,1,1):C.R2GC_496_112,(2,1,0):C.R2GC_496_111,(2,1,1):C.R2GC_496_112,(5,1,0):C.R2GC_494_107,(5,1,1):C.R2GC_494_108,(1,1,0):C.R2GC_494_107,(1,1,1):C.R2GC_494_108,(7,1,0):C.R2GC_500_117,(7,1,1):C.R2GC_495_110,(4,1,0):C.R2GC_494_107,(4,1,1):C.R2GC_494_108,(3,1,0):C.R2GC_494_107,(3,1,1):C.R2GC_494_108,(8,1,0):C.R2GC_495_109,(8,1,1):C.R2GC_633_223,(6,1,0):C.R2GC_631_220,(6,1,1):C.R2GC_631_221,(11,1,0):C.R2GC_498_114,(11,1,1):C.R2GC_498_115,(10,1,0):C.R2GC_498_114,(10,1,1):C.R2GC_498_115,(9,1,1):C.R2GC_497_113,(0,2,0):C.R2GC_496_111,(0,2,1):C.R2GC_496_112,(2,2,0):C.R2GC_496_111,(2,2,1):C.R2GC_496_112,(5,2,0):C.R2GC_494_107,(5,2,1):C.R2GC_494_108,(1,2,0):C.R2GC_494_107,(1,2,1):C.R2GC_494_108,(7,2,0):C.R2GC_632_222,(7,2,1):C.R2GC_630_219,(4,2,0):C.R2GC_494_107,(4,2,1):C.R2GC_494_108,(3,2,0):C.R2GC_494_107,(3,2,1):C.R2GC_494_108,(8,2,0):C.R2GC_495_109,(8,2,1):C.R2GC_630_219,(6,2,0):C.R2GC_499_116,(11,2,0):C.R2GC_498_114,(11,2,1):C.R2GC_498_115,(10,2,0):C.R2GC_498_114,(10,2,1):C.R2GC_498_115,(9,2,1):C.R2GC_497_113})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.G ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.d, P.G] ] ],
               couplings = {(0,0,0):C.R2GC_502_119})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.G ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.G, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_502_119})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.b, P.G] ] ],
               couplings = {(0,0,0):C.R2GC_502_119})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.G ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.G, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_502_119})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.G ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.c, P.G] ] ],
               couplings = {(0,0,0):C.R2GC_502_119})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.G, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_502_119})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.d, P.G] ] ],
               couplings = {(0,0,0):C.R2GC_501_118})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.A ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.G, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_501_118})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.A ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_501_118})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_517_123,(0,1,0):C.R2GC_518_124})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.G, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_517_123,(0,1,0):C.R2GC_518_124})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_517_123,(0,1,0):C.R2GC_518_124})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.A ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_503_120})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.A ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_503_120})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.A ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_503_120})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_528_131,(0,1,0):C.R2GC_529_132})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_528_131,(0,1,0):C.R2GC_529_132})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_528_131,(0,1,0):C.R2GC_529_132})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_640_226})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.G, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_641_227})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.b__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_642_228})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_547_147})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.G, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_567_162})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.b__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.c, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_527_130})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.d__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_587_177})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.s__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.G, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_588_178})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_589_179})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_661_245})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_558_156})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.t__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_608_196})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.G, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_666_250})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.G, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_578_171})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.t__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.G, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_613_201})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.u__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_671_255})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.c__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.c, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_538_141})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_618_206})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_653_237,(0,1,0):C.R2GC_647_231})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.G, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_654_238,(0,1,0):C.R2GC_649_233})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.b__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_655_239,(0,1,0):C.R2GC_645_229})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_550_148,(0,1,0):C.R2GC_554_152})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.G, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_570_163,(0,1,0):C.R2GC_574_167})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.b__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.c, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_534_137,(0,1,0):C.R2GC_530_133})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.d__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_600_188,(0,1,0):C.R2GC_594_182})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.s__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.G, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_601_189,(0,1,0):C.R2GC_596_184})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_602_190,(0,1,0):C.R2GC_592_180})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.H3p__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_658_242,(0,1,0):C.R2GC_648_232})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.H3p__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.G, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_659_243,(0,1,0):C.R2GC_650_234})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.b__tilde__, P.u, P.H3p__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_660_244,(0,1,0):C.R2GC_646_230})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.H3p__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_551_149,(0,1,0):C.R2GC_557_155})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.H3p__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.G, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_571_164,(0,1,0):C.R2GC_577_170})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.b__tilde__, P.c, P.H3p__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.c, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_537_140,(0,1,0):C.R2GC_531_134})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.d__tilde__, P.t, P.H3p__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_605_193,(0,1,0):C.R2GC_595_183})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.s__tilde__, P.t, P.H3p__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.G, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_606_194,(0,1,0):C.R2GC_597_185})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.H3p__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_607_195,(0,1,0):C.R2GC_593_181})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_662_246,(0,1,0):C.R2GC_664_248})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_561_159,(0,1,0):C.R2GC_559_157})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.t__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_609_197,(0,1,0):C.R2GC_611_199})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.G, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_667_251,(0,1,0):C.R2GC_669_253})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.G, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_581_174,(0,1,0):C.R2GC_579_172})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.t__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.G, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_614_202,(0,1,0):C.R2GC_616_204})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.u__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_672_256,(0,1,0):C.R2GC_674_258})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.c__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.c, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_539_142,(0,1,0):C.R2GC_541_144})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_619_207,(0,1,0):C.R2GC_621_209})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.H3p ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_663_247,(0,1,0):C.R2GC_665_249})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.H3p ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_562_160,(0,1,0):C.R2GC_560_158})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.t__tilde__, P.d, P.H3p ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_610_198,(0,1,0):C.R2GC_612_200})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.H3p ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.G, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_668_252,(0,1,0):C.R2GC_670_254})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.H3p ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.G, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_582_175,(0,1,0):C.R2GC_580_173})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.t__tilde__, P.s, P.H3p ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.G, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_615_203,(0,1,0):C.R2GC_617_205})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.u__tilde__, P.b, P.H3p ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_673_257,(0,1,0):C.R2GC_675_259})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.c__tilde__, P.b, P.H3p ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.c, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_540_143,(0,1,0):C.R2GC_542_145})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.H3p ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_620_208,(0,1,0):C.R2GC_622_210})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_553_151})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.G, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_573_166})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_520_126})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_552_150})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.G, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_572_165})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_519_125})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_555_153})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.G, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_575_168})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_521_127})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.H3z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_556_154})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.H3z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.G, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_576_169})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.H3z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_522_128})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_652_236})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_533_136})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_599_187})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_651_235})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_532_135})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.HL ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_598_186})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_656_240})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_535_138})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_603_191})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.H3z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.G, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_657_241})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.H3z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.G] ] ],
                couplings = {(0,0,0):C.R2GC_536_139})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H3z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.G, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_604_192})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.G, P.G, P.HH ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS3 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_479_27,(0,0,1):C.R2GC_479_28,(0,0,2):C.R2GC_479_29,(0,0,3):C.R2GC_479_30,(0,0,4):C.R2GC_479_31,(0,0,5):C.R2GC_479_32})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.G, P.G, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_478_21,(0,0,1):C.R2GC_478_22,(0,0,2):C.R2GC_478_23,(0,0,3):C.R2GC_478_24,(0,0,4):C.R2GC_478_25,(0,0,5):C.R2GC_478_26})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_639_225,(0,1,0):C.R2GC_513_121})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.c, P.G] ] ],
                 couplings = {(0,0,0):C.R2GC_526_129,(0,1,0):C.R2GC_513_121})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_586_176,(0,1,0):C.R2GC_513_121})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.d, P.G] ] ],
                 couplings = {(0,0,0):C.R2GC_546_146,(0,1,0):C.R2GC_513_121})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_566_161,(0,1,0):C.R2GC_513_121})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.b, P.G] ] ],
                 couplings = {(0,0,0):C.R2GC_516_122,(0,1,0):C.R2GC_513_121})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.G, P.G ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV2, L.VV3, L.VV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.G] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,2,4):C.R2GC_469_1,(0,0,0):C.R2GC_473_7,(0,0,2):C.R2GC_473_8,(0,0,3):C.R2GC_473_9,(0,0,5):C.R2GC_473_10,(0,0,6):C.R2GC_473_11,(0,0,7):C.R2GC_473_12,(0,1,1):C.R2GC_470_2})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.A, P.G, P.G, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_474_13,(0,0,1):C.R2GC_474_14})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.G, P.G, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_477_19,(0,0,1):C.R2GC_477_20})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.G, P.G, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.b, P.t] ], [ [P.b, P.u] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.t] ], [ [P.d, P.u] ], [ [P.s, P.t] ], [ [P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_486_69,(0,0,1):C.R2GC_486_70,(0,0,2):C.R2GC_486_71,(0,0,3):C.R2GC_486_72,(0,0,4):C.R2GC_486_73,(0,0,5):C.R2GC_486_74,(0,0,6):C.R2GC_486_75,(0,0,7):C.R2GC_486_76,(0,0,8):C.R2GC_486_77})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.A, P.A, P.G, P.G ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_471_3,(0,0,1):C.R2GC_471_4})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.G, P.G, P.G, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(1,0,0):C.R2GC_476_17,(1,0,1):C.R2GC_476_18,(0,1,0):C.R2GC_475_15,(0,1,1):C.R2GC_475_16})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.A, P.G, P.G, P.G ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_472_5,(0,0,1):C.R2GC_472_6})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.G, P.G, P.HL, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_480_33,(0,0,1):C.R2GC_480_34,(0,0,2):C.R2GC_480_35,(0,0,3):C.R2GC_480_36,(0,0,4):C.R2GC_480_37,(0,0,5):C.R2GC_480_38})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.G, P.G, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_481_39,(0,0,1):C.R2GC_481_40,(0,0,2):C.R2GC_481_41,(0,0,3):C.R2GC_481_42,(0,0,4):C.R2GC_481_43,(0,0,5):C.R2GC_481_44})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.G, P.G, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.b, P.t] ], [ [P.b, P.u] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.t] ], [ [P.d, P.u] ], [ [P.s, P.t] ], [ [P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_487_78,(0,0,1):C.R2GC_487_79,(0,0,2):C.R2GC_487_80,(0,0,3):C.R2GC_487_81,(0,0,4):C.R2GC_487_82,(0,0,5):C.R2GC_487_83,(0,0,6):C.R2GC_487_84,(0,0,7):C.R2GC_487_85,(0,0,8):C.R2GC_487_86})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.G, P.G, P.HH, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_482_45,(0,0,1):C.R2GC_482_46,(0,0,2):C.R2GC_482_47,(0,0,3):C.R2GC_482_48,(0,0,4):C.R2GC_482_49,(0,0,5):C.R2GC_482_50})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.G, P.G, P.HH, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_483_51,(0,0,1):C.R2GC_483_52,(0,0,2):C.R2GC_483_53,(0,0,3):C.R2GC_483_54,(0,0,4):C.R2GC_483_55,(0,0,5):C.R2GC_483_56})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.G, P.G, P.G__minus__, P.H3p ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.b, P.t] ], [ [P.b, P.u] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.t] ], [ [P.d, P.u] ], [ [P.s, P.t] ], [ [P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_488_87,(0,0,1):C.R2GC_488_88,(0,0,2):C.R2GC_488_89,(0,0,3):C.R2GC_488_90,(0,0,4):C.R2GC_488_91,(0,0,5):C.R2GC_488_92,(0,0,6):C.R2GC_488_93,(0,0,7):C.R2GC_488_94,(0,0,8):C.R2GC_488_95})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.G, P.G, P.G__plus__, P.H3p__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.b, P.t] ], [ [P.b, P.u] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.t] ], [ [P.d, P.u] ], [ [P.s, P.t] ], [ [P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_488_87,(0,0,1):C.R2GC_488_88,(0,0,2):C.R2GC_488_89,(0,0,3):C.R2GC_488_90,(0,0,4):C.R2GC_488_91,(0,0,5):C.R2GC_488_92,(0,0,6):C.R2GC_488_93,(0,0,7):C.R2GC_488_94,(0,0,8):C.R2GC_488_95})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.G, P.G, P.H3p__tilde__, P.H3p ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.b, P.t] ], [ [P.b, P.u] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.t] ], [ [P.d, P.u] ], [ [P.s, P.t] ], [ [P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_489_96,(0,0,1):C.R2GC_489_97,(0,0,2):C.R2GC_489_98,(0,0,3):C.R2GC_489_99,(0,0,4):C.R2GC_489_100,(0,0,5):C.R2GC_489_101,(0,0,6):C.R2GC_489_102,(0,0,7):C.R2GC_489_103,(0,0,8):C.R2GC_489_104})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.G, P.G, P.G0, P.H3z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_484_57,(0,0,1):C.R2GC_484_58,(0,0,2):C.R2GC_484_59,(0,0,3):C.R2GC_484_60,(0,0,4):C.R2GC_484_61,(0,0,5):C.R2GC_484_62})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.G, P.G, P.H3z, P.H3z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_485_63,(0,0,1):C.R2GC_485_64,(0,0,2):C.R2GC_485_65,(0,0,3):C.R2GC_485_66,(0,0,4):C.R2GC_485_67,(0,0,5):C.R2GC_485_68})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.G, P.G, P.G ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8, L.VVV9 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.G] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_624_265,(0,0,1):C.UVGC_624_266,(0,0,2):C.UVGC_624_267,(0,0,3):C.UVGC_626_274,(0,0,4):C.UVGC_626_275,(0,0,5):C.UVGC_624_269,(0,0,6):C.UVGC_624_270,(0,0,7):C.UVGC_624_271,(0,1,0):C.UVGC_627_276,(0,1,1):C.UVGC_627_277,(0,1,2):C.UVGC_627_278,(0,1,3):C.UVGC_627_279,(0,1,5):C.UVGC_627_280,(0,1,6):C.UVGC_627_281,(0,1,7):C.UVGC_627_282,(0,3,0):C.UVGC_627_276,(0,3,1):C.UVGC_627_277,(0,3,2):C.UVGC_627_278,(0,3,3):C.UVGC_629_285,(0,3,4):C.UVGC_629_286,(0,3,5):C.UVGC_627_280,(0,3,6):C.UVGC_627_281,(0,3,7):C.UVGC_627_282,(0,5,0):C.UVGC_624_265,(0,5,1):C.UVGC_624_266,(0,5,2):C.UVGC_624_267,(0,5,3):C.UVGC_625_272,(0,5,4):C.UVGC_625_273,(0,5,5):C.UVGC_624_269,(0,5,6):C.UVGC_624_270,(0,5,7):C.UVGC_624_271,(0,7,0):C.UVGC_624_265,(0,7,1):C.UVGC_624_266,(0,7,2):C.UVGC_624_267,(0,7,3):C.UVGC_624_268,(0,7,4):C.UVGC_493_7,(0,7,5):C.UVGC_624_269,(0,7,6):C.UVGC_624_270,(0,7,7):C.UVGC_624_271,(0,8,0):C.UVGC_627_276,(0,8,1):C.UVGC_627_277,(0,8,2):C.UVGC_627_278,(0,8,3):C.UVGC_628_283,(0,8,4):C.UVGC_628_284,(0,8,5):C.UVGC_627_280,(0,8,6):C.UVGC_627_281,(0,8,7):C.UVGC_627_282,(0,2,3):C.UVGC_493_6,(0,2,4):C.UVGC_493_7,(0,4,3):C.UVGC_492_4,(0,4,4):C.UVGC_492_5,(0,6,3):C.UVGC_490_1})

V_125 = CTVertex(name = 'V_125',
                 type = 'UV',
                 particles = [ P.G, P.G, P.G, P.G ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.G] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(2,0,4):C.UVGC_495_11,(2,0,5):C.UVGC_495_10,(0,0,4):C.UVGC_495_11,(0,0,5):C.UVGC_495_10,(4,0,4):C.UVGC_494_8,(4,0,5):C.UVGC_494_9,(3,0,4):C.UVGC_494_8,(3,0,5):C.UVGC_494_9,(8,0,4):C.UVGC_495_10,(8,0,5):C.UVGC_495_11,(6,0,0):C.UVGC_634_312,(6,0,2):C.UVGC_634_313,(6,0,3):C.UVGC_634_314,(6,0,4):C.UVGC_635_319,(6,0,5):C.UVGC_635_320,(6,0,6):C.UVGC_634_316,(6,0,7):C.UVGC_634_317,(6,0,8):C.UVGC_634_318,(7,0,0):C.UVGC_634_312,(7,0,2):C.UVGC_634_313,(7,0,3):C.UVGC_634_314,(7,0,4):C.UVGC_633_307,(7,0,5):C.UVGC_634_315,(7,0,6):C.UVGC_634_316,(7,0,7):C.UVGC_634_317,(7,0,8):C.UVGC_634_318,(5,0,4):C.UVGC_494_8,(5,0,5):C.UVGC_494_9,(1,0,4):C.UVGC_494_8,(1,0,5):C.UVGC_494_9,(11,0,4):C.UVGC_498_14,(11,0,5):C.UVGC_498_15,(10,0,4):C.UVGC_498_14,(10,0,5):C.UVGC_498_15,(9,0,4):C.UVGC_497_12,(9,0,5):C.UVGC_497_13,(0,1,4):C.UVGC_495_11,(0,1,5):C.UVGC_495_10,(2,1,4):C.UVGC_495_11,(2,1,5):C.UVGC_495_10,(5,1,4):C.UVGC_494_8,(5,1,5):C.UVGC_494_9,(1,1,4):C.UVGC_494_8,(1,1,5):C.UVGC_494_9,(7,1,1):C.UVGC_499_16,(7,1,4):C.UVGC_495_10,(7,1,5):C.UVGC_500_17,(4,1,4):C.UVGC_494_8,(4,1,5):C.UVGC_494_9,(3,1,4):C.UVGC_494_8,(3,1,5):C.UVGC_494_9,(8,1,0):C.UVGC_633_304,(8,1,2):C.UVGC_633_305,(8,1,3):C.UVGC_633_306,(8,1,4):C.UVGC_633_307,(8,1,5):C.UVGC_633_308,(8,1,6):C.UVGC_633_309,(8,1,7):C.UVGC_633_310,(8,1,8):C.UVGC_633_311,(6,1,0):C.UVGC_631_295,(6,1,2):C.UVGC_631_296,(6,1,3):C.UVGC_631_297,(6,1,4):C.UVGC_631_298,(6,1,5):C.UVGC_631_299,(6,1,6):C.UVGC_631_300,(6,1,7):C.UVGC_631_301,(6,1,8):C.UVGC_631_302,(11,1,4):C.UVGC_498_14,(11,1,5):C.UVGC_498_15,(10,1,4):C.UVGC_498_14,(10,1,5):C.UVGC_498_15,(9,1,4):C.UVGC_497_12,(9,1,5):C.UVGC_497_13,(0,2,4):C.UVGC_495_11,(0,2,5):C.UVGC_495_10,(2,2,4):C.UVGC_495_11,(2,2,5):C.UVGC_495_10,(5,2,4):C.UVGC_494_8,(5,2,5):C.UVGC_494_9,(1,2,4):C.UVGC_494_8,(1,2,5):C.UVGC_494_9,(7,2,0):C.UVGC_631_295,(7,2,2):C.UVGC_631_296,(7,2,3):C.UVGC_631_297,(7,2,4):C.UVGC_630_290,(7,2,5):C.UVGC_632_303,(7,2,6):C.UVGC_631_300,(7,2,7):C.UVGC_631_301,(7,2,8):C.UVGC_631_302,(4,2,4):C.UVGC_494_8,(4,2,5):C.UVGC_494_9,(3,2,4):C.UVGC_494_8,(3,2,5):C.UVGC_494_9,(8,2,0):C.UVGC_630_287,(8,2,2):C.UVGC_630_288,(8,2,3):C.UVGC_630_289,(8,2,4):C.UVGC_630_290,(8,2,5):C.UVGC_630_291,(8,2,6):C.UVGC_630_292,(8,2,7):C.UVGC_630_293,(8,2,8):C.UVGC_630_294,(6,2,1):C.UVGC_499_16,(6,2,5):C.UVGC_497_12,(11,2,4):C.UVGC_498_14,(11,2,5):C.UVGC_498_15,(10,2,4):C.UVGC_498_14,(10,2,5):C.UVGC_498_15,(9,2,4):C.UVGC_497_12,(9,2,5):C.UVGC_497_13})

V_126 = CTVertex(name = 'V_126',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.G ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.G] ], [ [P.G] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,3):C.UVGC_502_19,(0,1,0):C.UVGC_515_23,(0,1,1):C.UVGC_515_24,(0,1,2):C.UVGC_515_25,(0,1,4):C.UVGC_515_26,(0,1,5):C.UVGC_515_27,(0,1,6):C.UVGC_515_28,(0,1,7):C.UVGC_515_29,(0,1,8):C.UVGC_515_30,(0,1,3):C.UVGC_545_81,(0,2,0):C.UVGC_515_23,(0,2,1):C.UVGC_515_24,(0,2,2):C.UVGC_515_25,(0,2,4):C.UVGC_515_26,(0,2,5):C.UVGC_515_27,(0,2,6):C.UVGC_515_28,(0,2,7):C.UVGC_515_29,(0,2,8):C.UVGC_515_30,(0,2,3):C.UVGC_545_81})

V_127 = CTVertex(name = 'V_127',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.G ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.G] ], [ [P.ghG] ], [ [P.G, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_502_19,(0,1,0):C.UVGC_515_23,(0,1,1):C.UVGC_515_24,(0,1,2):C.UVGC_515_25,(0,1,3):C.UVGC_515_26,(0,1,4):C.UVGC_515_27,(0,1,6):C.UVGC_515_28,(0,1,7):C.UVGC_515_29,(0,1,8):C.UVGC_515_30,(0,1,5):C.UVGC_565_121,(0,2,0):C.UVGC_515_23,(0,2,1):C.UVGC_515_24,(0,2,2):C.UVGC_515_25,(0,2,3):C.UVGC_515_26,(0,2,4):C.UVGC_515_27,(0,2,6):C.UVGC_515_28,(0,2,7):C.UVGC_515_29,(0,2,8):C.UVGC_515_30,(0,2,5):C.UVGC_565_121})

V_128 = CTVertex(name = 'V_128',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.G ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.G] ], [ [P.c] ], [ [P.d] ], [ [P.G] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,1):C.UVGC_502_19,(0,1,0):C.UVGC_515_23,(0,1,2):C.UVGC_515_24,(0,1,3):C.UVGC_515_25,(0,1,4):C.UVGC_515_26,(0,1,5):C.UVGC_515_27,(0,1,6):C.UVGC_515_28,(0,1,7):C.UVGC_515_29,(0,1,8):C.UVGC_515_30,(0,1,1):C.UVGC_515_31,(0,2,0):C.UVGC_515_23,(0,2,2):C.UVGC_515_24,(0,2,3):C.UVGC_515_25,(0,2,4):C.UVGC_515_26,(0,2,5):C.UVGC_515_27,(0,2,6):C.UVGC_515_28,(0,2,7):C.UVGC_515_29,(0,2,8):C.UVGC_515_30,(0,2,1):C.UVGC_515_31})

V_129 = CTVertex(name = 'V_129',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.G ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.G] ], [ [P.ghG] ], [ [P.G, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_502_19,(0,1,0):C.UVGC_515_23,(0,1,1):C.UVGC_515_24,(0,1,2):C.UVGC_515_25,(0,1,3):C.UVGC_515_26,(0,1,4):C.UVGC_515_27,(0,1,6):C.UVGC_515_28,(0,1,7):C.UVGC_515_29,(0,1,8):C.UVGC_515_30,(0,1,5):C.UVGC_638_323,(0,2,0):C.UVGC_515_23,(0,2,1):C.UVGC_515_24,(0,2,2):C.UVGC_515_25,(0,2,3):C.UVGC_515_26,(0,2,4):C.UVGC_515_27,(0,2,6):C.UVGC_515_28,(0,2,7):C.UVGC_515_29,(0,2,8):C.UVGC_515_30,(0,2,5):C.UVGC_638_323})

V_130 = CTVertex(name = 'V_130',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.G ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.G] ], [ [P.d] ], [ [P.G] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_502_19,(0,1,0):C.UVGC_515_23,(0,1,1):C.UVGC_515_24,(0,1,3):C.UVGC_515_25,(0,1,4):C.UVGC_515_26,(0,1,5):C.UVGC_515_27,(0,1,6):C.UVGC_515_28,(0,1,7):C.UVGC_515_29,(0,1,8):C.UVGC_515_30,(0,1,2):C.UVGC_525_41,(0,2,0):C.UVGC_515_23,(0,2,1):C.UVGC_515_24,(0,2,3):C.UVGC_515_25,(0,2,4):C.UVGC_515_26,(0,2,5):C.UVGC_515_27,(0,2,6):C.UVGC_515_28,(0,2,7):C.UVGC_515_29,(0,2,8):C.UVGC_515_30,(0,2,2):C.UVGC_525_41})

V_131 = CTVertex(name = 'V_131',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.G] ], [ [P.ghG] ], [ [P.G, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_502_19,(0,1,0):C.UVGC_515_23,(0,1,1):C.UVGC_515_24,(0,1,2):C.UVGC_515_25,(0,1,3):C.UVGC_515_26,(0,1,4):C.UVGC_515_27,(0,1,6):C.UVGC_515_28,(0,1,7):C.UVGC_515_29,(0,1,8):C.UVGC_515_30,(0,1,5):C.UVGC_585_161,(0,2,0):C.UVGC_515_23,(0,2,1):C.UVGC_515_24,(0,2,2):C.UVGC_515_25,(0,2,3):C.UVGC_515_26,(0,2,4):C.UVGC_515_27,(0,2,6):C.UVGC_515_28,(0,2,7):C.UVGC_515_29,(0,2,8):C.UVGC_515_30,(0,2,5):C.UVGC_585_161})

V_132 = CTVertex(name = 'V_132',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.A ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_501_18,(0,1,0):C.UVGC_544_80,(0,2,0):C.UVGC_544_80})

V_133 = CTVertex(name = 'V_133',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.A ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_501_18,(0,1,0):C.UVGC_564_120,(0,2,0):C.UVGC_564_120})

V_134 = CTVertex(name = 'V_134',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.A ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_501_18,(0,1,0):C.UVGC_514_22,(0,2,0):C.UVGC_514_22})

V_135 = CTVertex(name = 'V_135',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_548_86,(0,1,0):C.UVGC_549_87})

V_136 = CTVertex(name = 'V_136',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_568_126,(0,1,0):C.UVGC_569_127})

V_137 = CTVertex(name = 'V_137',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_517_33,(0,1,0):C.UVGC_518_34})

V_138 = CTVertex(name = 'V_138',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.A ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_503_20,(0,1,0):C.UVGC_637_322,(0,2,0):C.UVGC_637_322})

V_139 = CTVertex(name = 'V_139',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.A ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_503_20,(0,1,0):C.UVGC_524_40,(0,2,0):C.UVGC_524_40})

V_140 = CTVertex(name = 'V_140',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.A ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_503_20,(0,1,0):C.UVGC_584_160,(0,2,0):C.UVGC_584_160})

V_141 = CTVertex(name = 'V_141',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_643_334,(0,1,0):C.UVGC_644_335})

V_142 = CTVertex(name = 'V_142',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_528_46,(0,1,0):C.UVGC_529_47})

V_143 = CTVertex(name = 'V_143',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_590_172,(0,1,0):C.UVGC_591_173})

V_144 = CTVertex(name = 'V_144',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.G] ], [ [P.d, P.G, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_640_325,(0,0,2):C.UVGC_640_326,(0,0,1):C.UVGC_640_327})

V_145 = CTVertex(name = 'V_145',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.G, P.s] ], [ [P.G, P.s, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_641_328,(0,0,2):C.UVGC_641_329,(0,0,1):C.UVGC_641_330})

V_146 = CTVertex(name = 'V_146',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.G] ], [ [P.b, P.G, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_642_331,(0,0,2):C.UVGC_642_332,(0,0,1):C.UVGC_642_333})

V_147 = CTVertex(name = 'V_147',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.G] ], [ [P.c, P.G] ], [ [P.d, P.G] ] ],
                 couplings = {(0,0,1):C.UVGC_547_83,(0,0,2):C.UVGC_547_84,(0,0,0):C.UVGC_547_85})

V_148 = CTVertex(name = 'V_148',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.G] ], [ [P.c, P.G, P.s] ], [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_567_123,(0,0,2):C.UVGC_567_124,(0,0,1):C.UVGC_567_125})

V_149 = CTVertex(name = 'V_149',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.G] ], [ [P.b, P.G] ], [ [P.c, P.G] ] ],
                 couplings = {(0,0,1):C.UVGC_527_43,(0,0,2):C.UVGC_527_44,(0,0,0):C.UVGC_527_45})

V_150 = CTVertex(name = 'V_150',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.G] ], [ [P.d, P.G, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_587_163,(0,0,2):C.UVGC_587_164,(0,0,1):C.UVGC_587_165})

V_151 = CTVertex(name = 'V_151',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.G, P.s] ], [ [P.G, P.s, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_588_166,(0,0,2):C.UVGC_588_167,(0,0,1):C.UVGC_588_168})

V_152 = CTVertex(name = 'V_152',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.G] ], [ [P.b, P.G, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_589_169,(0,0,2):C.UVGC_589_170,(0,0,1):C.UVGC_589_171})

V_153 = CTVertex(name = 'V_153',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.G] ], [ [P.d, P.G, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_661_376,(0,0,2):C.UVGC_661_377,(0,0,1):C.UVGC_661_378})

V_154 = CTVertex(name = 'V_154',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.G] ], [ [P.c, P.G] ], [ [P.d, P.G] ] ],
                 couplings = {(0,0,1):C.UVGC_558_104,(0,0,2):C.UVGC_558_105,(0,0,0):C.UVGC_558_106})

V_155 = CTVertex(name = 'V_155',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.G] ], [ [P.d, P.G, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_608_214,(0,0,2):C.UVGC_608_215,(0,0,1):C.UVGC_608_216})

V_156 = CTVertex(name = 'V_156',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.G, P.s] ], [ [P.G, P.s, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_666_391,(0,0,2):C.UVGC_666_392,(0,0,1):C.UVGC_666_393})

V_157 = CTVertex(name = 'V_157',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.G] ], [ [P.c, P.G, P.s] ], [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_578_144,(0,0,2):C.UVGC_578_145,(0,0,1):C.UVGC_578_146})

V_158 = CTVertex(name = 'V_158',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.G, P.s] ], [ [P.G, P.s, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_613_229,(0,0,2):C.UVGC_613_230,(0,0,1):C.UVGC_613_231})

V_159 = CTVertex(name = 'V_159',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.G] ], [ [P.b, P.G, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_671_406,(0,0,2):C.UVGC_671_407,(0,0,1):C.UVGC_671_408})

V_160 = CTVertex(name = 'V_160',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.G] ], [ [P.b, P.G] ], [ [P.c, P.G] ] ],
                 couplings = {(0,0,1):C.UVGC_538_64,(0,0,2):C.UVGC_538_65,(0,0,0):C.UVGC_538_66})

V_161 = CTVertex(name = 'V_161',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.G] ], [ [P.b, P.G, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_618_244,(0,0,2):C.UVGC_618_245,(0,0,1):C.UVGC_618_246})

V_162 = CTVertex(name = 'V_162',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.G] ], [ [P.d, P.G, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_653_356,(0,0,2):C.UVGC_653_357,(0,0,1):C.UVGC_653_358,(0,1,0):C.UVGC_647_342,(0,1,2):C.UVGC_647_343,(0,1,1):C.UVGC_647_344})

V_163 = CTVertex(name = 'V_163',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.G, P.s] ], [ [P.G, P.s, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_654_359,(0,0,2):C.UVGC_654_360,(0,0,1):C.UVGC_654_361,(0,1,0):C.UVGC_649_348,(0,1,2):C.UVGC_649_349,(0,1,1):C.UVGC_649_350})

V_164 = CTVertex(name = 'V_164',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.u, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.G] ], [ [P.b, P.G, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_655_362,(0,0,2):C.UVGC_655_363,(0,0,1):C.UVGC_655_364,(0,1,0):C.UVGC_645_336,(0,1,2):C.UVGC_645_337,(0,1,1):C.UVGC_645_338})

V_165 = CTVertex(name = 'V_165',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.d, P.G] ], [ [P.c, P.G] ], [ [P.d, P.G] ] ],
                 couplings = {(0,0,1):C.UVGC_550_88,(0,0,2):C.UVGC_550_89,(0,0,0):C.UVGC_550_90,(0,1,1):C.UVGC_554_96,(0,1,2):C.UVGC_554_97,(0,1,0):C.UVGC_554_98})

V_166 = CTVertex(name = 'V_166',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.G] ], [ [P.c, P.G, P.s] ], [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_570_128,(0,0,2):C.UVGC_570_129,(0,0,1):C.UVGC_570_130,(0,1,0):C.UVGC_574_136,(0,1,2):C.UVGC_574_137,(0,1,1):C.UVGC_574_138})

V_167 = CTVertex(name = 'V_167',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.c, P.G] ], [ [P.b, P.G] ], [ [P.c, P.G] ] ],
                 couplings = {(0,0,1):C.UVGC_534_56,(0,0,2):C.UVGC_534_57,(0,0,0):C.UVGC_534_58,(0,1,1):C.UVGC_530_48,(0,1,2):C.UVGC_530_49,(0,1,0):C.UVGC_530_50})

V_168 = CTVertex(name = 'V_168',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.G] ], [ [P.d, P.G, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_600_194,(0,0,2):C.UVGC_600_195,(0,0,1):C.UVGC_600_196,(0,1,0):C.UVGC_594_180,(0,1,2):C.UVGC_594_181,(0,1,1):C.UVGC_594_182})

V_169 = CTVertex(name = 'V_169',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.G, P.s] ], [ [P.G, P.s, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_601_197,(0,0,2):C.UVGC_601_198,(0,0,1):C.UVGC_601_199,(0,1,0):C.UVGC_596_186,(0,1,2):C.UVGC_596_187,(0,1,1):C.UVGC_596_188})

V_170 = CTVertex(name = 'V_170',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.G] ], [ [P.b, P.G, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_602_200,(0,0,2):C.UVGC_602_201,(0,0,1):C.UVGC_602_202,(0,1,0):C.UVGC_592_174,(0,1,2):C.UVGC_592_175,(0,1,1):C.UVGC_592_176})

V_171 = CTVertex(name = 'V_171',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.H3p__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.G] ], [ [P.d, P.G, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_658_367,(0,0,2):C.UVGC_658_368,(0,0,1):C.UVGC_658_369,(0,1,0):C.UVGC_648_345,(0,1,2):C.UVGC_648_346,(0,1,1):C.UVGC_648_347})

V_172 = CTVertex(name = 'V_172',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.H3p__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.G, P.s] ], [ [P.G, P.s, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_659_370,(0,0,2):C.UVGC_659_371,(0,0,1):C.UVGC_659_372,(0,1,0):C.UVGC_650_351,(0,1,2):C.UVGC_650_352,(0,1,1):C.UVGC_650_353})

V_173 = CTVertex(name = 'V_173',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.u, P.H3p__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.G] ], [ [P.b, P.G, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_660_373,(0,0,2):C.UVGC_660_374,(0,0,1):C.UVGC_660_375,(0,1,0):C.UVGC_646_339,(0,1,2):C.UVGC_646_340,(0,1,1):C.UVGC_646_341})

V_174 = CTVertex(name = 'V_174',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.H3p__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.d, P.G] ], [ [P.c, P.G] ], [ [P.d, P.G] ] ],
                 couplings = {(0,0,1):C.UVGC_551_91,(0,0,2):C.UVGC_551_92,(0,0,0):C.UVGC_551_93,(0,1,1):C.UVGC_557_101,(0,1,2):C.UVGC_557_102,(0,1,0):C.UVGC_557_103})

V_175 = CTVertex(name = 'V_175',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.H3p__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.G] ], [ [P.c, P.G, P.s] ], [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_571_131,(0,0,2):C.UVGC_571_132,(0,0,1):C.UVGC_571_133,(0,1,0):C.UVGC_577_141,(0,1,2):C.UVGC_577_142,(0,1,1):C.UVGC_577_143})

V_176 = CTVertex(name = 'V_176',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.c, P.H3p__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.c, P.G] ], [ [P.b, P.G] ], [ [P.c, P.G] ] ],
                 couplings = {(0,0,1):C.UVGC_537_61,(0,0,2):C.UVGC_537_62,(0,0,0):C.UVGC_537_63,(0,1,1):C.UVGC_531_51,(0,1,2):C.UVGC_531_52,(0,1,0):C.UVGC_531_53})

V_177 = CTVertex(name = 'V_177',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.t, P.H3p__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.G] ], [ [P.d, P.G, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_605_205,(0,0,2):C.UVGC_605_206,(0,0,1):C.UVGC_605_207,(0,1,0):C.UVGC_595_183,(0,1,2):C.UVGC_595_184,(0,1,1):C.UVGC_595_185})

V_178 = CTVertex(name = 'V_178',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.t, P.H3p__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.G, P.s] ], [ [P.G, P.s, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_606_208,(0,0,2):C.UVGC_606_209,(0,0,1):C.UVGC_606_210,(0,1,0):C.UVGC_597_189,(0,1,2):C.UVGC_597_190,(0,1,1):C.UVGC_597_191})

V_179 = CTVertex(name = 'V_179',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.H3p__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.G] ], [ [P.b, P.G, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_607_211,(0,0,2):C.UVGC_607_212,(0,0,1):C.UVGC_607_213,(0,1,0):C.UVGC_593_177,(0,1,2):C.UVGC_593_178,(0,1,1):C.UVGC_593_179})

V_180 = CTVertex(name = 'V_180',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.G] ], [ [P.d, P.G, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_662_379,(0,0,2):C.UVGC_662_380,(0,0,1):C.UVGC_662_381,(0,1,0):C.UVGC_664_385,(0,1,2):C.UVGC_664_386,(0,1,1):C.UVGC_664_387})

V_181 = CTVertex(name = 'V_181',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.d, P.G] ], [ [P.c, P.G] ], [ [P.d, P.G] ] ],
                 couplings = {(0,0,1):C.UVGC_561_113,(0,0,2):C.UVGC_561_114,(0,0,0):C.UVGC_561_115,(0,1,1):C.UVGC_559_107,(0,1,2):C.UVGC_559_108,(0,1,0):C.UVGC_559_109})

V_182 = CTVertex(name = 'V_182',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.d, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.G] ], [ [P.d, P.G, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_609_217,(0,0,2):C.UVGC_609_218,(0,0,1):C.UVGC_609_219,(0,1,0):C.UVGC_611_223,(0,1,2):C.UVGC_611_224,(0,1,1):C.UVGC_611_225})

V_183 = CTVertex(name = 'V_183',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.G, P.s] ], [ [P.G, P.s, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_667_394,(0,0,2):C.UVGC_667_395,(0,0,1):C.UVGC_667_396,(0,1,0):C.UVGC_669_400,(0,1,2):C.UVGC_669_401,(0,1,1):C.UVGC_669_402})

V_184 = CTVertex(name = 'V_184',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.G] ], [ [P.c, P.G, P.s] ], [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_581_153,(0,0,2):C.UVGC_581_154,(0,0,1):C.UVGC_581_155,(0,1,0):C.UVGC_579_147,(0,1,2):C.UVGC_579_148,(0,1,1):C.UVGC_579_149})

V_185 = CTVertex(name = 'V_185',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.s, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.G, P.s] ], [ [P.G, P.s, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_614_232,(0,0,2):C.UVGC_614_233,(0,0,1):C.UVGC_614_234,(0,1,0):C.UVGC_616_238,(0,1,2):C.UVGC_616_239,(0,1,1):C.UVGC_616_240})

V_186 = CTVertex(name = 'V_186',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.G] ], [ [P.b, P.G, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_672_409,(0,0,2):C.UVGC_672_410,(0,0,1):C.UVGC_672_411,(0,1,0):C.UVGC_674_415,(0,1,2):C.UVGC_674_416,(0,1,1):C.UVGC_674_417})

V_187 = CTVertex(name = 'V_187',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.c, P.G] ], [ [P.b, P.G] ], [ [P.c, P.G] ] ],
                 couplings = {(0,0,1):C.UVGC_539_67,(0,0,2):C.UVGC_539_68,(0,0,0):C.UVGC_539_69,(0,1,1):C.UVGC_541_73,(0,1,2):C.UVGC_541_74,(0,1,0):C.UVGC_541_75})

V_188 = CTVertex(name = 'V_188',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.G] ], [ [P.b, P.G, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_619_247,(0,0,2):C.UVGC_619_248,(0,0,1):C.UVGC_619_249,(0,1,0):C.UVGC_621_253,(0,1,2):C.UVGC_621_254,(0,1,1):C.UVGC_621_255})

V_189 = CTVertex(name = 'V_189',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.H3p ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.G] ], [ [P.d, P.G, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_663_382,(0,0,2):C.UVGC_663_383,(0,0,1):C.UVGC_663_384,(0,1,0):C.UVGC_665_388,(0,1,2):C.UVGC_665_389,(0,1,1):C.UVGC_665_390})

V_190 = CTVertex(name = 'V_190',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.H3p ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.d, P.G] ], [ [P.c, P.G] ], [ [P.d, P.G] ] ],
                 couplings = {(0,0,1):C.UVGC_562_116,(0,0,2):C.UVGC_562_117,(0,0,0):C.UVGC_562_118,(0,1,1):C.UVGC_560_110,(0,1,2):C.UVGC_560_111,(0,1,0):C.UVGC_560_112})

V_191 = CTVertex(name = 'V_191',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.d, P.H3p ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.G] ], [ [P.d, P.G, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_610_220,(0,0,2):C.UVGC_610_221,(0,0,1):C.UVGC_610_222,(0,1,0):C.UVGC_612_226,(0,1,2):C.UVGC_612_227,(0,1,1):C.UVGC_612_228})

V_192 = CTVertex(name = 'V_192',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.H3p ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.G, P.s] ], [ [P.G, P.s, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_668_397,(0,0,2):C.UVGC_668_398,(0,0,1):C.UVGC_668_399,(0,1,0):C.UVGC_670_403,(0,1,2):C.UVGC_670_404,(0,1,1):C.UVGC_670_405})

V_193 = CTVertex(name = 'V_193',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.H3p ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.G] ], [ [P.c, P.G, P.s] ], [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_582_156,(0,0,2):C.UVGC_582_157,(0,0,1):C.UVGC_582_158,(0,1,0):C.UVGC_580_150,(0,1,2):C.UVGC_580_151,(0,1,1):C.UVGC_580_152})

V_194 = CTVertex(name = 'V_194',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.s, P.H3p ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.G, P.s] ], [ [P.G, P.s, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_615_235,(0,0,2):C.UVGC_615_236,(0,0,1):C.UVGC_615_237,(0,1,0):C.UVGC_617_241,(0,1,2):C.UVGC_617_242,(0,1,1):C.UVGC_617_243})

V_195 = CTVertex(name = 'V_195',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.b, P.H3p ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.G] ], [ [P.b, P.G, P.u] ], [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_673_412,(0,0,2):C.UVGC_673_413,(0,0,1):C.UVGC_673_414,(0,1,0):C.UVGC_675_418,(0,1,2):C.UVGC_675_419,(0,1,1):C.UVGC_675_420})

V_196 = CTVertex(name = 'V_196',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.b, P.H3p ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.c, P.G] ], [ [P.b, P.G] ], [ [P.c, P.G] ] ],
                 couplings = {(0,0,1):C.UVGC_540_70,(0,0,2):C.UVGC_540_71,(0,0,0):C.UVGC_540_72,(0,1,1):C.UVGC_542_76,(0,1,2):C.UVGC_542_77,(0,1,0):C.UVGC_542_78})

V_197 = CTVertex(name = 'V_197',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.H3p ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.G] ], [ [P.b, P.G, P.t] ], [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_620_250,(0,0,2):C.UVGC_620_251,(0,0,1):C.UVGC_620_252,(0,1,0):C.UVGC_622_256,(0,1,2):C.UVGC_622_257,(0,1,1):C.UVGC_622_258})

V_198 = CTVertex(name = 'V_198',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.d, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_553_95})

V_199 = CTVertex(name = 'V_199',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_573_135})

V_200 = CTVertex(name = 'V_200',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.b, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_520_36})

V_201 = CTVertex(name = 'V_201',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.d, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_552_94})

V_202 = CTVertex(name = 'V_202',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_572_134})

V_203 = CTVertex(name = 'V_203',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_519_35})

V_204 = CTVertex(name = 'V_204',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.d, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_555_99})

V_205 = CTVertex(name = 'V_205',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_575_139})

V_206 = CTVertex(name = 'V_206',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_521_37})

V_207 = CTVertex(name = 'V_207',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.H3z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.d, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_556_100})

V_208 = CTVertex(name = 'V_208',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.H3z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_576_140})

V_209 = CTVertex(name = 'V_209',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H3z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.b, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_522_38})

V_210 = CTVertex(name = 'V_210',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_652_355})

V_211 = CTVertex(name = 'V_211',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_533_55})

V_212 = CTVertex(name = 'V_212',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_599_193})

V_213 = CTVertex(name = 'V_213',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_651_354})

V_214 = CTVertex(name = 'V_214',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_532_54})

V_215 = CTVertex(name = 'V_215',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.HL ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_598_192})

V_216 = CTVertex(name = 'V_216',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_656_365})

V_217 = CTVertex(name = 'V_217',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_535_59})

V_218 = CTVertex(name = 'V_218',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.HH ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_603_203})

V_219 = CTVertex(name = 'V_219',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.H3z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_657_366})

V_220 = CTVertex(name = 'V_220',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.H3z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_536_60})

V_221 = CTVertex(name = 'V_221',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H3z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_604_204})

V_222 = CTVertex(name = 'V_222',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.G, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_639_324,(0,1,0):C.UVGC_636_321})

V_223 = CTVertex(name = 'V_223',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.c, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_526_42,(0,1,0):C.UVGC_523_39})

V_224 = CTVertex(name = 'V_224',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.G, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_586_162,(0,1,0):C.UVGC_583_159})

V_225 = CTVertex(name = 'V_225',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.d, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_546_82,(0,1,0):C.UVGC_543_79})

V_226 = CTVertex(name = 'V_226',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.G, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_566_122,(0,1,0):C.UVGC_563_119})

V_227 = CTVertex(name = 'V_227',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.b, P.G] ] ],
                 couplings = {(0,0,0):C.UVGC_516_32,(0,1,0):C.UVGC_513_21})

V_228 = CTVertex(name = 'V_228',
                 type = 'UV',
                 particles = [ P.G, P.G ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.G] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,1,0):C.UVGC_623_259,(0,1,1):C.UVGC_623_260,(0,1,2):C.UVGC_623_261,(0,1,5):C.UVGC_623_262,(0,1,6):C.UVGC_623_263,(0,1,7):C.UVGC_623_264,(0,0,3):C.UVGC_491_2,(0,0,4):C.UVGC_491_3})

