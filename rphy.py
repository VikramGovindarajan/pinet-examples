


// 3RD ZONE
RFL=0.0;
RCL=0.0;
RNA=0.0;
RDOP=0.0;

for (K=1;K<=10;K++) {
  IPS.Properties.Double TAC1 = DHSNZ3AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 5, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
  IPS.Properties.Double TAC2 = DHSNZ3AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 5, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
  TAC=0.5*(TAC1+TAC2);
 RCL = RCL + TC2AC3[K-1]*(TAC-TOREF);
  IPS.Properties.Double TNAAC = PipeNZ3AC.GetPropertyFromFullDisplayName("Downstream node, Increment "+K+".{Flow Node Results}Total temperature") as IPS.Properties.Double;
 RNA = RNA + TC3AC3[K-1]*(TNAAC-TOREF);

  IPS.Properties.Double TDA3 = DHSNZ3AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 2, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
  IPS.Properties.Double TDA4 = DHSNZ3AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 2, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
  TDA6=0.5*(TDA3+TDA4);
  QDNA=TDA6/(TOREF);
  if (TDA6<=1000.0 && TDA6 > 473.0) {
      RDOP = RDOP + TCDAC3[K-1]*Math.Log(QDNA);
  }
  else if (TDA6 > 1000.0 && TDA6 <= 2000.0){
      RDOP = RDOP + TCD2AC3[K-1]*Math.Log(QDNA);
  }
  else {
      IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range time = " + Time);
      return;
  } 
    // if (IFR==1) { //fuel stuck to clad
        // RFL = RFL + TC1AC3[K-1]*(TAC-TOREF);
    // }
    // else if (IFR==0) { //fuel free to expand
        RFL = RFL + TC1AC3[K-1]*(TDA6-TOREF);
    // }
}

TLAB1 = DHSNZ3LAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TLAB2 = DHSNZ3LAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TLAB=0.5*(TLAB1+TLAB2);
RCL = RCL + TC2LAB3*(TLAB-TOREF);
TNALAB = PipeNZ3LAB.GetPropertyFromPropID("TotalTemperatureNode2") as IPS.Properties.Double;
RNA = RNA + TC3LAB3*(TNALAB-TOREF);

TDL3 = DHSNZ3LAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDL4 = DHSNZ3LAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDL6=0.5*(TDL3+TDL4);
QDNL=TDL6/(TOREF);
  if (TDL6<=1000.0 && TDL6 > 473.0) {
      RDOP = RDOP + TCDLAB3*Math.Log(QDNL);
  }
  else if (TDL6 > 1000.0 && TDL6 <= 2000.0){
      RDOP = RDOP + TCD2LAB3*Math.Log(QDNL);
  }
  else {
      IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range time = " + Time);
      return;
  }

// if (IFR==1) { //fuel stuck to clad
    // RFL = RFL + TC1LAB3*(TLAB-TOREF);
// }
// else if (IFR==0) { //fuel free to expand
    RFL = RFL + TC1LAB3*(TDL6-TOREF);
// }


TUAB1 = DHSNZ3UAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TUAB2 = DHSNZ3UAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TUAB = 0.5*(TUAB1+TUAB2);
RCL = RCL + TC2UAB3*(TUAB-TOREF);
TNAUAB = PipeNZ3UAB.GetPropertyFromPropID("TotalTemperatureNode2") as IPS.Properties.Double;
RNA = RNA + TC3UAB3*(TNAUAB-TOREF);

TDU3 = DHSNZ3UAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDU4 = DHSNZ3UAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDU6=0.5*(TDU3+TDU4);
QDNU=TDU6/(TOREF);
  if (TDU6<=1000.0 && TDU6 > 473.0) {
      RDOP = RDOP + TCDUAB3*Math.Log(QDNU);
  }
  else if (TDU6 > 1000.0 && TDU6 <= 2000.0){
      RDOP = RDOP + TCD2UAB3*Math.Log(QDNU);
  }
  else {
      IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range time = " + Time);
      return;
  }

// if (IFR==1) { //fuel stuck to clad
    // RFL = RFL + TC1UAB3*(TUAB-TOREF);
// }
// else if (IFR==0) { //fuel free to expand
    RFL = RFL + TC1UAB3*(TDU6-TOREF);
// }

/*        DUMMY1.Value = RFL*1E5;
DUMMY2.Value = RCL*1E5;
DUMMY3.Value = RNA*1E5;
DUMMY4.Value = RDOP*1E5; */

TRCL.Value = TRCL.Value + RCL;
TRFL.Value = TRFL.Value + RFL;
TRNA.Value = TRNA.Value + RNA;
TRDOP.Value = TRDOP.Value + RDOP;

// 4th ZONE
RFL=0.0;
RCL=0.0;
RNA=0.0;
RDOP=0.0;

