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
            g=HTcomp.HSlab("hslab"+d,"snode"+d,"hflux",0.0,"pipe"+d,"pipe",[fun1],FALAB[i],nlayers=3)
            g.add_layer(3.81E-4,0.0203,2,FALABI[i],'SS23','User')
            g.add_layer(1.4E-4,0.0203,2,GIFALAB[i],'gap23','User')
            p[i*3+l]=g.add_layer(0.0024,0.0203,2,GIFALAB[i],'MOX23','User',heat_input=HILAB[i])
        elif l==1:
            p.append(d+str(3))
            g=HTcomp.HSlab("hslab"+d,"snode"+d,"hflux",0.0,"pipe"+d,"pipe",[fun1],FAAC[i],nlayers=3)
            g.add_layer(3.81E-4,0.9144,2,FAACI[i],'SS23','User')
            g.add_layer(7.E-5,0.9144,2,GIFAAC[i],'gap23','User')
            p[i*3+l]=g.add_layer(0.00247,0.9144,2,GIFAAC[i],'MOX23','User',10,heat_input=HIAC[i],AFF=AFF[i])
        elif l==2:
            p.append(d+str(3))
            g=HTcomp.HSlab("hslab"+d,"snode"+d,"hflux",0.0,"pipe"+d,"pipe",[fun1],FAUAB[i],nlayers=3)
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


