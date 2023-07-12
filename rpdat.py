TOREF = 200.0+273.15

TC1AC = []
TC1LAB = []
TC1UAB = []
TC2AC = []
TC2LAB = []
TC2UAB = []
TC3AC = []
TC3LAB = []
TC3UAB = []
TCDAC = []
TCDLAB = []
TCDUAB = []
TCD2UAB = []
TCD2LAB = []
TCD2AC = []

# assigning perturbation worths
# Radial Zone1
TC1AC  .append((-6.59520E-09, -9.30070E-09, -1.19000E-08, -1.38050E-08, -1.47490E-08, -1.43510E-08, -1.26660E-08, -1.02770E-08, -7.64830E-09, -5.07940E-09))
TC1LAB .append(-7.23000E-11)
TC1UAB .append(-1.29890E-10)
TC2AC  .append((-2.80390E-10,1.47570E-09,3.16212E-09,4.37677E-09,4.93643E-09,4.68643E-09,3.70051E-09,2.27740E-09,6.76104E-10,-7.58355E-10))
TC2LAB .append(-1.83741E-10)
TC2UAB .append(-2.53500E-10)
TC3AC  .append((-6.48704E-09,2.82884E-09,1.12767E-08,1.73149E-08,2.00477E-08,1.87978E-08,1.39790E-08,7.01204E-09,-8.57388E-10,-8.07072E-09))
TC3LAB .append(-2.26078E-09)
TC3UAB .append(-2.26411E-09)
TCDAC  .append(( -1.03280E-05,-1.10020E-05,-1.39690E-05,-1.64940E-05,-1.77530E-05,-1.71620E-05,-1.48230E-05,-1.15730E-05,-8.28660E-06,-6.50430E-06))
TCDLAB .append(-3.48140E-06)
TCDUAB .append(-1.95700E-06)
TCD2AC .append(( -1.05040E-05,-1.06650E-05,-1.34590E-05,-1.58870E-05,-1.71090E-05,-1.65500E-05,-1.43060E-05,-1.11860E-05,-8.05940E-06,-6.60670E-06) )
TCD2LAB.append(-4.02500E-06)
TCD2UAB.append(-2.22670E-06)

TC1AC  .append(( -4.09430E-08, -5.83230E-08, -7.51680E-08, -8.74980E-08, -9.35550E-08, -9.09140E-08, -7.99660E-08, -6.44940E-08, -4.75330E-08, -3.11060E-08) )
TC1LAB .append(-3.73080E-10)
TC1UAB .append(-8.01530E-10)
TC2AC  .append(( -1.86933E-09,7.31016E-09,1.61645E-08,2.25420E-08,2.54319E-08,2.40259E-08,1.87840E-08,1.13045E-08,2.77309E-09,-4.83093E-09))
TC2LAB .append(-1.00622E-09)
TC2UAB .append(-1.48764E-09)
TC3AC  .append(( -3.90040E-08,8.93536E-09,5.22872E-08,8.32804E-08,9.70312E-08,9.01572E-08,6.52120E-08,2.95820E-08,-1.12134E-08,-4.79332E-08) )
TC3LAB .append(-1.26991E-08)
TC3UAB .append(-1.26904E-08)
TCDAC  .append(( -5.89890E-05,-6.30470E-05,-7.96980E-05,-9.38670E-05,-1.00870E-04,-9.73650E-05,-8.40260E-05,-6.56500E-05,-4.67250E-05,-3.48750E-05) )
TCDLAB .append(-1.98000E-05)
TCDUAB .append(-1.00580E-05)
TCD2AC .append(( -5.99520E-05,-6.12960E-05,-7.70020E-05,-9.06630E-05,-9.74730E-05,-9.41550E-05,-8.13280E-05,-6.36460E-05,-4.55760E-05,-3.53890E-05) )
TCD2LAB.append(-2.29300E-05)
TCD2UAB.append(-1.14060E-05)

