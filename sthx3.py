# PFBR IHX
# Heat addition by secondary sodium during primary system preheating

import math

#primary circuit (IHX shell)
circuit1 = comp.Circuit("circuit1")
circuit1.assign_fluid("Nitrogen","CoolProp")
node1 = circuit1.add_node("node1",elevation=7.5)
node2 = circuit1.add_node("node2")
Af = 0.25*math.pi*(1.831**2-0.57**2) - 3600*0.25*math.pi*0.019**2
Pw = math.pi*(1.831+0.57+3600*0.019)
dh = 4.*Af/(Pw)
pipe1=circuit1.add_pipe("pipe1",dh,7.5,"node2","node1",'DW',30.,20,cfarea=Af,npar=1)

circuit1.add_BC("bc1","node1",'P',1.E5)
circuit1.add_BC("bc2","node2",'T',150.+273.)
circuit1.add_BC("bc3","node2",'P',1.E5+0.8*9.81*7.5)

#secondary circuit (IHX tube)
circuit2 = comp.Circuit("circuit2")
circuit2.assign_fluid("Na6","User")
node3 = circuit2.add_node("node3")
node4 = circuit2.add_node("node4",elevation=7.5)
pipe2=circuit2.add_pipe("pipe2",0.0174,7.5,"node3","node4",'DW',30.,20,npar=3600)
circuit2.add_BC("bc4","node3",'P',5.E5)
circuit2.add_BC("bc5","node3",'T',170.+273.)
circuit2.add_BC("bc6","node4",'msource',-7.5)

Au = math.pi*0.019*7.5*3600
Ad = math.pi*0.0174*7.5*3600
def script1(flow_elem,WallTemp):
    Re = flow_elem.ther_gues.rhomass()*abs(flow_elem.velocity)*flow_elem.diameter/flow_elem.ther_gues.viscosity()
    Pr = flow_elem.ther_gues.viscosity()*flow_elem.ther_gues.cpmass()/flow_elem.ther_gues.conductivity()
    n = 0.43
    if Re < 2300.:
        Nu = 4.364
    elif Re > 5000.:
        Nu = 0.021*Re**0.8*Pr**n
    else:
        Nu1 = 4.364
        Nu2 = 0.023*5000.**0.8*Pr**n
        Nu = Nu1 + (Re-2300.)*(Nu2-Nu1)/(5000.-2300.)
    h = Nu * flow_elem.ther_gues.conductivity() / flow_elem.diameter
    return h

def script2(flow_elem,WallTemp):
    Re = flow_elem.ther_gues.rhomass()*abs(flow_elem.velocity)*flow_elem.diameter/flow_elem.ther_gues.viscosity()
    if Re > 2300.:
        Pe = flow_elem.ther_gues.rhomass()*flow_elem.velocity*flow_elem.diameter*flow_elem.ther_gues.cpmass()/flow_elem.ther_gues.conductivity()
        Nu = 4.82 + 0.0185*Pe**0.827
    else:
        Nu = 4.364
    h = Nu * flow_elem.ther_gues.conductivity() / flow_elem.diameter
    return h

hslab1 = HTcomp.HSlab("hslab1",dcomp="pipe1",dvar="pipe",dval=[script1],ucomp="pipe2",uvar="pipe",uval=[script2],uarea=Ad,config="parallel",nlayers=1)
layer1 = hslab1.add_layer(thk_elem=0.0016,thk_cros=7.5,nnodes=2,darea=Au,solname='SS6',sollib="User")

from PINET import solver_settings
solver_settings.conv_crit_ht = 1.E-7
solver_settings.conv_crit_flow = 1.E-7
solver_settings.conv_crit_temp_trans = 1.E-7
