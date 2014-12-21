$XCord = 550
$YCord = 850
$cant = 100

$cada_x_veces = 10


;~ adb shell
am startservice --ei lat 39580450 --ei long 2657550 -n com.lexa.fakegpsdonate/.FakeGPSService
am force-stop com.lexa.fakegpsdonate


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

;~ DropItems(0,1, 1);Dropear llaves

;~ Up_Items(100)


DropItems_bluestack(1, 50)


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
		MouseClick("left", 1875, 64)
;~ 		MouseClick("left", 1463, 145 + $LV * 22)
MouseClick("left",1764, 266)

		MouseClick("left", 1636, 937)
		Sleep(200)
	Next
EndFunc   ;==>DropItemsDropItems_bluestack

Func Up_Items($cant = 1)
	For $i = 1 To $cant / $cada_x_veces
		ConsoleWrite("x=0 ; while [ $x -lt " & $cada_x_veces & " ]; do input tap 545 1230; input tap 545 1350; busybox sleep 0.9; (( x++ )); done" & @CRLF)
	Next
	If Mod($cant, $cada_x_veces) > 0 Then ConsoleWrite("x=0 ; while [ $x -lt " & Mod($cant, $cada_x_veces) & " ]; do input tap 545 1230; input tap 545 1350; busybox sleep 0.9; (( x++ )); done" & @CRLF)

EndFunc   ;==>Up_Items