for (K=1;K<=10;K++) {
  IPS.Properties.Double TAC1 = DHSNZ4AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 5, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
  IPS.Properties.Double TAC2 = DHSNZ4AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 5, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
  TAC=0.5*(TAC1+TAC2);
 RCL = RCL + TC2AC4[K-1]*(TAC-TOREF);
  IPS.Properties.Double TNAAC = PipeNZ4AC.GetPropertyFromFullDisplayName("Downstream node, Increment "+K+".{Flow Node Results}Total temperature") as IPS.Properties.Double;
 RNA = RNA + TC3AC4[K-1]*(TNAAC-TOREF);

  IPS.Properties.Double TDA3 = DHSNZ4AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 2, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
  IPS.Properties.Double TDA4 = DHSNZ4AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 2, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
  TDA6=0.5*(TDA3+TDA4);
  QDNA=TDA6/(TOREF);
  if (TDA6<=1000.0 && TDA6 > 473.0) {
      RDOP = RDOP + TCDAC4[K-1]*Math.Log(QDNA);
  }
  else if (TDA6 > 1000.0 && TDA6 <= 2000.0){
      RDOP = RDOP + TCD2AC4[K-1]*Math.Log(QDNA);
  }
  else {
      IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range time = " + Time);
      return;
  }
 
    // if (IFR==1) { //fuel stuck to clad
        // RFL = RFL + TC1AC4[K-1]*(TAC-TOREF);
    // }
    // else if (IFR==0) { //fuel free to expand
        RFL = RFL + TC1AC4[K-1]*(TDA6-TOREF);
    // }
}

TLAB1 = DHSNZ4LAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TLAB2 = DHSNZ4LAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TLAB=0.5*(TLAB1+TLAB2);
RCL = RCL + TC2LAB4*(TLAB-TOREF);
TNALAB = PipeNZ4LAB.GetPropertyFromPropID("TotalTemperatureNode2") as IPS.Properties.Double;
RNA = RNA + TC3LAB4*(TNALAB-TOREF);

TDL3 = DHSNZ4LAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDL4 = DHSNZ4LAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDL6=0.5*(TDL3+TDL4);
QDNL=TDL6/(TOREF);
  if (TDL6<=1000.0 && TDL6 > 473.0) {
      RDOP = RDOP + TCDLAB4*Math.Log(QDNL);
  }
  else if (TDL6 > 1000.0 && TDL6 <= 2000.0){
      RDOP = RDOP + TCD2LAB4*Math.Log(QDNL);
  }
  else {
      IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range time = " + Time);
      return;
  }

// if (IFR==1) { //fuel stuck to clad
    // RFL = RFL + TC1LAB4*(TLAB-TOREF);
// }
// else if (IFR==0) { //fuel free to expand
    RFL = RFL + TC1LAB4*(TDL6-TOREF);
// }

TUAB1 = DHSNZ4UAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TUAB2 = DHSNZ4UAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TUAB = 0.5*(TUAB1+TUAB2);
RCL = RCL + TC2UAB4*(TUAB-TOREF);
RFL = RFL + TC1UAB4*(TUAB-TOREF);
TNAUAB = PipeNZ4UAB.GetPropertyFromPropID("TotalTemperatureNode2") as IPS.Properties.Double;
RNA = RNA + TC3UAB4*(TNAUAB-TOREF);

TDU3 = DHSNZ4UAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDU4 = DHSNZ4UAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDU6=0.5*(TDU3+TDU4);
QDNU=TDU6/(TOREF);
  if (TDU6<=1000.0 && TDU6 > 473.0) {
      RDOP = RDOP + TCDUAB4*Math.Log(QDNU);
  }
  else if (TDU6 > 1000.0 && TDU6 <= 2000.0){
      RDOP = RDOP + TCD2UAB4*Math.Log(QDNU);
  }
  else {
      IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range time = " + Time);
      return;
  }

// if (IFR==1) { //fuel stuck to clad
    // RFL = RFL + TC1UAB4*(TUAB-TOREF);
// }
// else if (IFR==0) { //fuel free to expand
    RFL = RFL + TC1UAB4*(TDU6-TOREF);
// }

TRCL.Value = TRCL.Value + RCL;
TRFL.Value = TRFL.Value + RFL;
TRNA.Value = TRNA.Value + RNA;
TRDOP.Value = TRDOP.Value + RDOP;

// 5th zone
RFL=0.0;
RCL=0.0;
RNA=0.0;
RDOP=0.0;

