circuit1=comp.Circuit("circuit1")
circuit1.assign_fluid("Na23","User")

circuit1.add_node("node1",elevation=0)
circuit1.add_node("node7",elevation=2.4519)

bc1=circuit1.add_BC("bc1","node1",'T',598.899)
bc2=circuit1.add_BC("bc2","node1",'P',100.E5)
global bc3
bc3=circuit1.add_BC("bc3","node7",'msource',-2191.7992)
#bc3=circuit1.add_BC("bc3","node7",'P',376464.8406894)

def fun2(flow_elem,WallTemp):
    Pe = flow_elem.ther_gues.rhomass()*flow_elem.velocity*flow_elem.diameter*flow_elem.ther_gues.cpmass()/flow_elem.ther_gues.conductivity()
    Nu = 5.0 + 0.025*Pe**0.8
    h = Nu * flow_elem.ther_gues.conductivity() / flow_elem.diameter
    return h

def fun1(flow_elem,WallTemp):
    Pe = flow_elem.ther_gues.rhomass()*flow_elem.velocity*flow_elem.diameter*flow_elem.ther_gues.cpmass()/flow_elem.ther_gues.conductivity()
    P = 0.00726    #Pin Pitch
    D = 0.005842   #Pin Diameter
    Nu = 4.0 + 0.16*(P/D)**5.0 + 0.33*(P/D)**3.8*(Pe/100)**0.86
            #13.066               #7.0961
    b = Nu * flow_elem.ther_gues.conductivity() / flow_elem.diameter
    return b

