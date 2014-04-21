#include <Constants.au3>



# adb shell
# am startservice --ez no_history true --ei lat 41307258 --ei long 2002908 -n com.lexa.fakegpsdonate/.FakeGPSService # am force-stop com.lexa.fakegpsdonate ;Barcelona
# am startservice --ez no_history true --ei lat 41492162 --ei long 2153385 -n com.lexa.fakegpsdonate/.FakeGPSService # am force-stop com.lexa.fakegpsdonate # Barcelona2
# am startservice --ez no_history true --ei lat 39580450 --ei long 2657550 -n com.lexa.fakegpsdonate/.FakeGPSService # am force-stop com.lexa.fakegpsdonate ;calle caro
# am startservice --ez no_history true --ei lat 39588515 --ei long 2634927 -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.4# am force-stop com.lexa.fakegpsdonate ;Caasa dani
# am force-stop com.lexa.fakegpsdonate
# getevent -lp /dev/input/event1

# MouseClickDrag("left",1450, 945,1535, 945,1)


# am startservice --ez no_history true --ei lat 39571583 --ei long 2669035 -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.4# am force-stop com.lexa.fakegpsdonate ;casa Grace;
# am startservice --ez no_history true --ei lat 39583947 --ei long 2657041 -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.4# am force-stop com.lexa.fakegpsdonate ;casa Gabor

# Exit


# 	str_hack = "deftion drop() { " +
# 	str_hack = str_hack + "input tap 1000 150;"
# 	str_hack = str_hack + "input tap " + XCord + " " + YCord + ";"
# 	str_hack = str_hack + "input tap 550 1550;"
# 	str_hack = str_hack + "busybox sleep 0.4# }" + @CRLF


# if WinExists(@ScriptDir + "\adb.exe") : WinClose(@ScriptDir + "\adb.exe")



# DropItems_bluestack("U8", 50)


# DropItems_bluestack("X10", 50)
# DropItems_bluestack("R1", 50)
# DropItems_bluestack("R2", 10)
# DropItems_bluestack("R3", 10)
# DropItems_bluestack("R4", 10)
# DropItems_bluestack("X1", 60)
# DropItems_bluestack("X2", 60)
# DropItems_bluestack("X3", 40)
# DropItems_bluestack("X4", 40)

# DropItems_bluestack("C1", 40)
# DropItems_bluestack("C2", 5)
# DropItems_bluestack("C3", 5)
# DropItems_bluestack("C4", 5)

# DropItems_bluestack("R1", 11, 'recicle')
# DropItems_bluestack("R2", 10, 'recicle')
# DropItems_bluestack("R3", 10, 'recicle')
# DropItems_bluestack("R4", 25, 'recicle')
# DropItems_bluestack("R5", 115, 'recicle')






DropItems_bluestack("U8", 400,'drop',1) #llaves
exit(0)