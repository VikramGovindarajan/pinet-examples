# SPX benchmark test

circuit1=comp.Circuit("circuit1")
circuit1.assign_fluid("Na6","User")

circuit1.add_node("node1", elevation= 0.0)
circuit1.add_node("node2", elevation= 4.3)
#yet to add inlet and outlet pipe data.
#yet to add material properties of fertile material.

#parameters
SA_IC = 190
SA_OC = 168
SA_RB = 225

Pins_fis = 271
Pins_fer = 91

H_inlet=0.2
H_gap=  0.55
H_fer = 0.3
H_fis = 1
H_trans = 0.2
H_outlet = 1.2


pi = math.pi
L = 0.1651/1.732

#nominal power inputs

Pow_IC = 1.75E9
Pow_OC = 1.208E9
Pow_RB = 3.188E7

#preliminary calculations


def fun(flow_elem,WallTemp):
    Pe = flow_elem.ther_gues.rhomass()*flow_elem.velocity*flow_elem.diameter*flow_elem.ther_gues.cpmass()/flow_elem.ther_gues.conductivity()
    Nu = 5.0 + 0.025*Pe**0.8
    h = Nu * flow_elem.ther_gues.conductivity() / flow_elem.diameter
    return h
#_____________________________________________________________________________________________
#CHANNEL 1 (inner core) (IC)

#nodes (data= table 3)
circuit1.add_node("node11", elevation= 0.2)
circuit1.add_node("node12", elevation= 0.75)
circuit1.add_node("node13", elevation= 1.05)
circuit1.add_node("node14", elevation= 2.05)
circuit1.add_node("node15", elevation= 2.35)
circuit1.add_node("node16", elevation= 2.9)
circuit1.add_node("node17", elevation= 3.1)

#parameters for the pipes

#Inlet section
A1_In = 236.1E-4
D1_In  = 0.1651

#Pin bundle
A1_pin = 80.23E-4
D1_pin  = 0.004084

#Upper transition region
A1_UT = 236.1E-4
D1_UT  = 0.1651

#Outlet region
A1_OT = 38.48E-4
D1_OT  = 0.07

#Pipe 
circuit1.add_pipe("pipe11", D1_In,  H_inlet, "node1",  "node11", 0.001, 1, 2,  cfarea=A1_In,  npar=SA_IC,Kforward=156)
circuit1.add_pipe("pipe12", D1_pin, H_gap,   "node11", "node12", 0.001, 1, 5,  cfarea=A1_pin, npar=SA_IC)
circuit1.add_pipe("pipe13", D1_pin, H_fer,   "node12", "node13", 0.001, 1, 3,  cfarea=A1_pin, npar=SA_IC)
circuit1.add_pipe("pipe14", D1_pin, H_fis,   "node13", "node14", 0.001, 1, 10, cfarea=A1_pin, npar=SA_IC)
circuit1.add_pipe("pipe15", D1_pin, H_fer,   "node14", "node15", 0.001, 1, 3,  cfarea=A1_pin, npar=SA_IC)
circuit1.add_pipe("pipe16", D1_pin, H_gap,   "node15", "node16", 0.001, 1, 5,  cfarea=A1_pin, npar=SA_IC)
circuit1.add_pipe("pipe17", D1_UT,  H_trans, "node16", "node17", 0.001, 1, 2,  cfarea=A1_UT,  npar=SA_IC)
circuit1.add_pipe("pipe18", D1_OT,  H_outlet,"node17", "node2",  0.001, 1, 12, cfarea=A1_OT,  npar=SA_IC)

#Snodes
HTcomp.SNode("snode12")
HTcomp.SNode("snode13")
HTcomp.SNode("snode14")
HTcomp.SNode("snode15")
HTcomp.SNode("snode16")

#parameters for heatslab


P1_pin  = pi*8.5E-3*Pins_fis*SA_IC
P1_clad = pi*7.37E-3*Pins_fis*SA_IC
P1_He   = pi*7.14E-3*Pins_fis*SA_IC
P1_pelt = pi*2E-3*Pins_fis*SA_IC


#Lower gap()
hslab11=HTcomp.HSlab("hslab11","pipe12","pipe",[fun],"snode12","hflux",0.0,P1_pin*H_gap,nlayers=1)
hslab11.add_layer(thk_elem=0.565E-3,thk_cros=H_gap,nnodes=2,darea=P1_clad*H_gap,solname='SS13',sollib="User")

