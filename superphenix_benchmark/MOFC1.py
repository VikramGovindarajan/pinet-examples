
# SPX benchmark test

circuit1=comp.Circuit("circuit1")
circuit1.assign_fluid("Na6","User")
    
circuit1.add_node("node0", elevation= -0.2)
circuit1.add_node("node1", elevation= 0.0)
circuit1.add_node("node2", elevation= 4.3)
circuit1.add_node("node3", elevation= 4.5)

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

global total_power_frac
global Total_power
global Pow_IC
global Pow_OC
global Pow_RB
total_power_frac=0.2314
Total_power=29.8988E8*total_power_frac
Pow_IC = 0.5854*Total_power
Pow_OC = 0.4039*Total_power
Pow_RB = 0.0107*Total_power

#preliminary calculations

def fun(flow_elem,WallTemp):
    Pe = flow_elem.ther_gues.rhomass()*flow_elem.velocity*flow_elem.diameter*flow_elem.ther_gues.cpmass()/flow_elem.ther_gues.conductivity()
    Nu = 5.0 + 0.025*Pe**0.8
    h = Nu * flow_elem.ther_gues.conductivity() / flow_elem.diameter
    return h
    
circuit1.add_pipe("pipe1", 3.157, 0.2, "node0", "node1", 0.001, 1, 1,  cfarea=7.83)
circuit1.add_pipe("pipe2", 3.518, 0.2, "node2", "node3", 0.001, 1, 1,  cfarea=9.72)

EF =[0.2,0.75,1.05,2.05,2.35,2.9,3.1] #elevation of nodes in fuel channel
EB =[1.,1.15,2.75,2.9,3.1] #elevation of nodes in blanket channels
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


DF = [D1_In,D1_pin,D1_pin,D1_pin,D1_pin,D1_pin,D1_UT,D1_OT]
LF = [H_inlet,H_gap,H_fer,H_fis,H_fer,H_gap,H_trans,H_outlet]
NINCF = [2,5,3,10,3,5,2,12]
FAF = [A1_In,A1_pin,A1_pin,A1_pin,A1_pin,A1_pin,A1_UT,A1_OT]
PF = [SA_IC,SA_OC,225]
PDC = [156,260,72500]

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

DB = [D3_In,D3_pin,D3_pin,D3_pin,D3_UT,D3_OT]
LB = [1,0.15,1.6,0.15,H_trans,H_outlet]
NINCB = [10,2,16,2,2,5]
FAB = [A3_In,A3_pin,A3_pin,A3_pin,A3_UT,A3_OT]


for i in range(2): #fuel channels
    #nodes (data= table 3)
    for j in range(7):
        a=str(i+1)+str(j+1)
        circuit1.add_node("node"+a,elevation=EF[j])

    #Pipes
    for k in range(8):
        b=str(i+1)+str(k+1)
        c=str(i+1)+str(k)
        if k==0:    circuit1.add_pipe("pipe"+b,DF[k],LF[k],"node1", "node"+b,0.001,1,NINCF[k],cfarea=FAF[k],npar=PF[i],Kforward=PDC[i])
        elif k==1:  circuit1.add_pipe("pipe"+b,DF[k],LF[k],"node"+c,"node"+b,0.001,1,NINCF[k],cfarea=FAF[k],npar=PF[i])
        elif 1<k<7: circuit1.add_pipe("pipe"+b,DF[k],LF[k],"node"+c,"node"+b,0.001,1,NINCF[k],cfarea=FAF[k],npar=PF[i])
        else:       circuit1.add_pipe("pipe"+b,DF[k],LF[k],"node"+c,"node2", 0.001,1,NINCF[k],cfarea=FAF[k],npar=PF[i])