def pk1(time,delt):

    # reading components
    from PINET.project import get_comp
    # radial zone1
    DHSNZ1LAB = get_comp("hslab11")
    DHSNZ1AC  = get_comp("hslab12")
    DHSNZ1UAB = get_comp("hslab13")
    PipeNZ1LAB = get_comp("pipe11")
    PipeNZ1AC  = get_comp("pipe12")
    PipeNZ1UAB = get_comp("pipe13")

    DHSNZ2LAB = get_comp("hslab21")
    DHSNZ2AC  = get_comp("hslab22")
    DHSNZ2UAB = get_comp("hslab23")
    PipeNZ2LAB = get_comp("pipe21")
    PipeNZ2AC  = get_comp("pipe22")
    PipeNZ2UAB = get_comp("pipe23")
    DHSNZ3LAB = get_comp("hslab31")
    DHSNZ3AC  = get_comp("hslab32")
    DHSNZ3UAB = get_comp("hslab33")
    PipeNZ3LAB = get_comp("pipe31")
    PipeNZ3AC  = get_comp("pipe32")
    PipeNZ3UAB = get_comp("pipe33")
    DHSNZ4LAB = get_comp("hslab41")
    DHSNZ4AC  = get_comp("hslab42")
    DHSNZ4UAB = get_comp("hslab43")
    PipeNZ4LAB = get_comp("pipe41")
    PipeNZ4AC  = get_comp("pipe42")
    PipeNZ4UAB = get_comp("pipe43")
    DHSNZ5LAB = get_comp("hslab51")
    DHSNZ5AC  = get_comp("hslab52")
    DHSNZ5UAB = get_comp("hslab53")
    PipeNZ5LAB = get_comp("pipe51")
    PipeNZ5AC  = get_comp("pipe52")
    PipeNZ5UAB = get_comp("pipe53")
    DHSNZ6LAB = get_comp("hslab61")
    DHSNZ6AC  = get_comp("hslab62")
    DHSNZ6UAB = get_comp("hslab63")
    PipeNZ6LAB = get_comp("pipe61")
    PipeNZ6AC  = get_comp("pipe62")
    PipeNZ6UAB = get_comp("pipe63")

    from rpdat import TOREF,TFR
    from rpdat import TC1AC1  ,TC1LAB1 ,TC1UAB1 ,TC2AC1  ,TC2LAB1 ,TC2UAB1 ,TC3AC1,TC3LAB1 ,TC3UAB1 ,TCDAC1,TCDLAB1 ,TCDUAB1 ,TCD2AC1 ,TCD2LAB1,TCD2UAB1
    from rpdat import TC1AC2  ,TC1LAB2 ,TC1UAB2 ,TC2AC2  ,TC2LAB2 ,TC2UAB2 ,TC3AC2,TC3LAB2 ,TC3UAB2 ,TCDAC2,TCDLAB2 ,TCDUAB2 ,TCD2AC2 ,TCD2LAB2,TCD2UAB2
    from rpdat import TC1AC3  ,TC1LAB3 ,TC1UAB3 ,TC2AC3  ,TC2LAB3 ,TC2UAB3 ,TC3AC3  ,TC3LAB3 ,TC3UAB3 ,TCDAC3  ,TCDLAB3 ,TCDUAB3 ,TCD2AC3 ,TCD2LAB3,TCD2UAB3
    from rpdat import TC1AC4  ,TC1LAB4 ,TC1UAB4 ,TC2AC4  ,TC2LAB4 ,TC2UAB4 ,TC3AC4  ,TC3LAB4 ,TC3UAB4 ,TCDAC4  ,TCDLAB4 ,TCDUAB4 ,TCD2AC4 ,TCD2LAB4,TCD2UAB4
    from rpdat import TC1AC5  ,TC1LAB5 ,TC1UAB5 ,TC2AC5  ,TC2LAB5 ,TC2UAB5 ,TC3AC5  ,TC3LAB5 ,TC3UAB5 ,TCDAC5  ,TCDLAB5 ,TCDUAB5 ,TCD2AC5 ,TCD2LAB5,TCD2UAB5
    from rpdat import TC1AC6  ,TC1LAB6 ,TC1UAB6 ,TC2AC6  ,TC2LAB6 ,TC2UAB6 ,TC3AC6  ,TC3LAB6 ,TC3UAB6 ,TCDAC6  ,TCDLAB6 ,TCDUAB6 ,TCD2AC6 ,TCD2LAB6,TCD2UAB6


    # calculate TRFL, TRCL, TRNA, TRDOP
    TRFL  = 0.0
    TRCL  = 0.0
    TRNA  = 0.0
    TRDOP = 0.0

    # 1ST ZONE
    RFL  = 0.0
    RCL  = 0.0
    RNA  = 0.0
    RDOP = 0.0

    K = 0
    for K in range(10): #pending automate
        # fuel region 
        TNAAC = PipeNZ1AC.faces[K].dnode.ttemp_gues
        RNA = RNA + TC3AC1[K-1]*(TNAAC-TOREF)
        
        TDA3 = DHSNZ1AC.layers[0].nodes[10+K].temp_gues
        TDA4 = DHSNZ1AC.layers[1].ifaces[10+K].temp_gues
        TDA6=0.5*(TDA3+TDA4)
        QDNA=TDA6/TOREF
        if (TDA6<=1000.0 and TDA6 > 473.0):#pending automate
            RDOP = RDOP + TCDAC1[K-1]*math.log(QDNA)
        elif (TDA6 > 1000.0 and TDA6 <= 2000.0):
            RDOP = RDOP + TCD2AC1[K-1]*math.log(QDNA)
        else:
            print("warning: Doppler out of range. Time = " + time)
            sys.exit()

        TAC1 = DHSNZ1AC.layers[2].nodes[K].temp_gues
        TAC2 = DHSNZ1AC.layers[2].nodes[K].eface.temp_gues
        TAC=0.5*(TAC1+TAC2)
        RCL = RCL + TC2AC1[K-1]*(TAC-TOREF)

        IFR = 0
        if (IFR==1): # fuel stuck to clad
            RFL = RFL + TC1AC1[K-1]*(TAC-TOREF)
        elif (IFR==0): # fuel free to expand
            RFL = RFL + TC1AC1[K-1]*(TDA6-TOREF)

    K = 0
    # bottom axial blanket region
    TLAB1 = DHSNZ1LAB.layers[2].nodes[K].temp_gues
    TLAB2 = DHSNZ1LAB.layers[2].nodes[K].eface.temp_gues
    TLAB=0.5*(TLAB1+TLAB2)
    RCL = RCL + TC2LAB1*(TLAB-TOREF)

    TNALAB = PipeNZ1LAB.dnode.ttemp_gues
    RNA = RNA + TC3LAB1*(TNALAB-TOREF)

    TDL3 = DHSNZ1LAB.layers[0].nodes[1+K].temp_gues
    TDL4 = DHSNZ1LAB.layers[1].ifaces[1+K].temp_gues
    TDL6=0.5*(TDL3+TDL4)
    QDNL=TDL6/TOREF
    if (TDL6<=1000.0 and TDL6 > 473.0):
        RDOP = RDOP + TCDLAB1*math.log(QDNL)
    elif (TDL6 > 1000.0 and TDL6 <= 2000.0):
        RDOP = RDOP + TCD2LAB1*math.log(QDNL)
    else:
      print("warning: Doppler out of range. time = " + Time)
      sys.exit()

    if (IFR==1): #fuel stuck to clad
        RFL = RFL + TC1LAB1*(TLAB-TOREF)
    elif (IFR==0): #fuel free to expand
        RFL = RFL + TC1LAB1*(TDL6-TOREF)

    # upper axial blanket
    TUAB1 = DHSNZ1UAB.layers[2].nodes[K].temp_gues
    TUAB2 = DHSNZ1UAB.layers[2].nodes[K].eface.temp_gues
    TUAB = 0.5*(TUAB1+TUAB2)
    RCL = RCL + TC2UAB1*(TUAB-TOREF)

    TNAUAB = PipeNZ1UAB.dnode.ttemp_gues
    RNA = RNA + TC3UAB1*(TNAUAB-TOREF)

    TDU3 = DHSNZ1UAB.layers[0].nodes[1+K].temp_gues
    TDU4 = DHSNZ1UAB.layers[1].ifaces[1+K].temp_gues
    TDU6=0.5*(TDU3+TDU4)
    QDNU=TDU6/TOREF
    if (TDU6<=1000.0 and TDU6 > 473.0):
        RDOP = RDOP + TCDUAB1*math.log(QDNU)
    elif (TDU6 > 1000.0 and TDU6 <= 2000.0):
        RDOP = RDOP + TCD2UAB1*math.log(QDNU)
    else:
        print("warning: Doppler out of range. time = " + Time)
        sys.exit()

    if (IFR==1): #fuel stuck to clad
        RFL = RFL + TC1UAB1*(TUAB-TOREF)
    elif (IFR==0): #fuel free to expand
       RFL = RFL + TC1UAB1*(TDU6-TOREF)

    TRCL = TRCL + RCL
    TRFL = TRFL + RFL
    TRNA = TRNA + RNA
    TRDOP = TRDOP + RDOP

    print ("flag1",TRNA,TRDOP,TRFL,TRCL)
    sys.exit()

    # // 2ND ZONE
    # RFL=0.0;
    # RCL=0.0;
    # RNA=0.0;
    # RDOP=0.0;

    # for (K=1;K<=10;K++) {
      # IPS.Properties.Double TAC1 = DHSNZ2AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 5, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
      # IPS.Properties.Double TAC2 = DHSNZ2AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 5, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
      # TAC=0.5*(TAC1+TAC2);
      # RCL = RCL + TC2AC2[K-1]*(TAC-TOREF);
      # IPS.Properties.Double TNAAC = PipeNZ2AC.GetPropertyFromFullDisplayName("Downstream node, Increment "+K+".{Flow Node Results}Total temperature") as IPS.Properties.Double;
     # RNA = RNA + TC3AC2[K-1]*(TNAAC-TOREF);

      # IPS.Properties.Double TDA3 = DHSNZ2AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 2, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
      # IPS.Properties.Double TDA4 = DHSNZ2AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 2, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
      # TDA6=0.5*(TDA3+TDA4);
      # QDNA=TDA6/(TOREF);
      # if (TDA6<=1000.0 && TDA6 > 473.0) {
          # RDOP = RDOP + TCDAC2[K-1]*Math.Log(QDNA);
      # }
      # else if (TDA6 > 1000.0 && TDA6 <= 2000.0){
          # RDOP = RDOP + TCD2AC2[K-1]*Math.Log(QDNA);
      # }
      # else {
          # IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range. time = "+ Time); 
          # return;
      # }
     
        # // if (IFR==1) { //fuel stuck to clad
            # // RFL = RFL + TC1AC2[K-1]*(TAC-TOREF);
        # // }
        # // else if (IFR==0) { //fuel free to expand
            # RFL = RFL + TC1AC2[K-1]*(TDA6-TOREF);
        # // }

    # }

    # TLAB1 = DHSNZ2LAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
    # TLAB2 = DHSNZ2LAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
    # TLAB=0.5*(TLAB1+TLAB2);
    # RCL = RCL + TC2LAB2*(TLAB-TOREF);

    # TNALAB = PipeNZ2LAB.GetPropertyFromPropID("TotalTemperatureNode2") as IPS.Properties.Double;
    # RNA = RNA + TC3LAB2*(TNALAB-TOREF);

    # TDL3 = DHSNZ2LAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
    # TDL4 = DHSNZ2LAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
    # TDL6=0.5*(TDL3+TDL4);
    # QDNL=TDL6/(TOREF);
      # if (TDL6<=1000.0 && TDL6 > 473.0) {
          # RDOP = RDOP + TCDLAB2*Math.Log(QDNL);
      # }
      # else if (TDL6 > 1000.0 && TDL6 <= 2000.0){
          # RDOP = RDOP + TCD2LAB2*Math.Log(QDNL);
      # }
      # else {
          # IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range. time =" + Time); 
          # return;
      # }

        # // if (IFR==1) { //fuel stuck to clad
            # // RFL = RFL + TC1LAB2*(TLAB-TOREF);
        # // }
        # // else if (IFR==0) { //fuel free to expand
            # RFL = RFL + TC1LAB2*(TDL6-TOREF);
        # // }

    # TUAB1 = DHSNZ2UAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
    # TUAB2 = DHSNZ2UAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
    # TUAB = 0.5*(TUAB1+TUAB2);
    # RCL = RCL + TC2UAB2*(TUAB-TOREF);
    # TNAUAB = PipeNZ2UAB.GetPropertyFromPropID("TotalTemperatureNode2") as IPS.Properties.Double;
    # RNA = RNA + TC3UAB2*(TNAUAB-TOREF);

    # TDU3 = DHSNZ2UAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
    # TDU4 = DHSNZ2UAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
    # TDU6=0.5*(TDU3+TDU4);
    # QDNU=TDU6/(TOREF);
      # if (TDU6<=1000.0 && TDU6 > 473.0) {
          # RDOP = RDOP + TCDUAB2*Math.Log(QDNU);
      # }
      # else if (TDU6 > 1000.0 && TDU6 <= 2000.0){
          # RDOP = RDOP + TCD2UAB2*Math.Log(QDNU);
      # }
      # else {
          # IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range Time = "+Time);
          # return;
      # }

        # // if (IFR==1) { //fuel stuck to clad
            # // RFL = RFL + TC1UAB2*(TUAB-TOREF);
        # // }
        # // else if (IFR==0) { //fuel free to expand
            # RFL = RFL + TC1UAB2*(TDU6-TOREF);
        # // }


    # TRCL.Value = TRCL.Value + RCL;
    # TRFL.Value = TRFL.Value + RFL;
    # TRNA.Value = TRNA.Value + RNA;
    # TRDOP.Value = TRDOP.Value + RDOP;

action_setup.Action(None,None,pk1)