for (K=1;K<=10;K++) {
  IPS.Properties.Double TAC1 = DHSNZ5AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 5, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
  IPS.Properties.Double TAC2 = DHSNZ5AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 5, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
  TAC=0.5*(TAC1+TAC2);
 RCL = RCL + TC2AC5[K-1]*(TAC-TOREF);
  IPS.Properties.Double TNAAC = PipeNZ5AC.GetPropertyFromFullDisplayName("Downstream node, Increment "+K+".{Flow Node Results}Total temperature") as IPS.Properties.Double;
 RNA = RNA + TC3AC5[K-1]*(TNAAC-TOREF);

  IPS.Properties.Double TDA3 = DHSNZ5AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 2, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
  IPS.Properties.Double TDA4 = DHSNZ5AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 2, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
  TDA6=0.5*(TDA3+TDA4);
  QDNA=TDA6/(TOREF);
  if (TDA6<=1000.0 && TDA6 > 473.0) {
      RDOP = RDOP + TCDAC5[K-1]*Math.Log(QDNA);
  }
  else if (TDA6 > 1000.0 && TDA6 <= 2000.0){
      RDOP = RDOP + TCD2AC5[K-1]*Math.Log(QDNA);
  }
  else {
      IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range time = " + Time);
      return;
  }
 
    // if (IFR==1) { //fuel stuck to clad
        // RFL = RFL + TC1AC5[K-1]*(TAC-TOREF);
    // }
    // else if (IFR==0) { //fuel free to expand
        RFL = RFL + TC1AC5[K-1]*(TDA6-TOREF);
    // } 
}

TLAB1 = DHSNZ5LAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TLAB2 = DHSNZ5LAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TLAB=0.5*(TLAB1+TLAB2);
RCL = RCL + TC2LAB5*(TLAB-TOREF);
TNALAB = PipeNZ5LAB.GetPropertyFromPropID("TotalTemperatureNode2") as IPS.Properties.Double;
RNA = RNA + TC3LAB5*(TNALAB-TOREF);

TDL3 = DHSNZ5LAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDL4 = DHSNZ5LAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDL6=0.5*(TDL3+TDL4);
QDNL=TDL6/(TOREF);
  if (TDL6<=1000.0 && TDL6 > 473.0) {
      RDOP = RDOP + TCDLAB5*Math.Log(QDNL);
  }
  else if (TDL6 > 1000.0 && TDL6 <= 2000.0){
      RDOP = RDOP + TCD2LAB5*Math.Log(QDNL);
  }
  else {
      IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range time = "+ Time);
      return;
  }

// if (IFR==1) { //fuel stuck to clad
    // RFL = RFL + TC1LAB5*(TLAB-TOREF);
// }
// else if (IFR==0) { //fuel free to expand
    RFL = RFL + TC1LAB5*(TDL6-TOREF);
// }

TUAB1 = DHSNZ5UAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TUAB2 = DHSNZ5UAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TUAB = 0.5*(TUAB1+TUAB2);
RCL = RCL + TC2UAB5*(TUAB-TOREF);
TNAUAB = PipeNZ5UAB.GetPropertyFromPropID("TotalTemperatureNode2") as IPS.Properties.Double;
RNA = RNA + TC3UAB5*(TNAUAB-TOREF);

TDU3 = DHSNZ5UAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDU4 = DHSNZ5UAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDU6=0.5*(TDU3+TDU4);
QDNU=TDU6/(TOREF);
  if (TDU6<=1000.0 && TDU6 > 473.0) {
      RDOP = RDOP + TCDUAB5*Math.Log(QDNU);
  }
  else if (TDU6 > 1000.0 && TDU6 <= 2000.0){
      RDOP = RDOP + TCD2UAB5*Math.Log(QDNU);
  }
  else {
      IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range time = " + Time);
      return;
  }

// if (IFR==1) { //fuel stuck to clad
    // RFL = RFL + TC1UAB5*(TUAB-TOREF);
// }
// else if (IFR==0) { //fuel free to expand
    RFL = RFL + TC1UAB5*(TDU6-TOREF);
// }

/* DUMMY1.Value = RFL*1E5;
DUMMY2.Value = RCL*1E5;
DUMMY3.Value = RNA*1E5;
DUMMY4.Value = RDOP*1E5;
 */   


TRCL.Value = TRCL.Value + RCL;
TRFL.Value = TRFL.Value + RFL;
TRNA.Value = TRNA.Value + RNA;
TRDOP.Value = TRDOP.Value + RDOP;

//6th zone
RFL=0.0;
RCL=0.0;
RNA=0.0;
RDOP=0.0;

for (K=1;K<=10;K++) {
  IPS.Properties.Double TAC1 = DHSNZ6AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 5, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
  IPS.Properties.Double TAC2 = DHSNZ6AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 5, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
  TAC=0.5*(TAC1+TAC2);
 RCL = RCL + TC2AC6[K-1]*(TAC-TOREF);
  IPS.Properties.Double TNAAC = PipeNZ6AC.GetPropertyFromFullDisplayName("Downstream node, Increment "+K+".{Flow Node Results}Total temperature") as IPS.Properties.Double;
 RNA = RNA + TC3AC6[K-1]*(TNAAC-TOREF);

  IPS.Properties.Double TDA3 = DHSNZ6AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 2, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
  IPS.Properties.Double TDA4 = DHSNZ6AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 2, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
  TDA6=0.5*(TDA3+TDA4);
  QDNA=TDA6/(TOREF);
  if (TDA6<=1000.0 && TDA6 > 473.0) {
      RDOP = RDOP + TCDAC6[K-1]*Math.Log(QDNA);
  }
  else if (TDA6 > 1000.0 && TDA6 <= 2000.0){
      RDOP = RDOP + TCD2AC6[K-1]*Math.Log(QDNA);
  }
  else {
      IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range time = " + Time);
      return;
  }
 
    // if (IFR==1) { //fuel stuck to clad
        // RFL = RFL + TC1AC6[K-1]*(TAC-TOREF);
    // }
    // else if (IFR==0) { //fuel free to expand
        RFL = RFL + TC1AC6[K-1]*(TDA6-TOREF);
    // } 
 }