#Lower fertile region
hslab12=HTcomp.HSlab("hslab12","pipe13","pipe",[fun],"snode13","hflux",0.0,P1_pin*H_fer,nlayers=3)
hslab12.add_layer(thk_elem=0.565E-3,thk_cros=H_fer,nnodes=2,darea=P1_clad*H_fer,solname='SS13',  sollib="User")
hslab12.add_layer(thk_elem=0.115E-3,thk_cros=H_fer,nnodes=2,darea=P1_He*H_fer,  solname='gap13', sollib="User")
hslab12.add_layer(thk_elem=2.570E-3,thk_cros=H_fer,nnodes=3,darea=P1_pelt*H_fer,solname='MOX13', sollib="User",heat_input= 8.938E-3*Pow_IC,AFF=[0.151,0.264,0.585])

#fissile region
hslab13=HTcomp.HSlab("hslab13","pipe14","pipe",[fun],"snode14","hflux",0.0,P1_pin*H_fis,nlayers=3)
hslab13.add_layer(thk_elem=0.565E-3,thk_cros=H_fis,nnodes=2,darea=P1_clad*H_fis,solname='SS13', sollib="User")
hslab13.add_layer(thk_elem=0.115E-3,thk_cros=H_fis,nnodes=2,darea=P1_He*H_fis,  solname='gap13',sollib="User")
hslab13.add_layer(thk_elem=2.570E-3,thk_cros=H_fis,nnodes=3,darea=P1_pelt*H_fis,solname='MOX13',sollib="User",heat_input= 0.98542*Pow_IC,AFF=[0.0787,0.1,0.118,0.128,0.129,0.122,0.108,0.091,0.072,0.0533])

#Upper fertile region
hslab14=HTcomp.HSlab("hslab14","pipe15","pipe",[fun],"snode15","hflux",0.0,P1_pin*H_fer,nlayers=3)
hslab14.add_layer(thk_elem=0.565E-3,thk_cros=H_fer,nnodes=2,darea=P1_clad*H_fer,solname='SS13',sollib="User")
hslab14.add_layer(thk_elem=0.115E-3,thk_cros=H_fer,nnodes=2,darea=P1_He*H_fer,  solname='gap13',sollib="User")
hslab14.add_layer(thk_elem=2.570E-3,thk_cros=H_fer,nnodes=3,darea=P1_pelt*H_fer,solname='MOX13',sollib="User",heat_input= 5.6213E-3*Pow_IC,AFF=[0.616,0.257,0.127])

#Upper gap
hslab15=HTcomp.HSlab("hslab15","pipe16","pipe",[fun],"snode16","hflux",0.0,P1_pin*H_gap,nlayers=1)
hslab15.add_layer(thk_elem=0.565E-3,thk_cros=H_gap,nnodes=2,darea=P1_clad*H_gap,solname='SS13',sollib="User")

#___________________________________________________________________________________________________________________________________________________

#CHANNEL 2 (outer core) (OC)

#nodes (data= table 3)
circuit1.add_node("node21", elevation= 0.2)
circuit1.add_node("node22", elevation= 0.75)
circuit1.add_node("node23", elevation= 1.05)
circuit1.add_node("node24", elevation= 2.05)
circuit1.add_node("node25", elevation= 2.35)
circuit1.add_node("node26", elevation= 2.9)
circuit1.add_node("node27", elevation= 3.1)

#parameters for the pipes

#Inlet section
A2_In = 236.1E-4
D2_In  = 0.1651

#Pin bundle
A2_pin = 80.23E-4
D2_pin  = 0.004084

#Upper transition region
A2_UT = 236.1E-4
D2_UT  = 0.1651

#Outlet region
A2_OT = 0.003848
D2_OT  = 0.07

