
import time
import random

def wainting_game():
    target = random.randint(2,4) #target second to  wait
    print(" Your target tilme is {}second".format(target))

    input("--- Press enter to begin --")
    start = time.perf_counter()

    input('\n press enter after {} second'.format(target))
    elapsed = time.perf_counter()-start

    print("\n elapsed time :{0:.3f} second ".format(target))
    if elapsed == target :
        print("Perfect timing !")
    elif (target> elapsed) :
        print(" {0:.3f} second too fast ".format(target - elapsed ))
    else :
        print(" {0:.3f} second too slo ".format( elapsed-target  ))
        
    
wainting_game()    