TC1AC  .append((-5.25410E-08, -7.49800E-08, -9.65460E-08, -1.12250E-07, -1.19880E-07, -1.16350E-07, -1.02220E-07, -8.22530E-08, -6.09790E-08, -3.97960E-08))
TC1LAB .append(-2.35270E-10)
TC1UAB .append(-1.40110E-09)
TC2AC  .append((-2.45759E-09,7.44861E-09,1.74178E-08,2.46246E-08,2.77485E-08,2.58394E-08,1.96521E-08,1.16208E-08,1.22567E-09,-7.34916E-09))
TC2LAB .append(-1.11460E-09)
TC2UAB .append(-2.37393E-09)
TC3AC  .append((-5.09404E-08,-1.36100E-09,4.55924E-08,7.93156E-08,9.35872E-08,8.47336E-08,5.67224E-08,2.08715E-08,-2.71272E-08,-6.30616E-08))
TC3LAB .append(-1.49999E-08)
TC3UAB .append(-1.64864E-08)
TCDAC  .append((-8.35130E-05,-8.87310E-05,-1.09970E-04,-1.28520E-04,-1.37510E-04,-1.32150E-04,-1.13640E-04,-8.94560E-05,-6.34540E-05,-3.98290E-05))
TCDLAB .append(-2.72010E-05)
TCDUAB .append(-8.79000E-06)
TCD2AC .append(( -8.55700E-05,-8.71590E-05,-1.07150E-04,-1.25120E-04,-1.33940E-04,-1.28830E-04,-1.10920E-04,-8.75210E-05,-6.25050E-05,-4.04190E-05))
TCD2LAB.append(-3.16550E-05)
TCD2UAB.append(-9.74770E-06)

TC1AC  .append((-6.81340E-08,-9.63120E-08,-1.23400E-07,-1.42980E-07,-1.52220E-07,-1.47440E-07,-1.29530E-07,-1.04650E-07,-7.62230E-08,-4.90090E-08))
TC1LAB .append(-4.30750E-10)
TC1UAB .append(-1.80890E-09)
TC2AC  .append((-4.16656E-09,8.30622E-09,2.05081E-08,2.91544E-08,3.26898E-08,2.94742E-08,2.04984E-08,8.93061E-09,-2.25342E-09,-1.04937E-08))
TC2LAB .append(-1.69114E-09)
TC2UAB .append(-2.90550E-09)
TC3AC  .append((-7.21700E-08,-1.04028E-08,4.58724E-08,8.56128E-08,1.02206E-07,8.96616E-08,5.24832E-08,6.23504E-10,-4.95488E-08,-8.28688E-08))
TC3LAB .append(-2.11128E-08)
TC3UAB .append(-2.01541E-08)
TCDAC  .append(( -1.13180E-04,-1.19860E-04,-1.48070E-04,-1.72400E-04,-1.83470E-04,-1.73300E-04,-1.43710E-04,-1.08660E-04,-7.44080E-05,-4.61640E-05))
TCDLAB .append(-3.69240E-05)
TCDUAB .append(-1.03440E-05)
TCD2AC .append(( -1.16370E-04,-1.18090E-04,-1.44750E-04,-1.68430E-04,-1.79390E-04,-1.69670E-04,-1.40960E-04,-1.06900E-04,-7.37430E-05,-4.72230E-05))
TCD2LAB.append(-4.30460E-05)
TCD2UAB.append(-1.15300E-05)