#Pipe 
circuit1.add_pipe("pipe21",D2_In, H_inlet, "node1", "node21",0.001,1,2, cfarea=A2_In, npar=SA_OC,Kforward=260.)
circuit1.add_pipe("pipe22",D2_pin,H_gap,   "node21","node22",0.001,1,5, cfarea=A2_pin,npar=SA_OC)
circuit1.add_pipe("pipe23",D2_pin,H_fer,   "node22","node23",0.001,1,3, cfarea=A2_pin,npar=SA_OC)
circuit1.add_pipe("pipe24",D2_pin,H_fis,   "node23","node24",0.001,1,10,cfarea=A2_pin,npar=SA_OC)
circuit1.add_pipe("pipe25",D2_pin,H_fer,   "node24","node25",0.001,1,3, cfarea=A2_pin,npar=SA_OC)
circuit1.add_pipe("pipe26",D2_pin,H_gap,   "node25","node26",0.001,1,5, cfarea=A2_pin,npar=SA_OC)
circuit1.add_pipe("pipe27",D2_UT, H_trans, "node26","node27",0.001,1,2, cfarea=A2_UT, npar=SA_OC)
circuit1.add_pipe("pipe28",D2_OT, H_outlet,"node27","node2", 0.001,1,12,cfarea=A2_OT, npar=SA_OC)
#Snodes
HTcomp.SNode("snode22")
HTcomp.SNode("snode23")
HTcomp.SNode("snode24")
HTcomp.SNode("snode25")
HTcomp.SNode("snode26")

#parameters for heatslab


P2_pin  = pi*8.5E-3*Pins_fis*SA_OC
P2_clad = pi*7.37E-3*Pins_fis*SA_OC
P2_He   = pi*7.14E-3*Pins_fis*SA_OC
P2_pelt = pi*2E-3*Pins_fis*SA_OC


#Lower gap
hslab21=HTcomp.HSlab("hslab21","pipe22","pipe",[fun],"snode22","hflux",0.0,P2_pin*H_gap,nlayers=1)
hslab21.add_layer(thk_elem=0.565E-3,thk_cros=H_gap,nnodes=2,darea=P2_clad*H_gap,solname='SS13',sollib="User")

#Lower fertile region
hslab22=HTcomp.HSlab("hslab22","pipe23","pipe",[fun],"snode23","hflux",0.0,P2_pin*H_fer,nlayers=3)
hslab22.add_layer(thk_elem=0.565E-3,thk_cros=H_fer,nnodes=2,darea=P2_clad*H_fer,solname='SS13', sollib="User")
hslab22.add_layer(thk_elem=0.115E-3,thk_cros=H_fer,nnodes=2,darea=P2_He*H_fer,  solname='gap13',sollib="User")
hslab22.add_layer(thk_elem=2.570E-3,thk_cros=H_fer,nnodes=3,darea=P2_pelt*H_fer,solname='MOX13',sollib="User",heat_input= 0.007422*Pow_OC,AFF=[0.141,0.257,0.602])

#fissile region
hslab23=HTcomp.HSlab("hslab23","pipe24","pipe",[fun],"snode24","hflux",0.0,P2_pin*H_fis,nlayers=3)
hslab23.add_layer(thk_elem=0.565E-3,thk_cros=H_fis,nnodes=2,darea=P2_clad*H_fis,solname='SS13', sollib="User")
hslab23.add_layer(thk_elem=0.115E-3,thk_cros=H_fis,nnodes=2,darea=P2_He*H_fis,  solname='gap13',sollib="User")
hslab23.add_layer(thk_elem=2.570E-3,thk_cros=H_fis,nnodes=3,darea=P2_pelt*H_fis,solname='MOX13',sollib="User",heat_input= 0.98976*Pow_OC,AFF=[0.077,0.099,0.117,0.127,0.129,0.122,0.108,0.09,0.073,0.058])


#Upper fertile region
hslab24=HTcomp.HSlab("hslab24","pipe25","pipe",[fun],"snode25","hflux",0.0,P2_pin*H_fer,nlayers=3)
hslab24.add_layer(thk_elem=0.565E-3,thk_cros=H_fer,nnodes=2,darea=P2_clad*H_fer,solname='SS13', sollib="User")
hslab24.add_layer(thk_elem=0.115E-3,thk_cros=H_fer,nnodes=2,darea=P2_He*H_fer,  solname='gap13',sollib="User")
hslab24.add_layer(thk_elem=2.570E-3,thk_cros=H_fer,nnodes=3,darea=P2_pelt*H_fer,solname='MOX13',sollib="User",heat_input= 0.0048505*Pow_OC,AFF=[0.628,0.25,0.122])

