import angr, claripy
p = angr.Project('./madorbad', auto_load_libs=False)

argv=claripy.BVS('argv', 0x3a * 8)
state = p.factory.entry_state(args=['./madorbad', argv])

simgr = p.factory.simgr(state, threads= 20)

simgr = simgr.explore(find=0x400fe0, avoid=(0x4010ca))
try:
    print simgr
    flag = simgr.found[0]
    flag = flag.solver.eval(argv, cast_to=str)
    print "The flag is: {}".format(flag.strip())
except:
    print "well ... fuck"


