# GER Modeling

circuit1 = comp.Circuit("circuit1")
circuit1.assign_fluid("water","CoolProp")

circuit1.add_node("node1")
circuit1.add_node("node2")

circuit1.add_ger("GER1","node1","node2",Ck=2E6,m=2,n=2)

circuit1.add_BC("bc1","node1",'P',20.E5)
circuit1.add_BC("bc2","node1",'T',300.0)
circuit1.add_BC("bc3","node2",'P',10.E5)
