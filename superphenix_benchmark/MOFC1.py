
# SPX benchmark test

circuit1=comp.Circuit("circuit1")
circuit1.assign_fluid("Na6","User")
    
circuit1.add_node("node0", elevation= -0.2)
circuit1.add_node("node1", elevation= 0.0)
circuit1.add_node("node2", elevation= 4.3)
circuit1.add_node("node3", elevation= 4.5)

circuit1.add_pipe("pipe1", 3.157, 0.2, "node0", "node1", 0.001, 1, 1,  cfarea=7.83)
circuit1.add_pipe("pipe2", 3.518, 0.2, "node2", "node3", 0.001, 1, 1,  cfarea=9.72)

#nominal power inputs
global total_power_frac
global Pow_IC
global Pow_OC
global Pow_RB
total_power_frac=0.2314
Total_power=29.8988E8*total_power_frac
Pow_IC = 0.5854*Total_power
Pow_OC = 0.4039*Total_power
Pow_RB = 0.0107*Total_power

def fun1(flow_elem,WallTemp):
    Pe = flow_elem.ther_gues.rhomass()*flow_elem.velocity*flow_elem.diameter*flow_elem.ther_gues.cpmass()/flow_elem.ther_gues.conductivity()
    Nu = 5.0 + 0.025*Pe**0.8
    h = Nu * flow_elem.ther_gues.conductivity() / flow_elem.diameter
    return h

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

global p
p=[]

EF =[0.2,0.75,1.05,2.05,2.35,2.9,3.1] #elevation of nodes in fuel channel
EB =[1.,1.15,2.75,2.9,3.1] #elevation of nodes in blanket channels

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
PF = [SA_IC,SA_OC,SA_RB]
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

DB = [D3_In,D3_pin,D3_pin,D3_pin,D3_UT,D3_OT]
LB = [1,0.15,1.6,0.15,H_trans,H_outlet]
NINCB = [10,2,16,2,2,5]
FAB = [A3_In,A3_pin,A3_pin,A3_pin,A3_UT,A3_OT]

#parameters for heatslab
P1_pin  = math.pi*8.5E-3*Pins_fis*SA_IC
P1_clad = math.pi*7.37E-3*Pins_fis*SA_IC
P1_He   = math.pi*7.14E-3*Pins_fis*SA_IC
P1_pelt = math.pi*2E-3*Pins_fis*SA_IC
P2_pin  = math.pi*8.50E-3*Pins_fis*SA_OC
P2_clad = math.pi*7.37E-3*Pins_fis*SA_OC
P2_He   = math.pi*7.14E-3*Pins_fis*SA_OC
P2_pelt = math.pi*2.00E-3*Pins_fis*SA_OC

GIFALABI = [P1_pelt*H_fer,P2_pelt*H_fer]
GIFALAB  = [P1_He*H_fer  ,P2_He*H_fer  ]
FALABI   = [P1_clad*H_fer,P2_clad*H_fer]
FALAB    = [P1_pin*H_fer ,P2_pin*H_fer ]
HILAB    = [8.938E-3*Pow_IC,0.007422*Pow_OC]
AFFLAB   = [[0.151,0.264,0.585],
          [0.141,0.257,0.602]]
GIFAACI = [P1_pelt*H_fis,P2_pelt*H_fis]
GIFAAC  = [P1_He*H_fis  ,P2_He*H_fis  ]
FAACI   = [P1_clad*H_fis,P2_clad*H_fis]
FAAC    = [P1_pin*H_fis ,P2_pin*H_fis ]
HIAC    = [0.98542*Pow_IC,0.98976*Pow_OC]
AFF     = [[0.0787,0.1,0.118,0.128,0.129,0.122,0.108,0.091,0.072,0.0533],
           [0.077,0.099,0.117,0.127,0.129,0.122,0.108,0.09,0.073,0.058]]
GIFAUABI = GIFALABI
GIFAUAB  = GIFALAB
FAUABI   = FALABI
FAUAB    = FALAB
HIUAB    = [5.6213E-3*Pow_IC,0.0048505*Pow_OC]
AFFUAB   = [[0.616,0.257,0.127],
          [0.628,0.25,0.122]]
