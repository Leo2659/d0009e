def recept(antal):
    print("Ägg: ", round(3/4*antal), " st")
    print("Ströbröd: ", round(3/4*antal), " dl")
    print("Vaniljsocker ", round(1/2*antal), " tsk")
    print("Bakpulver: ", round(1/2*antal), " tsk")
    print("Vetemjöl: ", round(3/4*antal), " dl")
    print("Smör: " , round(75/4*antal)," g")
    print("Vatten: ", round(1/4*antal) ," dl")

def tidblanda(antal):
    tid = 10 + antal
    return tid

def tidgrädda(antal):
    tid = 30 + antal*3
    return tid

def sockerkaka(antal):
    tid = tidgrädda(antal) + tidgrädda(antal) 
    timmar = tid/60
    print("Sockerkaka för ", antal, " personer:")
    print()
    recept(antal)
    print()
    print("Tidsåtgång: ", timmar, " timmar" + "\n")

sockerkaka(4)
sockerkaka(7)
