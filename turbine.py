# Turbine Model - Hefni Test-Case 10.2.5

circuit1 = comp.Circuit("circuit1")
circuit1.assign_fluid("water","CoolProp")

circuit1.add_node("node1")
circuit1.add_node("node2")

circuit1.add_turbine("turbine1","node1","node2",Cst=2E6,eata_is=0.94)

circuit1.add_BC("bc1","node1",'P',270.E5)
circuit1.add_BC("bc2","node1",'T',873.1711267378283)
circuit1.add_BC("bc3","node2",'P',100.E5)