TLAB1 = DHSNZ6LAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TLAB2 = DHSNZ6LAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TLAB=0.5*(TLAB1+TLAB2);
RCL = RCL + TC2LAB6*(TLAB-TOREF);
TNALAB = PipeNZ6LAB.GetPropertyFromPropID("TotalTemperatureNode2") as IPS.Properties.Double;
RNA = RNA + TC3LAB6*(TNALAB-TOREF);

TDL3 = DHSNZ6LAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDL4 = DHSNZ6LAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDL6=0.5*(TDL3+TDL4);
QDNL=TDL6/(TOREF);
  if (TDL6<=1000.0 && TDL6 > 473.0) {
      RDOP = RDOP + TCDLAB6*Math.Log(QDNL);
  }
  else if (TDL6 > 1000.0 && TDL6 <= 2000.0){
      RDOP = RDOP + TCD2LAB6*Math.Log(QDNL);
  }
  else {
      IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range time = "+Time);
      return;
  }

// if (IFR==1) { //fuel stuck to clad
    // RFL = RFL + TC1LAB6*(TLAB-TOREF);
// }
// else if (IFR==0) { //fuel free to expand
    RFL = RFL + TC1LAB6*(TDL6-TOREF);
// }

TUAB1 = DHSNZ6UAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TUAB2 = DHSNZ6UAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
TUAB = 0.5*(TUAB1+TUAB2);
RCL = RCL + TC2UAB6*(TUAB-TOREF);
TNAUAB = PipeNZ6UAB.GetPropertyFromPropID("TotalTemperatureNode2") as IPS.Properties.Double;
RNA = RNA + TC3UAB6*(TNAUAB-TOREF);

TDU3 = DHSNZ6UAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDU4 = DHSNZ6UAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
TDU6=0.5*(TDU3+TDU4);
QDNU=TDU6/(TOREF);
  if (TDU6<=1000.0 && TDU6 > 473.0) {
      RDOP = RDOP + TCDUAB6*Math.Log(QDNU);
  }
  else if (TDU6 > 1000.0 && TDU6 <= 2000.0){
      RDOP = RDOP + TCD2UAB6*Math.Log(QDNU);
  }
  else {
      IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: Doppler out of range time = "+ Time);
      return;
  }

// if (IFR==1) { //fuel stuck to clad
    // RFL = RFL + TC1UAB6*(TUAB-TOREF);
// }
// else if (IFR==0) { //fuel free to expand
    RFL = RFL + TC1UAB6*(TDU6-TOREF);
// }

/* DUMMY1.Value = RFL*1E5;
DUMMY2.Value = RCL*1E5;
DUMMY3.Value = RNA*1E5;
DUMMY4.Value = RDOP*1E5;
 */   

TRCL.Value = TRCL.Value + RCL;
TRFL.Value = TRFL.Value + RFL;
TRNA.Value = TRNA.Value + RNA;
TRDOP.Value = TRDOP.Value + RDOP;