TC1AC  .append((-6.62820E-08,-9.60420E-08,-1.24330E-07,-1.44650E-07,-1.53650E-07,-1.48240E-07,-1.30330E-07,-1.02480E-07,-7.17880E-08,-4.41260E-08))
TC1LAB .append(-6.31450E-10)
TC1UAB .append(-1.46650E-09)
TC2AC  .append(( -6.89832E-09,-7.08376E-10,5.39935E-09,9.31944E-09,1.17273E-08,9.02011E-09,1.33844E-09,-4.71939E-09,-8.26566E-09,-1.07710E-08))
TC2LAB .append(-1.66171E-09)
TC2UAB .append(-2.33493E-09)
TC3AC  .append((-8.14968E-08,-5.68988E-08,-3.54508E-08,-2.22933E-08,-1.01800E-08,-1.33417E-08,-2.39865E-08,-4.23808E-08,-5.89596E-08,-7.01792E-08))
TC3LAB .append(-1.90070E-08)
TC3UAB .append(-1.44654E-08)
TCDAC  .append(( -7.88150E-05,-8.37410E-05,-1.02580E-04,-1.18860E-04,-1.26900E-04,-1.13000E-04,-6.97220E-05,-4.23240E-05,-2.77880E-05,-1.80730E-05))
TCDLAB .append(-2.88690E-05)
TCDUAB .append(-5.84180E-06)
TCD2AC .append((-8.05970E-05,-8.21700E-05,-9.99440E-05,-1.15800E-04,-1.23860E-04,-1.10590E-04,-6.81070E-05,-4.14110E-05,-2.74120E-05,-1.85830E-05))
TCD2LAB.append(-3.39970E-05)
TCD2UAB.append(-6.58490E-06)

TC1AC  .append((-6.54220E-08,-9.47640E-08,-1.22550E-07,-1.41510E-07,-1.46970E-07,-1.37990E-07,-1.12720E-07,-8.14570E-08,-5.53970E-08,-3.36750E-08))
TC1LAB .append(-1.11150E-09)
TC1UAB .append(-7.86540E-10)
TC2AC  .append((-1.31894E-08,-1.41143E-08,-1.43619E-08,-1.46642E-08,-1.42763E-08,-1.42559E-08,-1.04986E-08,-6.21367E-09,-6.35271E-09,-6.72964E-09))
TC2LAB .append(-2.30841E-09)
TC2UAB .append(-1.30874E-09)
TC3AC  .append((-1.22777E-07,-1.46107E-07,-1.66642E-07,-1.80734E-07,-1.79528E-07,-1.63738E-07,-1.03404E-07,-5.54988E-08,-4.91792E-08,-4.66368E-08))
TC3LAB .append(-2.29183E-08)
TC3UAB .append(-8.61896E-09)
TCDAC  .append(( -9.11750E-05,-1.08190E-04,-1.34260E-04,-1.54020E-04,-1.59290E-04,-1.39290E-04,-8.91090E-05,-5.58620E-05,-3.66230E-05,-2.21180E-05))
TCDLAB .append(-2.99330E-05)
TCDUAB .append(-6.34030E-06)
TCD2AC .append((-9.55360E-05,-1.10750E-04,-1.36960E-04,-1.57180E-04,-1.62920E-04,-1.43180E-04,-9.25980E-05,-5.86300E-05,-3.87230E-05,-2.39510E-05))
TCD2LAB.append(-3.61050E-05)
TCD2UAB.append(-7.58020E-06)

gemW = ( (-4.9759601E-03,-4.9759601E-03,-4.9727950E-03,-4.9465660E-03,
     -4.8999230E-03,-4.8770560E-03,-4.5790760E-03,
     -4.5042170E-03,-4.0803270E-03,-3.6035070E-03,
     -3.1068070E-03,-2.6024970E-03,-2.0963570E-03,
     -1.6033470E-03,-1.1575970E-03,-7.7857700E-04,
     -4.5669700E-04,-2.0180700E-04,-1.6020400E-04,
    -2.3214000E-05,-5.4510000E-06,0.0000000E+00) )
     
gemh = ( (0.0,25.520,37.250,52.770,62.410,65.270,79.860,81.910,
     91.138,100.366,109.594,118.822,128.050,137.278,146.506,
    155.734,164.962,174.190,176.240,189.540,199.780,207.350) )