P3_pin   = math.pi*15.8E-3*Pins_fer*SA_RB
P3_clad  = math.pi*14.66E-3*Pins_fer*SA_RB
P3_He    = math.pi*14.36E-3*Pins_fer*SA_RB

GIFAACIB = [P3_He*1.6]
GIFAACB  = [P3_He*1.6]
FAACIB   = [P3_clad*1.6]
FAACB    = [P3_pin*1.6]
HIACB    = [Pow_RB]
AFFB     = [[0.01337,0.02021,0.0357,0.05966,0.08194,0.09845,0.10139,0.1122,0.1092,0.1005,0.08691,0.06946,0.04898,0.02862,0.01583,0.01038]]

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

    for k in range(2,5):
        d=str(i+1)+str(k+1)
        HTcomp.SNode("snode"+d)
        
        if k==2: #Lower fertile region
            g=HTcomp.HSlab("hslab"+d,"snode"+d,"hflux",0.0,"pipe"+d,"pipe",[fun1],GIFALABI[i],nlayers=3)
            p.append(g.add_layer(2.570E-3, H_fer, 2,GIFALAB[i],'MOX13','User',heat_input= HILAB[i],AFF=AFFLAB[i]))
            g.add_layer         (0.115E-3, H_fer, 2,FALABI[i], 'gap13','User')
            g.add_layer         (0.565E-3, H_fer, 2,FALAB[i],  'SS13', 'User')

        elif k==3: #fissile region
            g=HTcomp.HSlab("hslab"+d,"snode"+d,"hflux",0.0,"pipe"+d,"pipe",[fun1],GIFAACI[i],nlayers=3)
            p.append(g.add_layer(2.570E-3, H_fis, 2, GIFAAC[i], 'MOX13', 'User',heat_input=HIAC[i],AFF=AFF[i]))
            g.add_layer         (0.115E-3, H_fis, 2, FAACI[i],  'gap13', 'User')
            g.add_layer         (0.565E-3, H_fis, 2, FAAC[i],   'SS13',  'User')

        elif k==4: #Upper fertile region
            g=HTcomp.HSlab("hslab"+d,"snode"+d,"hflux",0.0,"pipe"+d,"pipe",[fun1],GIFAUABI[i],nlayers=3)
            p.append(g.add_layer(2.570E-3, H_fer, 2, GIFAUAB[i],'MOX13','User',heat_input=HIUAB[i],AFF=AFFUAB[i]))
            g.add_layer         (0.115E-3, H_fer, 2, FAUABI[i], 'gap13','User')
            g.add_layer         (0.565E-3, H_fer, 2, FAUAB[i],  'SS13', 'User')

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

    for k in range(2,3):
        d=str(i+1)+str(k+1)
        HTcomp.SNode("snode"+d)

        if k==2: #fertile region
            g=HTcomp.HSlab("hslab"+d,"snode"+d,"hflux",0.0,"pipe"+d,"pipe",[fun1],GIFAACIB[i-2],nlayers=3)
            p.append(g.add_layer(7.18E-3, 1.6, 2, GIFAACB[i-2], 'MOX13', 'User',heat_input=HIACB[i-2],AFF=AFFB[i-2]))
            g.add_layer         (0.30E-3, 1.6, 2, FAACIB[i-2],  'gap13', 'User')
            g.add_layer         (1.14E-3, 1.6, 2, FAACB[i-2],   'SS13',  'User')

#__________________________________________________________________________________________________________________________________________________
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
    p[0].heat_input = 8.938E-3*Pow_IC
    p[1].heat_input = 0.98542*Pow_IC
    p[2].heat_input = 5.6213E-3*Pow_IC
    p[3].heat_input = 0.007422*Pow_OC
    p[4].heat_input = 0.98976*Pow_OC
    p[5].heat_input = 0.0048505*Pow_OC
    p[6].heat_input = Pow_RB
    
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