// calculate RBMF
RBMF.Value=0.0;
int I;
for (I=1;I<=6;I++) {
    double SUM1=0.0;
    for (K=1;K<=10;K++) { // fuel region
        if (I==1) {
            // if (IFR==1) {
                // IPS.Properties.Double TAC1 = DHSNZ1AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 5, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
                // IPS.Properties.Double TAC2 = DHSNZ1AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 5, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double; 
                // TLAB1 = DHSNZ1LAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TLAB2 = DHSNZ1LAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TUAB1 = DHSNZ1UAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TUAB2 = DHSNZ1UAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TAC=0.5*(TAC1+TAC2);
                // SUM1=SUM1+TAC-TOREF;
                // TLAB=0.5*(TLAB1+TLAB2);
                // TUAB=0.5*(TUAB1+TUAB2);
            // }
            // else {
                IPS.Properties.Double TDA3 = DHSNZ1AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 2, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
                IPS.Properties.Double TDA4 = DHSNZ1AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 2, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
                TDA6=0.5*(TDA3+TDA4);
                TDL3 = DHSNZ1LAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDL4 = DHSNZ1LAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDL6=0.5*(TDL3+TDL4);
                TDU3 = DHSNZ1UAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDU4 = DHSNZ1UAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDU6=0.5*(TDU3+TDU4);
                SUM1=SUM1+TDA6-TOREF;
            // }
        }
        else if (I==2) {
            // if (IFR==1) {
                // IPS.Properties.Double TAC1 = DHSNZ2AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 5, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
                // IPS.Properties.Double TAC2 = DHSNZ2AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 5, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double; 
                // TLAB1 = DHSNZ2LAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TLAB2 = DHSNZ2LAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TUAB1 = DHSNZ2UAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TUAB2 = DHSNZ2UAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TAC=0.5*(TAC1+TAC2);
                // SUM1=SUM1+TAC-TOREF;
                // TLAB=0.5*(TLAB1+TLAB2);
                // TUAB=0.5*(TUAB1+TUAB2);
            // }
            // else {
                IPS.Properties.Double TDA3 = DHSNZ2AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 2, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
                IPS.Properties.Double TDA4 = DHSNZ2AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 2, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
                TDA6=0.5*(TDA3+TDA4);
                TDL3 = DHSNZ2LAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDL4 = DHSNZ2LAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDL6=0.5*(TDL3+TDL4);
                TDU3 = DHSNZ2UAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDU4 = DHSNZ2UAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDU6=0.5*(TDU3+TDU4);
                SUM1=SUM1+TDA6-TOREF;
            // }
        }
        else if (I==3) {
            // if (IFR==1) {
                // IPS.Properties.Double TAC1 = DHSNZ3AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 5, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
                // IPS.Properties.Double TAC2 = DHSNZ3AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 5, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double; 
                // TLAB1 = DHSNZ3LAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TLAB2 = DHSNZ3LAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TUAB1 = DHSNZ3UAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TUAB2 = DHSNZ3UAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TAC=0.5*(TAC1+TAC2);
                // SUM1=SUM1+TAC-TOREF;
                // TLAB=0.5*(TLAB1+TLAB2);
                // TUAB=0.5*(TUAB1+TUAB2);
            // }
            // else {
                IPS.Properties.Double TDA3 = DHSNZ3AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 2, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
                IPS.Properties.Double TDA4 = DHSNZ3AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 2, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
                TDA6=0.5*(TDA3+TDA4);
                TDL3 = DHSNZ3LAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDL4 = DHSNZ3LAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDL6=0.5*(TDL3+TDL4);
                TDU3 = DHSNZ3UAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDU4 = DHSNZ3UAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDU6=0.5*(TDU3+TDU4);
                SUM1=SUM1+TDA6-TOREF;
            // }
        }
        else if (I==4) {
            // if (IFR==1) {
                // IPS.Properties.Double TAC1 = DHSNZ4AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 5, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
                // IPS.Properties.Double TAC2 = DHSNZ4AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 5, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double; 
                // TLAB1 = DHSNZ4LAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TLAB2 = DHSNZ4LAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TUAB1 = DHSNZ4UAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TUAB2 = DHSNZ4UAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TAC=0.5*(TAC1+TAC2);
                // SUM1=SUM1+TAC-TOREF;
                // TLAB=0.5*(TLAB1+TLAB2);
                // TUAB=0.5*(TUAB1+TUAB2);
            // }
            // else {
                IPS.Properties.Double TDA3 = DHSNZ4AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 2, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
                IPS.Properties.Double TDA4 = DHSNZ4AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 2, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
                TDA6=0.5*(TDA3+TDA4);
                TDL3 = DHSNZ4LAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDL4 = DHSNZ4LAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDL6=0.5*(TDL3+TDL4);
                TDU3 = DHSNZ4UAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDU4 = DHSNZ4UAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDU6=0.5*(TDU3+TDU4);
                SUM1=SUM1+TDA6-TOREF;
            // }
        }
        else if (I==5) {
            // if (IFR==1) {
                // IPS.Properties.Double TAC1 = DHSNZ5AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 5, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
                // IPS.Properties.Double TAC2 = DHSNZ5AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 5, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double; 
                // TLAB1 = DHSNZ5LAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TLAB2 = DHSNZ5LAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TUAB1 = DHSNZ5UAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TUAB2 = DHSNZ5UAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TAC=0.5*(TAC1+TAC2);
                // SUM1=SUM1+TAC-TOREF;
                // TLAB=0.5*(TLAB1+TLAB2);
                // TUAB=0.5*(TUAB1+TUAB2);
            // }
            // else {
                IPS.Properties.Double TDA3 = DHSNZ5AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 2, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
                IPS.Properties.Double TDA4 = DHSNZ5AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 2, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
                TDA6=0.5*(TDA3+TDA4);
                TDL3 = DHSNZ5LAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDL4 = DHSNZ5LAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDL6=0.5*(TDL3+TDL4);
                TDU3 = DHSNZ5UAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDU4 = DHSNZ5UAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDU6=0.5*(TDU3+TDU4);
                SUM1=SUM1+TDA6-TOREF;
            // }
        }
        else if (I==6) {
            // if (IFR==1) {
                // IPS.Properties.Double TAC1 = DHSNZ6AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 5, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
                // IPS.Properties.Double TAC2 = DHSNZ6AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 5, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
                // TLAB1 = DHSNZ6LAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TLAB2 = DHSNZ6LAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TUAB1 = DHSNZ6UAB.GetPropertyFromPropID("UN,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TUAB2 = DHSNZ6UAB.GetPropertyFromPropID("SE,5,-1,-1,-1.Temperature") as IPS.Properties.Double;
                // TAC=0.5*(TAC1+TAC2);
                // SUM1=SUM1+TAC-TOREF;
                // TLAB=0.5*(TLAB1+TLAB2);
                // TUAB=0.5*(TUAB1+TUAB2);
            // }
            // else {
                IPS.Properties.Double TDA3 = DHSNZ6AC.GetPropertyFromFullDisplayName("Upstream node, HT element direction 2, Cross direction "+K+".{Solid Node Results}Temperature") as IPS.Properties.Double;
                IPS.Properties.Double TDA4 = DHSNZ6AC.GetPropertyFromFullDisplayName("Sub-element, HT element direction 2, Cross direction "+K+".{Generic}Temperature") as IPS.Properties.Double;
                TDA6=0.5*(TDA3+TDA4);
                TDL3 = DHSNZ6LAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDL4 = DHSNZ6LAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDL6=0.5*(TDL3+TDL4);
                TDU3 = DHSNZ6UAB.GetPropertyFromPropID("UN,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDU4 = DHSNZ6UAB.GetPropertyFromPropID("SE,2,-1,-1,-1.Temperature") as IPS.Properties.Double;
                TDU6=0.5*(TDU3+TDU4);
                SUM1=SUM1+TDA6-TOREF;
            // }
        }
    }
    // if (IFR==1) { //upper and lower axial blanket region
        // SUM1=SUM1+TLAB-TOREF;
        // SUM1=SUM1+TUAB-TOREF;
    // }
    // else {
        SUM1=SUM1+TDL6-TOREF;
        SUM1=SUM1+TDU6-TOREF;
    // }

    if (I==1) {
    RBMF.Value=RBMF.Value+TC1AC1[9]*SUM1*(-1.0);
    }
    else if (I==2) {
    RBMF.Value=RBMF.Value+TC1AC2[9]*SUM1*(-1.0);}
    else if (I==3) {
    RBMF.Value=RBMF.Value+TC1AC3[9]*SUM1*(-1.0);}
    else if (I==4) {
    RBMF.Value=RBMF.Value+TC1AC4[9]*SUM1*(-1.0);}
    else if (I==5) {
    RBMF.Value=RBMF.Value+TC1AC5[9]*SUM1*(-1.0);}
    else {
    RBMF.Value=RBMF.Value+TC1AC6[9]*SUM1*(-1.0);
    }
}


// calculate TCGR, TCCR
IPS.Core.Component QSDTRC = IPS.Server.IProject.GetInstance().GetComponent("QS-DTRC");
IPS.Properties.Double DTC = QSDTRC.GetPropertyFromFullDisplayName("{Script}Script.Script Inputs And Outputs.{OUTPUT}DTRC") as IPS.Properties.Double;
IPS.Core.Component QSDTRG = IPS.Server.IProject.GetInstance().GetComponent("QS-DTRG");
IPS.Properties.Double DTG = QSDTRG.GetPropertyFromFullDisplayName("{Script}Script.Script Inputs And Outputs.{OUTPUT}DTRG") as IPS.Properties.Double;
IPS.Core.Component QSDTRV = IPS.Server.IProject.GetInstance().GetComponent("QS-DTRV");
IPS.Properties.Double DTR = QSDTRV.GetPropertyFromFullDisplayName("{Script}Script.Script Inputs And Outputs.{OUTPUT}DTRV") as IPS.Properties.Double;

double TCGR = -0.952410817E-5;
double WDCR = -7.82E-5*1000.0;
RG.Value = TCGR*(DTG.Value-273.15);
double ALCR = 1.60e-5;
double ALRV = 1.60e-5;
double EFLCR =4.89;
double EFLRV =7.341;
double DLCR=ALCR*EFLCR*(DTC.Value-273.15);
double DLRV=ALRV*EFLRV*(DTR.Value-273.15);
RC.Value = WDCR*(DLCR-DLRV);

double [] gemW= new double [] {-4.9759601E-03,-4.9759601E-03,-4.9727950E-03,-4.9465660E-03,
     -4.8999230E-03,-4.8770560E-03,-4.5790760E-03,
     -4.5042170E-03,-4.0803270E-03,-3.6035070E-03,
     -3.1068070E-03,-2.6024970E-03,-2.0963570E-03,
     -1.6033470E-03,-1.1575970E-03,-7.7857700E-04,
     -4.5669700E-04,-2.0180700E-04,-1.6020400E-04,
    -2.3214000E-05,-5.4510000E-06,0.0000000E+00};
     
double [] gemh= new double [] {0.0,25.520,37.250,52.770,62.410,65.270,79.860,81.910,
     91.138,100.366,109.594,118.822,128.050,137.278,146.506,
    155.734,164.962,174.190,176.240,189.540,199.780,207.350};

  IPS.Core.Component PipeRIP = IPS.Server.IProject.GetInstance().GetComponent("GER - 1");
  IPS.Properties.Double QR = PipeRIP.GetPropertyFromFullDisplayName("{Flow Element Results,Generic}Total mass flow") as IPS.Properties.Double;
  double geml=265.0-539504/(2440.13+QR*QR/(734.08*3*734.08*3)*100*100);
  geml=geml-18.59;      
  if (geml <= 25.3 || geml >= 207.35) {
    IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("warning: geml out of range time = " + Time);
  }

  for (K=1;K<=22;K++) {
    if (geml<=gemh[K-1]) {
      RGEM.Value=gemW[K-1]*450.0/497.59601-(gemW[K-1]*450.0/497.59601-gemW[K-1-1]*450.0/497.59601)/(gemh[K-1]-gemh[K-1-1])*(gemh[K-1]-geml);
      break;
    }
  }

TFR=TRFL.Value+TRCL.Value+TRNA.Value+TRDOP.Value+RBMF.Value+RG.Value+RC.Value+RGEM.Value;

if (Time==0) {
   REXTSS.Value = -TFR;
   RTOT.Value  = 0;
}
 else {
   REXT=REXTSS.Value+REXTCR.Value+REXTSC.Value;
   RTOT.Value = REXT+TFR;
}

// Q2
double DT = TimeStep;

double DKK = RTOT.Value;
double[] AUXCI1 = new double[6];
double[] AUXCI2 = new double[6];
double[] QALPHA = new double[6];
double[] QGAMMA = new double[6];
double[] QBETA = new double[6];

QBETA[0] = 8.98184E-05;
QBETA[1] = 7.51112E-04;
QBETA[2] = 6.56706E-04;
QBETA[3] = 1.22693E-03;
QBETA[4] = 5.30909E-04;
QBETA[5] = 1.69559E-04;
double[] QLAMBD = new double[6];
QLAMBD[0] = 1.29701E-02;
QLAMBD[1] = 3.13017E-02;
QLAMBD[2] = 1.34437E-01;
QLAMBD[3] = 3.41507E-01;
QLAMBD[4] = 1.35304E+00;
QLAMBD[5] = 3.70998E+00;
double QL = 4.780164E-07;
double A1,A2;
int M;
double QB=0.0;

double A11=0.0;
double A22=0.0;

for (M=0;M<=5;M++) {
    QB=QB + QBETA[M];
}
for (M=0;M<=5;M++) {
    AUXCI1[M]=2.0+DT*QLAMBD[M];
    AUXCI2[M]=(2.0-DT*QLAMBD[M])/AUXCI1[M];
}
if (Time==0) {
    CM1d.Value=(QBETA[0]*Q2d.Value)/(QL*QLAMBD[0]);
    CM2d.Value=(QBETA[1]*Q2d.Value)/(QL*QLAMBD[1]);
    CM3d.Value=(QBETA[2]*Q2d.Value)/(QL*QLAMBD[2]);
    CM4d.Value=(QBETA[3]*Q2d.Value)/(QL*QLAMBD[3]);
    CM5d.Value=(QBETA[4]*Q2d.Value)/(QL*QLAMBD[4]);
    CM6d.Value=(QBETA[5]*Q2d.Value)/(QL*QLAMBD[5]);
    CM1.Value=CM1d.Value;
    CM2.Value=CM2d.Value;
    CM3.Value=CM3d.Value;
    CM4.Value=CM4d.Value;
    CM5.Value=CM5d.Value;
    CM6.Value=CM6d.Value;

    Q2.Value = Q2d.Value;
}
else {

    /* IPS.Task.ConsoleSolverOutputProvider.GetConsoleOutputWindow().AddTextLine("CM1 = " + CM1d); */
    A1=DT*(1.0+DKK)/QL;
    
    for (M=0;M<=5;M++) {
        QALPHA[M]=QBETA[M]*A1/AUXCI1[M];
        A11=A11+QALPHA[M]*QLAMBD[M];
    }

    QGAMMA[0]=AUXCI2[0]*CM1d+Q2d.Value*QALPHA[0];
    QGAMMA[1]=AUXCI2[1]*CM2d+Q2d.Value*QALPHA[1];
    QGAMMA[2]=AUXCI2[2]*CM3d+Q2d.Value*QALPHA[2];
    QGAMMA[3]=AUXCI2[3]*CM4d+Q2d.Value*QALPHA[3];
    QGAMMA[4]=AUXCI2[4]*CM5d+Q2d.Value*QALPHA[4];
    QGAMMA[5]=AUXCI2[5]*CM6d+Q2d.Value*QALPHA[5];
    
    for (M=0;M<=5;M++) {
        A22=A22+QGAMMA[M]*QLAMBD[M];
    }

    A2=(DKK-QB*(1.0+DKK))/QL;
    Q2.Value=-A22/(A2+A11);
    Q2d.Value=Q2.Value;

    CM1.Value=Q2.Value*QALPHA[0]+QGAMMA[0];
    CM2.Value=Q2.Value*QALPHA[1]+QGAMMA[1];
    CM3.Value=Q2.Value*QALPHA[2]+QGAMMA[2];
    CM4.Value=Q2.Value*QALPHA[3]+QGAMMA[3];
    CM5.Value=Q2.Value*QALPHA[4]+QGAMMA[4];
    CM6.Value=Q2.Value*QALPHA[5]+QGAMMA[5];
    CM1d=CM1;
    CM2d=CM2;
    CM3d=CM3;
    CM4d=CM4;
    CM5d=CM5;
    CM6d=CM6;
}
//QMOY.Value = 0.076656;
PO.Value = Q2.Value + QMOY.Value;

// update power values
// Zone1
IPS.Core.Component NodeNZ1AC = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ1AC");
IPS.Core.Component NodeNZ1LAB = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ1LAB");
IPS.Core.Component NodeNZ1UAB = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ1UAB");

IPS.Core.Component NodeNZ2AC = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ2AC");
IPS.Core.Component NodeNZ2LAB = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ2LAB");
IPS.Core.Component NodeNZ2UAB = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ2UAB");

IPS.Core.Component NodeNZ3AC = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ3AC");
IPS.Core.Component NodeNZ3LAB = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ3LAB");
IPS.Core.Component NodeNZ3UAB = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ3UAB");

IPS.Core.Component NodeNZ4AC = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ4AC");
IPS.Core.Component NodeNZ4LAB = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ4LAB");
IPS.Core.Component NodeNZ4UAB = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ4UAB");

IPS.Core.Component NodeNZ5AC = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ5AC");
IPS.Core.Component NodeNZ5LAB = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ5LAB");
IPS.Core.Component NodeNZ5UAB = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ5UAB");

IPS.Core.Component NodeNZ6AC = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ6AC");
IPS.Core.Component NodeNZ6LAB = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ6LAB");
IPS.Core.Component NodeNZ6UAB = IPS.Server.IProject.GetInstance().GetComponent("Node-NZ6UAB");

// additional zone
IPS.Core.Component GERNZEX = IPS.Server.IProject.GetInstance().GetComponent("GER-NZEX");


IPS.Properties.Double gNZ1AC = NodeNZ1AC.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ1AC.Value = PO.Value * 3.3165E+06;
IPS.Properties.Double gNZ1LAB = NodeNZ1LAB.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ1LAB.Value = PO.Value * 9.7527E+03;
IPS.Properties.Double gNZ1UAB = NodeNZ1UAB.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ1UAB.Value = PO.Value * 1.4643E+04;

IPS.Properties.Double gNZ2AC = NodeNZ2AC.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ2AC.Value = PO.Value * 2.0275E+07;
IPS.Properties.Double gNZ2LAB = NodeNZ2LAB.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ2LAB.Value = PO.Value * 5.4413E+04;
IPS.Properties.Double gNZ2UAB = NodeNZ2UAB.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ2UAB.Value = PO.Value * 8.4355E+04;

IPS.Properties.Double gNZ3AC = NodeNZ3AC.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ3AC.Value = PO.Value * 2.8279E+07;
IPS.Properties.Double gNZ3LAB = NodeNZ3LAB.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ3LAB.Value = PO.Value * 7.0593E+04;
IPS.Properties.Double gNZ3UAB = NodeNZ3UAB.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ3UAB.Value = PO.Value * 1.2193E+05;

IPS.Properties.Double gNZ4AC = NodeNZ4AC.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ4AC.Value = PO.Value * 4.1711E+07;
IPS.Properties.Double gNZ4LAB = NodeNZ4LAB.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ4LAB.Value = PO.Value * 1.0201E+05;
IPS.Properties.Double gNZ4UAB = NodeNZ4UAB.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ4UAB.Value = PO.Value * 1.8841E+05;

IPS.Properties.Double gNZ5AC = NodeNZ5AC.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ5AC.Value = PO.Value * 4.3479E+07;
IPS.Properties.Double gNZ5LAB = NodeNZ5LAB.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ5LAB.Value = PO.Value * 8.8518E+04;
IPS.Properties.Double gNZ5UAB = NodeNZ5UAB.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ5UAB.Value = PO.Value * 1.7692E+05;

IPS.Properties.Double gNZ6AC = NodeNZ6AC.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ6AC.Value = PO.Value * 5.4461E+07;
IPS.Properties.Double gNZ6LAB = NodeNZ6LAB.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ6LAB.Value = PO.Value * 1.0964E+05;
IPS.Properties.Double gNZ6UAB = NodeNZ6UAB.GetPropertyFromFullDisplayName("{Heat Transfer}Heat input") as IPS.Properties.Double;
gNZ6UAB.Value = PO.Value * 2.3117E+05;

IPS.Properties.Double gNZEX = GERNZEX.GetPropertyFromFullDisplayName("{Empirical Data,Heat Transfer}Heat input") as IPS.Properties.Double;
gNZEX.Value = PO.Value * 7.113740198e6;
