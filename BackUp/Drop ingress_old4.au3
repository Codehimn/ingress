
#include <Constants.au3>

$XCord = 550
$YCord = 850
$cant = 100

$cada_x_veces = 1


;~ adb shell
;~ am startservice --ei lat 41307258 --ei long 2002908 -n com.lexa.fakegpsdonate/.FakeGPSService ;Barcelona
;~ am startservice --ei lat 41492162 --ei long 2153385 -n com.lexa.fakegpsdonate/.FakeGPSService ; am force-stop com.lexa.fakegpsdonate ; Barcelona2
;~ am startservice --ei lat 39580450 --ei long 2657550 -n com.lexa.fakegpsdonate/.FakeGPSService ;calle caro
;~ am force-stop com.lexa.fakegpsdonate
;~ adb shell getevent -lp /dev/input/event1

;~ MouseClickDrag("left",1450, 945,1535, 945,1)


;~ Exit


;~ 	$str_hack = "function drop() { " &
;~ 	$str_hack = $str_hack & "input tap 1000 150;"
;~ 	$str_hack = $str_hack & "input tap " & $XCord & " " & $YCord & ";"
;~ 	$str_hack = $str_hack & "input tap 550 1550;"
;~ 	$str_hack = $str_hack & "busybox sleep 0.4; }" & @CRLF


;~ ConsoleWrite($str_hack)
;~ ConsoleWrite("x=0 ; while [ $x -lt " & $cant & " ]; do $(drop); (( x++ )); done" & @CRLF)


;~ DropItems("R1", 46)
;~ DropItems("X1", 41)
;~ DropItems("R2", 37)
;~ DropItems("X2", 132)
;~ DropItems("R3", 59)
;~ DropItems("X3", 100)
;~ DropItems("R5", 80)
;~ DropItems("X5", 30)
;~ DropItems("R6", 10)
;~ DropItems("X6", 20)
;~ DropItems("R7", 80)
;~ DropItems("X7", 200)
;~ DropItems("R8", 10)
;~ DropItems("R8", 50)

;~ DropItems(0, 2, 1);Dropear llaves

;~ Up_Items(100)

$pid = Run("C:\Users\Codehimn\Dropbox\ingress\adb shell", "", @SW_SHOW, $STDIN_CHILD + $STDOUT_CHILD)
cworsend2("su")



;~ DropItems_bluestack(1, 80,0)
;~ Up_Items_bluestacks(200)
reciclar(8)


;~ x=0 ; while [ $x -lt 100 ]; do input tap 1000 150; input tap 550 850; input tap 550 1550; (( x++ )); done

ConsoleWrite("input keyevent 26" & @CRLF & @CRLF)

Func DropItems($item = 1, $cant = 1, $key_or_normal = 0) ;1 = KEY

	For $lvl = 1 To 8
		If StringInStr($item, $lvl) Then $YCord = 460 + ($lvl * 110)
	Next


	$str_hack = "function drop() { " & @CRLF
	$str_hack = $str_hack & "input tap 1000 150;"
	$str_hack = $str_hack & "input tap " & $XCord & " " & $YCord & ";"
;~ 	$str_hack = $str_hack & "input tap 550 1550;" ;
	$str_hack = $str_hack & "input tap 550 " & $key_or_normal & ";" ; Normal or Key drop
	$str_hack = $str_hack & "busybox sleep 0.4; }" & @CRLF

	ConsoleWrite($str_hack)
	For $i = 1 To $cant / $cada_x_veces
		ConsoleWrite("x=0 ; while [ $x -lt " & $cada_x_veces & " ]; do $(drop); (( x++ )); done" & @CRLF)
	Next
	If Mod($cant, $cada_x_veces) > 0 Then ConsoleWrite("x=0 ; while [ $x -lt " & Mod($cant, $cada_x_veces) & " ]; do $(drop); (( x++ )); done" & @CRLF)

EndFunc   ;==>DropItems


Func DropItems_bluestack($item, $cant = 1, $key_or_normal = 0) ;1 = KEY

	$LV = 3
	For $i = 1 To $cant
		touch_x_y(31851, 30381)
		Sleep(1500)
		touch_x_y(18875, 16762)
		Sleep(200)
		If $key_or_normal Then
;~ 		touch_x_y(5637,16296);Llave
		Else
			touch_x_y(3343, 16820);Otros
		EndIf
		Sleep(3200)

	Next
EndFunc   ;==>DropItems_bluestack

Func Up_Items($cant = 1)
	For $i = 1 To $cant / $cada_x_veces
		ConsoleWrite("x=0 ; while [ $x -lt " & $cada_x_veces & " ]; do input tap 545 1230; input tap 545 1350; busybox sleep 0.9; (( x++ )); done" & @CRLF)
	Next
	If Mod($cant, $cada_x_veces) > 0 Then ConsoleWrite("x=0 ; while [ $x -lt " & Mod($cant, $cada_x_veces) & " ]; do input tap 545 1230; input tap 545 1350; busybox sleep 0.9; (( x++ )); done" & @CRLF)

EndFunc   ;==>Up_Items

Func Up_Items_bluestacks($cant = 1)
	For $i = 1 To $cant / $cada_x_veces
		touch_x_y(10355, 17635)
		Sleep(200)
;~ 		touch_x_y(4817,17518);llave
		touch_x_y(6063, 16529)
		Sleep(1500)
	Next

EndFunc   ;==>Up_Items_bluestacks




Func touch_x_y($X_mouse, $Y_mouse)

	cworsend2("sendevent /dev/input/event1 3 0 " & $X_mouse)
	cworsend2("sendevent /dev/input/event1 3 1 " & $Y_mouse)
	cworsend2("sendevent /dev/input/event1 0 0 0")
	cworsend2("sendevent /dev/input/event1 0 0 0")
	cworsend2("sendevent /dev/input/event1 1 272 1")
	cworsend2("sendevent /dev/input/event1 0 0 0")
	cworsend2("sendevent /dev/input/event1 1 272 0")
	cworsend2("sendevent /dev/input/event1 0 0 0")

EndFunc   ;==>touch_x_y

Func cworsend2($var)
;~    Send($var)
	StdinWrite($pid, $var & @CRLF)
EndFunc   ;==>cworsend2


Func reciclar($veces)
	For $i =1 to $veces
	touch_x_y(28345, 12397)
	touch_x_y(3277, 26714)
	Sleep(800)
	Next
EndFunc