FA=0.00433
D=0.003238
E=[0.0000,0.9144,0.9347,1.0795,2.1719]#elevation  of nodes in channel
PDC=[9.7689,10.23113,9.77031,9.94184,11.84798,25.21945]#pressure drop coefficient
UN3FA=0.0052128
UN3D=0.07648207121336499
PF=[1,6,9,16,18,30]#no. of parallel flows in a channel
L=[0.0203,0.9144,0.0203,0.1448,1.0924,0.28]#length of pipe
FALAB=[0.0808,0.4851,0.7276,1.2936,1.4553,2.4254]
FALABI=[0.0703,0.4218,0.6327,1.1248,1.2654,2.1091]
GIFALAB=[0.066,0.399,0.598,1.063,1.196,1.993]
FAAC=[3.642,21.850,32.776,58.268,65.551,109.252]
FAACI=[3.167,19,28.5,50.668,65.551,95.002]
GIFAAC=[3.079,18.477,27.715,49.271,55.430,92.383]
FAUAB=[0.081,0.485,0.728,1.294,1.455,2.425]
FAUABI=[0.070,0.422,0.633,1.125,1.265,2.109]
GIFAUAB=[0.066,0.399,0.598,1.063,1.196,1.993]
FAUN1=[0.577,3.460,5.189,9.226,10.379,17.298]
FAUN2=[4.351,26.104,39.156,69.610,78.311,130.519]
FAUN3=[0.076336,0.458016,0.687024,1.221376,1.374048,2.29008]
global HIUAB
HIUAB=[14643,84355,121930,188410,176920,231170]
global HIAC
HIAC=[3316500,20275000,28279000,41711000,43479000,54461000]
global HILAB
HILAB=[9752.7,54413,70593,102010,88518,109640]
AFF=[[0.077776,0.078353,0.080316,0.081924,0.084594,0.08889,0.077776,0.078353,0.080316,0.081924],[0.093363,0.093682,0.094493,0.09595,0.098532,0.10169,0.093363,0.093682,0.094493,0.09595],[0.10873,0.108895,0.109211,0.110592,0.113178,0.115791,0.10873,0.108895,0.109211,0.110592],[0.118943,0.119016,0.119091,0.120322,0.122793,0.124753,0.118943,0.119016,0.119091,0.120322],[0.123089,0.123074,0.122948,0.123891,0.126394,0.126694,0.123089,0.123074,0.122948,0.123891],[0.120939,0.120839,0.120487,0.120782,0.122085,0.120845,0.120939,0.120839,0.120487,0.120782]]
global p
p=[]
i=0
while i<=5:
    j=0
    while j<=4:
        a=str(i+1)+str(j+1)
        circuit1.add_node("node"+a,elevation=E[j])
        j+=1
    k=0    
    while k<=5:
        b=str(i+1)+str(k+1)
        c=str(i+1)+str(k)
        if k==0:
            circuit1.add_pipe("pipe"+b,D,L[k],"node1","node"+b,0.03,1,1,cfarea=FA,npar=PF[i],Kforward=PDC[i])
        elif k==1:
            circuit1.add_pipe("pipe"+b,D,L[k],"node"+c,"node"+b,0.03,1,10,cfarea=FA,npar=PF[i])
        elif 1<k<5:
            circuit1.add_pipe("pipe"+b,D,L[k],"node"+c,"node"+b,0.03,1,1,cfarea=FA,npar=PF[i])
        else:
            circuit1.add_pipe("pipe"+b,UN3D,L[k],"node"+c,"node7",0.03,1,1,cfarea=UN3FA,npar=PF[i])
        HTcomp.SNode("snode"+b)
        k+=1
    l=0
    while l<=5:
        d=str(i+1)+str(l+1)
        if l==0:
            p.append(d+str(3))
            g=HTcomp.HSlab("hslab"+d,"pipe"+d,"pipe",[fun1],"snode"+d,"hflux",0.0,FALAB[i],nlayers=3)
            g.add_layer(3.81E-4,0.0203,2,FALABI[i],'SS23','User')
            g.add_layer(1.4E-4,0.0203,2,GIFALAB[i],'gap23','User')
            p[i*3+l]=g.add_layer(0.0024,0.0203,2,GIFALAB[i],'MOX23','User',heat_input=HILAB[i])
        elif l==1:
            p.append(d+str(3))
            g=HTcomp.HSlab("hslab"+d,"pipe"+d,"pipe",[fun1],"snode"+d,"hflux",0.0,FAAC[i],nlayers=3)
            g.add_layer(3.81E-4,0.9144,2,FAACI[i],'SS23','User')
            g.add_layer(7.E-5,0.9144,2,GIFAAC[i],'gap23','User')
            p[i*3+l]=g.add_layer(0.00247,0.9144,2,GIFAAC[i],'MOX23','User',10,heat_input=HIAC[i],AFF=AFF[i])
        elif l==2:
            p.append(d+str(3))
            g=HTcomp.HSlab("hslab"+d,"pipe"+d,"pipe",[fun1],"snode"+d,"hflux",0.0,FAUAB[i],nlayers=3)
            g.add_layer(3.81E-4,0.0203,2,FAUABI[i],'SS23','User')
            g.add_layer(1.4E-4,0.0203,2,GIFAUAB[i],'gap23','User')
            p[i*3+l]=g.add_layer(0.0024,0.0203,2,GIFAUAB[i],'MOX23','User',heat_input=HIUAB[i])
        elif l==3:
            g=HTcomp.HSlab("hslab"+d,"pipe"+d,"pipe",[fun1],"snode"+d,"hflux",0.0,FAUN1[i],nlayers=1)
            g.add_layer(0.0018497,0.1448,2,FAUN1[i],'SS23','User')
        elif l==4:
            g=HTcomp.HSlab("hslab"+d,"pipe"+d,"pipe",[fun1],"snode"+d,"hflux",0.0,FAUN2[i],nlayers=1)
            g.add_layer(8.625E-4,1.0924,2,FAUN2[i],'SS23','User')
        else:
            g=HTcomp.HSlab("hslab"+d,"pipe"+d,"pipe",[fun2],"snode"+d,"hflux",0.0,FAUN3[i],nlayers=1)
            g.add_layer(0.027,0.28,2,FAUN3[i],'SS23','User')
        l+=1
    i+=1
global pipe7
pipe7=circuit1.add_pipe("pipe7",0.003238,2.4722,"node1","node7",0.03,1,1,cfarea=0.12982,Kforward=147.6114,heat_input=7113740.)

global series1
series1=csv_reader("power.csv")
def power_trans(time,delt):
    m=0
    while m<=5:
        n=0
        while n<=2:
            if n==0:
                p[m*3+n].heat_input = series1(time)*HILAB[m]
            elif n==1:
                p[m*3+n].heat_input = series1(time)*HIAC[m]
            else:
                p[m*3+n].heat_input = series1(time)*HIUAB[m]
            n+=1
        m+=1
    pipe7.heat_input = series1(time) * 7113740.
action_setup.Action(None,None,power_trans)
global series2
series2=csv_reader("msource.csv")
def mdot(time,delt):
    y=series2(time)
    return y
action_setup.Action("bc3","bval",mdot)
from PINET import solver_settings
solver_settings.conv_crit_ht = 1.E-7
solver_settings.conv_crit_flow = 1.E-7
solver_settings.conv_crit_temp_trans = 1.E-7

from PINET import scheduler
scheduler.delt = 1.
scheduler.etime = 900    
