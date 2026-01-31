import angr

'''
These addresses can be found in radare2 through "afl" to find
the symbol for main and "axt @ str.ok_________Well_done_:_D" to
find the XREF for the string.
'''
main = 0x400686
string_xref = 0x40078c

#This is a perfect problem for angr to solve!
p = angr.Project('uck')

state = p.factory.entry_state(addr=main)
simgr = p.factory.simgr(state)

#0x40078c is the XREF for "[ + ok  ]" as mov edi, str.ok______Well_done
'''
By using the default angr exploratrion technique we can explore all 81
possible paths automatically and have angr find one to get to this location
'''
simgr.explore(find=string_xref)

found = simgr.found[0]

#This is angr's way of dumping a solved output from the constrianed file descriptor.
soln = found.state.posix.dumps(0) #0 is the the file descriptor for STDIN

assert(soln == '3735928559')