for i in range(2,3): #blanket channels
    for j in range(5):
        a=str(i+1)+str(j+1)
        circuit1.add_node("node"+a,elevation=EB[j])

    for k in range(6):
        b=str(i+1)+str(k+1)
        c=str(i+1)+str(k)
        if k==0:    circuit1.add_pipe("pipe"+b,DB[k],LB[k],"node1", "node"+b,0.001,1,NINCB[k],cfarea=FAF[k],npar=PF[i],Kforward=PDC[i])
        elif k==1:  circuit1.add_pipe("pipe"+b,DB[k],LB[k],"node"+c,"node"+b,0.001,1,NINCB[k],cfarea=FAF[k],npar=PF[i])
        elif 1<k<5: circuit1.add_pipe("pipe"+b,DB[k],LB[k],"node"+c,"node"+b,0.001,1,NINCB[k],cfarea=FAF[k],npar=PF[i])
        else:       circuit1.add_pipe("pipe"+b,DB[k],LB[k],"node"+c,"node2", 0.001,1,NINCB[k],cfarea=FAF[k],npar=PF[i])


#_____________________________________________________________________________________________
#CHANNEL 1 (inner core) (IC)

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


##Lower gap()
#hslab11=HTcomp.HSlab("hslab11","pipe12","pipe",[fun],"snode12","hflux",0.0,P1_pin*H_gap,nlayers=1)
#hslab11.add_layer(thk_elem=0.565E-3,thk_cros=H_gap,nnodes=2,darea=P1_clad*H_gap,solname='SS13',sollib="User")

global layer123
global layer133
global layer143
#Lower fertile region
hslab12=HTcomp.HSlab("hslab12","pipe13","pipe",[fun],"snode13","hflux",0.0,P1_pin*H_fer,nlayers=3)
hslab12.add_layer(thk_elem=0.565E-3,thk_cros=H_fer,nnodes=2,darea=P1_clad*H_fer,solname='SS13',  sollib="User")
hslab12.add_layer(thk_elem=0.115E-3,thk_cros=H_fer,nnodes=2,darea=P1_He*H_fer,  solname='gap13', sollib="User")
layer123 = hslab12.add_layer(thk_elem=2.570E-3,thk_cros=H_fer,nnodes=3,darea=P1_pelt*H_fer,solname='MOX13', sollib="User",heat_input= 8.938E-3*Pow_IC,AFF=[0.151,0.264,0.585])

#fissile region
hslab13=HTcomp.HSlab("hslab13","pipe14","pipe",[fun],"snode14","hflux",0.0,P1_pin*H_fis,nlayers=3)
hslab13.add_layer(thk_elem=0.565E-3,thk_cros=H_fis,nnodes=2,darea=P1_clad*H_fis,solname='SS13', sollib="User")
hslab13.add_layer(thk_elem=0.115E-3,thk_cros=H_fis,nnodes=2,darea=P1_He*H_fis,  solname='gap13',sollib="User")
layer133 = hslab13.add_layer(thk_elem=2.570E-3,thk_cros=H_fis,nnodes=3,darea=P1_pelt*H_fis,solname='MOX13',sollib="User",heat_input= 0.98542*Pow_IC,AFF=[0.0787,0.1,0.118,0.128,0.129,0.122,0.108,0.091,0.072,0.0533])

#Upper fertile region
hslab14=HTcomp.HSlab("hslab14","pipe15","pipe",[fun],"snode15","hflux",0.0,P1_pin*H_fer,nlayers=3)
hslab14.add_layer(thk_elem=0.565E-3,thk_cros=H_fer,nnodes=2,darea=P1_clad*H_fer,solname='SS13',sollib="User")
hslab14.add_layer(thk_elem=0.115E-3,thk_cros=H_fer,nnodes=2,darea=P1_He*H_fer,  solname='gap13',sollib="User")
layer143 = hslab14.add_layer(thk_elem=2.570E-3,thk_cros=H_fer,nnodes=3,darea=P1_pelt*H_fer,solname='MOX13',sollib="User",heat_input= 5.6213E-3*Pow_IC,AFF=[0.616,0.257,0.127])

##Upper gap
#hslab15=HTcomp.HSlab("hslab15","pipe16","pipe",[fun],"snode16","hflux",0.0,P1_pin*H_gap,nlayers=1)
#hslab15.add_layer(thk_elem=0.565E-3,thk_cros=H_gap,nnodes=2,darea=P1_clad*H_gap,solname='SS13',sollib="User")

