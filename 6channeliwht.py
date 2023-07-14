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

FAp=0.00433
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
FA=[FALAB,FAAC,FAUAB,FAUN1,FAUN2]
IWFALAB=[0.008171999999999999, 0.024516, 0.036774, 0.06537599999999999, 0.073548, 0.12258]
IWFAAC=[0.368136, 1.104408, 1.656612, 2.945088, 3.313224, 5.5220400000000005]
IWFAUAB=[0.008171999999999999, 0.024516, 0.036774, 0.06537599999999999, 0.073548, 0.12258]
IWFAUN1=[0.05829648, 0.17488944, 0.26233416, 0.46637184, 0.52466832, 0.8744472]
IWFAUN2=[0.4398, 1.3194000000000001, 1.9791, 3.5184, 3.9582, 6.597]
IWFAUN3=[0.112728, 0.338184, 0.507276, 0.901824, 1.014552, 1.69092]
IWFA=[IWFALAB,IWFAAC,IWFAUAB,IWFAUN1,IWFAUN2]
global HIUAB
HIUAB=[14643,84355,121930,188410,176920,231170]
global HIAC
HIAC=[3316500,20275000,28279000,41711000,43479000,54461000]
global HILAB
HILAB=[9752.7,54413,70593,102010,88518,109640]
AFF=[[0.077776,0.078353,0.080316,0.081924,0.084594,0.08889,0.077776,0.078353,0.080316,0.081924],[0.093363,0.093682,0.094493,0.09595,0.098532,0.10169,0.093363,0.093682,0.094493,0.09595],[0.10873,0.108895,0.109211,0.110592,0.113178,0.115791,0.10873,0.108895,0.109211,0.110592],[0.118943,0.119016,0.119091,0.120322,0.122793,0.124753,0.118943,0.119016,0.119091,0.120322],[0.123089,0.123074,0.122948,0.123891,0.126394,0.126694,0.123089,0.123074,0.122948,0.123891],[0.120939,0.120839,0.120487,0.120782,0.122085,0.120845,0.120939,0.120839,0.120487,0.120782]]
global f
f=[]
i=0 
while i<=5:# no. of radial zones
    j=0 #pin pipe nodes
    while j<=4:
        a=str(i+1)+str(j+1)
        circuit1.add_node("node"+a,elevation=E[j])
        j+=1
    k=0 #pin piping    
    while k<=5:
        b=str(i+1)+str(k+1)
        b1=str(i+1)+str(k)
        if k==0:
            circuit1.add_pipe("pipe"+b,D,L[k],"node1","node"+b,0.03,1,1,cfarea=FAp,npar=PF[i],Kforward=PDC[i])
        elif k==1:
            circuit1.add_pipe("pipe"+b,D,L[k],"node"+b1,"node"+b,0.03,1,10,cfarea=FAp,npar=PF[i])
        elif 1<k<5:
            circuit1.add_pipe("pipe"+b,D,L[k],"node"+b1,"node"+b,0.03,1,1,cfarea=FAp,npar=PF[i])
        else:
            circuit1.add_pipe("pipe"+b,UN3D,L[k],"node"+b1,"node7",0.03,1,1,cfarea=UN3FA,npar=PF[i])
        HTcomp.SNode("snode"+b)
        k+=1
    l=0 #pin heat layers
    while l<=4:
        c=str(i+1)+str(l+1)
        if l==0:
            f.append(c+str(3))
            g=HTcomp.HSlab("hslab"+c,"pipe"+c,"pipe",[fun1],"snode"+c,"hflux",0.0,FALAB[i],nlayers=3)
            g.add_layer(3.81E-4,L[l],2,FALABI[i],'SS23','User')
            g.add_layer(1.4E-4,L[l],2,GIFALAB[i],'gap23','User')
            f[i*3+l]=g.add_layer(0.0024,L[l],2,GIFALAB[i],'MOX23','User',heat_input=HILAB[i])
        elif l==1:
            f.append(c+str(3))
            g=HTcomp.HSlab("hslab"+c,"pipe"+c,"pipe",[fun1],"snode"+c,"hflux",0.0,FAAC[i],nlayers=3)
            g.add_layer(3.81E-4,L[l],2,FAACI[i],'SS23','User')
            g.add_layer(7.E-5,L[l],2,GIFAAC[i],'gap23','User')
            f[i*3+l]=g.add_layer(0.00247,L[l],2,GIFAAC[i],'MOX23','User',10,heat_input=HIAC[i],AFF=AFF[i])
        elif l==2:
            f.append(c+str(3))
            g=HTcomp.HSlab("hslab"+c,"pipe"+c,"pipe",[fun1],"snode"+c,"hflux",0.0,FAUAB[i],nlayers=3)
            g.add_layer(3.81E-4,L[l],2,FAUABI[i],'SS23','User')
            g.add_layer(1.4E-4,L[l],2,GIFAUAB[i],'gap23','User')
            f[i*3+l]=g.add_layer(0.0024,L[l],2,GIFAUAB[i],'MOX23','User',heat_input=HIUAB[i])
        elif l==3:
            g=HTcomp.HSlab("hslab"+c,"pipe"+c,"pipe",[fun1],"snode"+c,"hflux",0.0,FAUN1[i],nlayers=1)
            g.add_layer(0.0018497,L[l],2,FAUN1[i],'SS23','User')
        else:
            g=HTcomp.HSlab("hslab"+c,"pipe"+c,"pipe",[fun1],"snode"+c,"hflux",0.0,FAUN2[i],nlayers=1)
            g.add_layer(8.625E-4,L[l],2,FAUN2[i],'SS23','User')
        l+=1
    o=0
    while (o<=5) and (i>=1):
        i1=i-1
        d=str(i)+str(o+1)
        d1=str(i+1)+str(o+1)
        if o<=4:
            h=HTcomp.HSlab("hslabIW"+d,"pipe"+d,"pipe",[fun1],"pipe"+d1,"pipe",[fun1],IWFA[o][i1],config="parallel",nlayers=3)
            h.add_layer(3.05E-3,L[o],2,IWFA[o][i1],'SS23','User')
            h.add_layer(6.4E-4,L[o],2,IWFA[o][i],'gapSA','User')
            h.add_layer(3.05E-3,L[o],2,IWFA[o][i],'SS23','User')
        else:
            h=HTcomp.HSlab("hslabIW"+d,"pipe"+d,"pipe",[fun2],"pipe"+d1,"pipe",[fun2],IWFAUN3[i1],config="parallel",nlayers=3)
            h.add_layer(0.27,L[o],2,IWFAUN3[i1],'SS23','User')
            h.add_layer(6.4E-4,L[o],2,IWFAUN3[i],'gapSA','User')
            h.add_layer(0.27,L[o],2,IWFAUN3[i],'SS23','User')
        o+=1
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
                f[m*3+n].heat_input = series1(time)*HILAB[m]
            elif n==1:
                f[m*3+n].heat_input = series1(time)*HIAC[m]
            else:
                f[m*3+n].heat_input = series1(time)*HIUAB[m]
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


