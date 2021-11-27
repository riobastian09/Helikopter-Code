import curses
from time import sleep

def helikopter_kanan1():
    stdscr.addstr(0, 0,"")
    stdscr.addstr(1, 0,"")
    stdscr.addstr(2, 0,"           .  -  --  == <0>=================")
    stdscr.addstr(3, 0,"                         |")
    stdscr.addstr(4, 0,"                     ___|||___________ ")
    stdscr.addstr(5, 0,"  / '|  \       /===/     /    _  _   \ ")
    stdscr.addstr(6, 0," (- <0> -)=========(     /  [ U ][ U ] \ ")
    stdscr.addstr(7, 0,"  \  |' /      \____\   |  ==    w   == ) ")
    stdscr.addstr(8, 0,"                     \___\_____________/")
    stdscr.addstr(9, 0,"                        ||      ||")
    stdscr.addstr(10, 0,"                   [____/\______/\____] ")
    stdscr.addstr(11, 0,"")
    stdscr.addstr(12, 0,"")
    
def helikopter_kanan2():
    stdscr.addstr(0, 0,"")
    stdscr.addstr(1, 0,"")
    stdscr.addstr(2, 0,"           .  -  --  == <0>=================")
    stdscr.addstr(3, 0,"                         |")
    stdscr.addstr(4, 0,"                     ___|||___________ ")
    stdscr.addstr(5, 0,"  / '|  \       /===/     /  ___  ___ \ ")
    stdscr.addstr(6, 0," (- <0> -)=========(     /  [ O ][ O ] \ ")
    stdscr.addstr(7, 0,"  \  |' /      \____\   |   =   __   =  ) ")
    stdscr.addstr(8, 0,"                     \___\_____________/")
    stdscr.addstr(9, 0,"                        ||      ||")
    stdscr.addstr(10, 0,"                   [____/\______/\____] ")
    stdscr.addstr(11, 0,"")
    stdscr.addstr(12, 0,"")

def helikopter_kanan3():
    stdscr.addstr(0, 0,"")
    stdscr.addstr(1, 0,"")
    stdscr.addstr(2, 0,"           .  -  --  == <0>=================")
    stdscr.addstr(3, 0,"                         |")
    stdscr.addstr(4, 0,"                     ___|||___________ ")
    stdscr.addstr(5, 0,"  / '|  \       /===/     /   \_  _/  \ ")
    stdscr.addstr(6, 0," (- <0> -)=========(     /  [ > ][ < ] \ ")
    stdscr.addstr(7, 0,"  \  |' /      \____\   |  ===   ^  === ) ")
    stdscr.addstr(8, 0,"                     \___\_____________/")
    stdscr.addstr(9, 0,"                        ||      ||")
    stdscr.addstr(10, 0,"                   [____/\______/\____] ")
    stdscr.addstr(11, 0,"")
    stdscr.addstr(12, 0,"")
    
def helikopter_kiri1():
    stdscr.addstr(0, 0,"")
    stdscr.addstr(1, 0,"")
    stdscr.addstr(2, 0,"       =================<0> ==  --  -  .    ")
    stdscr.addstr(3, 0,"                         |")
    stdscr.addstr(4, 0,"                     ___|||___________ ")
    stdscr.addstr(5, 0,"  /  '''\       /===/     /  ___  ___ \ ")
    stdscr.addstr(6, 0," (==<0>==)=========(     /  [ O ][ O ] \ ")
    stdscr.addstr(7, 0,"  \ ''  /      \____\   |   =   __   =  ) ")
    stdscr.addstr(8, 0,"                     \___\_____________/")
    stdscr.addstr(9, 0,"                        ||      ||")
    stdscr.addstr(10, 0,"                   [____/\______/\____] ")
    stdscr.addstr(11, 0,"")
    stdscr.addstr(12, 0,"")
    
