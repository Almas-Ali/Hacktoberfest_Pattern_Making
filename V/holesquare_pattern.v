import os
mut side := 5
if os.args.len > 1{
	side = os.args[1].int()
}

for i in 0 .. side{
    for j in 0 .. side{
        if i == 0 || i == side - 1 || j == 0 || j == side - 1{
            print(' * ')
        }
        else{
            print('   ')
	    }
    }
    println("")
}