#___________________________________________________________________________________________________________________________________________________

#CHANNEL 2 (outer core) (OC)

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


#Snodes
HTcomp.SNode("snode22")
HTcomp.SNode("snode23")
HTcomp.SNode("snode24")
HTcomp.SNode("snode25")
HTcomp.SNode("snode26")

#parameters for heatslab


P2_pin  = pi*8.50E-3*Pins_fis*SA_OC
P2_clad = pi*7.37E-3*Pins_fis*SA_OC
P2_He   = pi*7.14E-3*Pins_fis*SA_OC
P2_pelt = pi*2.00E-3*Pins_fis*SA_OC


##Lower gap
#hslab21=HTcomp.HSlab("hslab21","pipe22","pipe",[fun],"snode22","hflux",0.0,P2_pin*H_gap,nlayers=1)
#hslab21.add_layer(thk_elem=0.565E-3,thk_cros=H_gap,nnodes=2,darea=P2_clad*H_gap,solname='SS13',sollib="User")

global layer223
global layer233
global layer243
#Lower fertile region
hslab22=HTcomp.HSlab("hslab22","pipe23","pipe",[fun],"snode23","hflux",0.0,P2_pin*H_fer,nlayers=3)
hslab22.add_layer(thk_elem=0.565E-3,thk_cros=H_fer,nnodes=2,darea=P2_clad*H_fer,solname='SS13', sollib="User")
hslab22.add_layer(thk_elem=0.115E-3,thk_cros=H_fer,nnodes=2,darea=P2_He*H_fer,  solname='gap13',sollib="User")
layer223 = hslab22.add_layer(thk_elem=2.570E-3,thk_cros=H_fer,nnodes=3,darea=P2_pelt*H_fer,solname='MOX13',sollib="User",heat_input= 0.007422*Pow_OC,AFF=[0.141,0.257,0.602])

#fissile region
hslab23=HTcomp.HSlab("hslab23","pipe24","pipe",[fun],"snode24","hflux",0.0,P2_pin*H_fis,nlayers=3)
hslab23.add_layer(thk_elem=0.565E-3,thk_cros=H_fis,nnodes=2,darea=P2_clad*H_fis,solname='SS13', sollib="User")
hslab23.add_layer(thk_elem=0.115E-3,thk_cros=H_fis,nnodes=2,darea=P2_He*H_fis,  solname='gap13',sollib="User")
layer233 = hslab23.add_layer(thk_elem=2.570E-3,thk_cros=H_fis,nnodes=3,darea=P2_pelt*H_fis,solname='MOX13',sollib="User",heat_input= 0.98976*Pow_OC,AFF=[0.077,0.099,0.117,0.127,0.129,0.122,0.108,0.09,0.073,0.058])


#Upper fertile region
hslab24=HTcomp.HSlab("hslab24","pipe25","pipe",[fun],"snode25","hflux",0.0,P2_pin*H_fer,nlayers=3)
hslab24.add_layer(thk_elem=0.565E-3,thk_cros=H_fer,nnodes=2,darea=P2_clad*H_fer,solname='SS13', sollib="User")
hslab24.add_layer(thk_elem=0.115E-3,thk_cros=H_fer,nnodes=2,darea=P2_He*H_fer,  solname='gap13',sollib="User")
layer243 = hslab24.add_layer(thk_elem=2.570E-3,thk_cros=H_fer,nnodes=3,darea=P2_pelt*H_fer,solname='MOX13',sollib="User",heat_input= 0.0048505*Pow_OC,AFF=[0.628,0.25,0.122])

##Upper gap
#hslab25=HTcomp.HSlab("hslab25","pipe26","pipe",[fun],"snode26","hflux",0.0,P2_pin*H_gap,nlayers=1)
#hslab25.add_layer(thk_elem=0.565E-3,thk_cros=H_gap,nnodes=2,darea=P2_clad*H_gap,solname='SS13',sollib="User")