def helikopter_kiri2():
    stdscr.addstr(0, 0,"")
    stdscr.addstr(1, 0,"")
    stdscr.addstr(2, 0,"       =================<0> ==  --  -  .    ")
    stdscr.addstr(3, 0,"                         |")
    stdscr.addstr(4, 0,"                     ___|||___________ ")
    stdscr.addstr(5, 0,"  /  '''\       /===/     /    _  _   \ ")
    stdscr.addstr(6, 0," (==<0>==)=========(     /  [ U ][ U ] \ ")
    stdscr.addstr(7, 0,"  \ ''  /      \____\   |  ==    w   == ) ")
    stdscr.addstr(8, 0,"                     \___\_____________/")
    stdscr.addstr(9, 0,"                        ||      ||")
    stdscr.addstr(10, 0,"                   [____/\______/\____] ")
    stdscr.addstr(11, 0,"")
    stdscr.addstr(12, 0,"")

def helikopter_kiri3():
    stdscr.addstr(0, 0,"")
    stdscr.addstr(1, 0,"")
    stdscr.addstr(2, 0,"       =================<0> ==  --  -  .    ")
    stdscr.addstr(3, 0,"                         |")
    stdscr.addstr(4, 0,"                     ___|||___________ ")
    stdscr.addstr(5, 0,"  /  '''\       /===/     /   \_  _/  \ ")
    stdscr.addstr(6, 0," (==<0>==)=========(     /  [ > ][ < ] \ ")
    stdscr.addstr(7, 0,"  \ ''  /      \____\   |  ===   ^  === ) ")
    stdscr.addstr(8, 0,"                     \___\_____________/")
    stdscr.addstr(9, 0,"                        ||      ||")
    stdscr.addstr(10, 0,"                   [____/\______/\____] ")
    stdscr.addstr(11, 0,"")
    stdscr.addstr(12, 0,"")
    
def helikopter_tengahA1():
    stdscr.addstr(0, 0,"")
    stdscr.addstr(1, 0,"")
    stdscr.addstr(2, 0,"           .  -  --  == <0> ==  --  -  .    ")
    stdscr.addstr(3, 0,"                         |")
    stdscr.addstr(4, 0,"                     ___|||___________ ")
    stdscr.addstr(5, 0,"  /'\ ' \       /===/     /  ___  ___ \ ")
    stdscr.addstr(6, 0," (- <0> -)=========(     /  [ O ][ O ] \ ")
    stdscr.addstr(7, 0,"  \ ''\ /      \____\   |   =   __   =  ) ")
    stdscr.addstr(8, 0,"                     \___\_____________/")
    stdscr.addstr(9, 0,"                        ||      ||")
    stdscr.addstr(10, 0,"                   [____/\______/\____] ")
    stdscr.addstr(11, 0,"")
    stdscr.addstr(12, 0,"")

def helikopter_tengahA2():
    stdscr.addstr(0, 0,"")
    stdscr.addstr(1, 0,"")
    stdscr.addstr(2, 0,"           .  -  --  == <0> ==  --  -  .    ")
    stdscr.addstr(3, 0,"                         |")
    stdscr.addstr(4, 0,"                     ___|||___________ ")
    stdscr.addstr(5, 0,"  /'\ ' \       /===/     /    _  _   \ ")
    stdscr.addstr(6, 0," (- <0> -)=========(     /  [ U ][ U ] \ ")
    stdscr.addstr(7, 0,"  \ ''\ /      \____\   |  ==    w   == ) ")
    stdscr.addstr(8, 0,"                     \___\_____________/")
    stdscr.addstr(9, 0,"                        ||      ||")
    stdscr.addstr(10, 0,"                   [____/\______/\____] ")
    stdscr.addstr(11, 0,"")
    stdscr.addstr(12, 0,"")

def helikopter_tengahA3():
    stdscr.addstr(0, 0,"")
    stdscr.addstr(1, 0,"")
    stdscr.addstr(2, 0,"           .  -  --  == <0> ==  --  -  .    ")
    stdscr.addstr(3, 0,"                         |")
    stdscr.addstr(4, 0,"                     ___|||___________ ")
    stdscr.addstr(5, 0,"  /'\ ' \       /===/     /   \_  _/  \ ")
    stdscr.addstr(6, 0," (- <0> -)=========(     /  [ > ][ < ] \ ")
    stdscr.addstr(7, 0,"  \ ''\ /      \____\   |  ===   ^  === ) ")
    stdscr.addstr(8, 0,"                     \___\_____________/")
    stdscr.addstr(9, 0,"                        ||      ||")
    stdscr.addstr(10, 0,"                   [____/\______/\____] ")
    stdscr.addstr(11, 0,"")
    stdscr.addstr(12, 0,"")