#Upper gap
hslab25=HTcomp.HSlab("hslab25","pipe26","pipe",[fun],"snode26","hflux",0.0,P2_pin*H_gap,nlayers=1)
hslab25.add_layer(thk_elem=0.565E-3,thk_cros=H_gap,nnodes=2,darea=P2_clad*H_gap,solname='SS13',sollib="User")

#_____________________________________________________________________________________________
#CHANNEL 3 (Radial Blanket) (RB)

#nodes (data= table 3)
circuit1.add_node("node31", elevation= 1.)
circuit1.add_node("node32", elevation= 1.15)
circuit1.add_node("node33", elevation= 2.75)
circuit1.add_node("node34", elevation= 2.9)
circuit1.add_node("node35", elevation= 3.1)

#parameters for the pipes

#Inlet section
A3_In = 236.1E-4
D3_In  = 0.1651

#Pin bundle
A3_pin = 55.25E-4
D3_pin  = 0.004317

#Upper transition region
A3_UT = 236.1E-4
D3_UT  = 0.1651

#Outlet region
A3_OT = 0.003848
D3_OT  = 0.07

#Pipe 
circuit1.add_pipe("pipe31",D3_In, 1,       "node1", "node31",0.001,1,10,cfarea=A3_In, npar=225,Kforward=72500.)
circuit1.add_pipe("pipe32",D3_pin,0.15,    "node31","node32",0.001,1,2, cfarea=A3_pin,npar=225)
circuit1.add_pipe("pipe33",D3_pin,1.6,     "node32","node33",0.001,1,16,cfarea=A3_pin,npar=225)
circuit1.add_pipe("pipe34",D3_pin,0.15,    "node33","node34",0.001,1,2, cfarea=A3_pin,npar=225)
circuit1.add_pipe("pipe35",D3_UT, H_trans, "node34","node35",0.001,1,2, cfarea=A3_UT, npar=225)
circuit1.add_pipe("pipe36",D3_OT, H_outlet,"node35","node2", 0.001,1,5, cfarea=A3_OT, npar=225)

#Snodes
HTcomp.SNode("snode32")
HTcomp.SNode("snode33")
HTcomp.SNode("snode34")


#parameters for heatslab

P3_pin  = pi*15.8E-3*Pins_fer*SA_RB
P3_clad = pi*14.66E-3*Pins_fer*SA_RB
P3_He   = pi*14.36E-3*Pins_fer*SA_RB

#(Nu relation yet to be defined and some doubt in lower axial blanket)


#Lower gap
hslab31=HTcomp.HSlab("hslab31","pipe32","pipe",[fun],"snode32","hflux",0.0,P3_pin*0.15,nlayers=1)
hslab31.add_layer(thk_elem=1.14E-3,thk_cros=0.15,nnodes=2,darea=P3_clad*0.15,solname='SS13',sollib="User")

#fertile region
hslab32=HTcomp.HSlab("hslab32","pipe33","pipe",[fun],"snode33","hflux",0.0,P3_pin*1.6,nlayers=3)
hslab32.add_layer(thk_elem=1.14E-3,thk_cros=1.6,nnodes=2,darea=P3_clad*1.6,solname='SS13', sollib="User")
hslab32.add_layer(thk_elem=0.30E-3,thk_cros=1.6,nnodes=2,darea=P3_He*1.6,  solname='gap13',sollib="User")
hslab32.add_layer(thk_elem=7.18E-3,thk_cros=1.6,nnodes=6,darea=P3_He*1.6,  solname='MOX13',sollib="User",heat_input= Pow_RB,AFF=[0.01337,0.02021,0.0357,0.05966,0.08194,0.09845,0.10139,0.1122,0.1092,0.1005,0.08691,0.06946,0.04898,0.02862,0.01583,0.01038])

#Upper gap
hslab33=HTcomp.HSlab("hslab33","pipe34","pipe",[fun],"snode34","hflux",0.0,P3_pin*0.15,nlayers=1)
hslab33.add_layer(thk_elem=1.14E-3,thk_cros=0.15,nnodes=2,darea=P3_clad*0.15,solname='SS13',sollib="User")

#___________________________________________________________________________________________________________________________________________________
#Boundary condition SPX

circuit1.add_BC("bc1","node2",'P',1.5E5)
circuit1.add_BC("bc6","node1",'T',668)
circuit1.add_BC("bc7","node1",'P',6.E5)