#_____________________________________________________________________________________________
#CHANNEL 3 (Radial Blanket) (RB)


#Snodes
HTcomp.SNode("snode32")
HTcomp.SNode("snode33")
HTcomp.SNode("snode34")


#parameters for heatslab

P3_pin  = pi*15.8E-3*Pins_fer*SA_RB
P3_clad = pi*14.66E-3*Pins_fer*SA_RB
P3_He   = pi*14.36E-3*Pins_fer*SA_RB

#(Nu relation yet to be defined and some doubt in lower axial blanket)

global layer323

##Lower gap
#hslab31=HTcomp.HSlab("hslab31","pipe32","pipe",[fun],"snode32","hflux",0.0,P3_pin*0.15,nlayers=1)
#hslab31.add_layer(thk_elem=1.14E-3,thk_cros=0.15,nnodes=2,darea=P3_clad*0.15,solname='SS13',sollib="User")

#fertile region
hslab32=HTcomp.HSlab("hslab32","pipe33","pipe",[fun],"snode33","hflux",0.0,P3_pin*1.6,nlayers=3)
hslab32.add_layer(thk_elem=1.14E-3,thk_cros=1.6,nnodes=2,darea=P3_clad*1.6,solname='SS13', sollib="User")
hslab32.add_layer(thk_elem=0.30E-3,thk_cros=1.6,nnodes=2,darea=P3_He*1.6,  solname='gap13',sollib="User")
layer323 = hslab32.add_layer(thk_elem=7.18E-3,thk_cros=1.6,nnodes=6,darea=P3_He*1.6,  solname='MOX13',sollib="User",heat_input= Pow_RB,AFF=[0.01337,0.02021,0.0357,0.05966,0.08194,0.09845,0.10139,0.1122,0.1092,0.1005,0.08691,0.06946,0.04898,0.02862,0.01583,0.01038])

##Upper gap
#hslab33=HTcomp.HSlab("hslab33","pipe34","pipe",[fun],"snode34","hflux",0.0,P3_pin*0.15,nlayers=1)
#hslab33.add_layer(thk_elem=1.14E-3,thk_cros=0.15,nnodes=2,darea=P3_clad*0.15,solname='SS13',sollib="User")

#___________________________________________________________________________________________________________________________________________________
#Boundary condition MOFC1

circuit1.add_BC("bc1","node3",'P',1.5E5)
circuit1.add_BC("bc2","node0",'msource',6300.)
circuit1.add_BC("bc3","node0",'T',662.2)

# series1 for temp vs time
global series1
series1 = csv_reader("temp_MOFC1_400.csv")
def fun2(time,delt):
    y = series1(time)
    return y

# series2 for power vs time
global series2
series2 = csv_reader("power_MOFC1_400.csv")
def fun3(time,delt):
    total_power_frac = series2(time)
    Total_power=29.8988E8*total_power_frac
    Pow_IC = 0.5854*Total_power
    Pow_OC = 0.4039*Total_power
    Pow_RB = 0.0107*Total_power
    layer123.heat_input = 8.938E-3*Pow_IC
    layer133.heat_input = 0.98542*Pow_IC
    layer143.heat_input = 5.6213E-3*Pow_IC
    layer223.heat_input = 0.007422*Pow_OC
    layer233.heat_input = 0.98976*Pow_OC
    layer243.heat_input = 0.0048505*Pow_OC
    layer323.heat_input = Pow_RB
    
from PINET import solver_settings
solver_settings.conv_crit_ht = 1.E-7
solver_settings.conv_crit_flow = 1.E-7
solver_settings.conv_crit_temp_trans = 1.E-7

action_setup.Action("bc3","bval",fun2)    
action_setup.Action(None,None,fun3)  

from PINET import scheduler
scheduler.delt = 10
scheduler.etime = 2210

def fun4(*comps):
    return comps[1].ttemp_gues-comps[0].ttemp_gues
post.Calculate(fun4,"node1","node2")