def helikopter_tengahB1():
    stdscr.addstr(0, 0,"")
    stdscr.addstr(1, 0,"")
    stdscr.addstr(2, 0,"           .  -  --  == <0> ==  --  -  .    ")
    stdscr.addstr(3, 0,"                         |")
    stdscr.addstr(4, 0,"                     ___|||___________ ")
    stdscr.addstr(5, 0,"  / ''/'\       /===/     /    _  _   \ ")
    stdscr.addstr(6, 0," (- <0> -)=========(     /  [ U ][ U ] \ ")
    stdscr.addstr(7, 0,"  \ /'' /      \____\   |  ==    w   == ) ")
    stdscr.addstr(8, 0,"                     \___\_____________/")
    stdscr.addstr(9, 0,"                        ||      ||")
    stdscr.addstr(10, 0,"                   [____/\______/\____] ")
    stdscr.addstr(11, 0,"")
    stdscr.addstr(12, 0,"")

def helikopter_tengahB2():
    stdscr.addstr(0, 0,"")
    stdscr.addstr(1, 0,"")
    stdscr.addstr(2, 0,"           .  -  --  == <0> ==  --  -  .    ")
    stdscr.addstr(3, 0,"                         |")
    stdscr.addstr(4, 0,"                     ___|||___________ ")
    stdscr.addstr(5, 0,"  / ''/'\       /===/     /  ___  ___ \ ")
    stdscr.addstr(6, 0," (- <0> -)=========(     /  [ O ][ O ] \ ")
    stdscr.addstr(7, 0,"  \ /'' /      \____\   |   =   __   =  ) ")
    stdscr.addstr(8, 0,"                     \___\_____________/")
    stdscr.addstr(9, 0,"                        ||      ||")
    stdscr.addstr(10, 0,"                   [____/\______/\____] ")
    stdscr.addstr(11, 0,"")
    stdscr.addstr(12, 0,"")

def helikopter_tengahB3():
    stdscr.addstr(0, 0,"")
    stdscr.addstr(1, 0,"")
    stdscr.addstr(2, 0,"           .  -  --  == <0> ==  --  -  .    ")
    stdscr.addstr(3, 0,"                         |")
    stdscr.addstr(4, 0,"                     ___|||___________ ")
    stdscr.addstr(5, 0,"  / ''/'\       /===/     /   \_  _/  \ ")
    stdscr.addstr(6, 0," (- <0> -)=========(     /  [ > ][ < ] \ ")
    stdscr.addstr(7, 0,"  \ /'' /      \____\   |  ===   ^  === ) ")
    stdscr.addstr(8, 0,"                     \___\_____________/")
    stdscr.addstr(9, 0,"                        ||      ||")
    stdscr.addstr(10, 0,"                   [____/\______/\____] ")
    stdscr.addstr(11, 0,"")
    stdscr.addstr(12, 0,"")
    
if __name__ == "__main__":
    stdscr = curses.initscr()        
    while True:
        helikopter_kanan1()
        sleep(.15)
        stdscr.refresh()
        helikopter_tengahB1()
        sleep(.15)
        stdscr.refresh()
        helikopter_kiri2()
        sleep(.15)
        stdscr.refresh() #satu
        helikopter_tengahA3()
        sleep(.15)
        stdscr.refresh()
        helikopter_kanan3()
        sleep(.15)
        stdscr.refresh()
        helikopter_tengahB3()
        sleep(.15)
        stdscr.refresh() #dua
        helikopter_kiri2()
        sleep(.15)
        stdscr.refresh()
        helikopter_tengahA2()
        sleep(.15)
        stdscr.refresh()
        helikopter_kanan1()
        sleep(.15)
        stdscr.refresh() #tiga
        helikopter_tengahB2()
        sleep(.15)
        stdscr.refresh()
        helikopter_kiri1()
        sleep(.15)
        stdscr.refresh()
        helikopter_tengahA1() #empat
        sleep(.15)
        stdscr.refresh()