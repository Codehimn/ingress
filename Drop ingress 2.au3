#include <Constants.au3>



; adb shell
; am startservice --ez no_history true --ei lat 41307258 --ei long 2002908 -n com.lexa.fakegpsdonate/.FakeGPSService ; am force-stop com.lexa.fakegpsdonate ;Barcelona
; am startservice --ez no_history true --ei lat 41492162 --ei long 2153385 -n com.lexa.fakegpsdonate/.FakeGPSService ; am force-stop com.lexa.fakegpsdonate ; Barcelona2
; am startservice --ez no_history true --ei lat 39580450 --ei long 2657550 -n com.lexa.fakegpsdonate/.FakeGPSService ; am force-stop com.lexa.fakegpsdonate ;calle caro
; am startservice --ez no_history true --ei lat 39588515 --ei long 2634927 -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.4; am force-stop com.lexa.fakegpsdonate ;Caasa dani
; am force-stop com.lexa.fakegpsdonate
; getevent -lp /dev/input/event1

; MouseClickDrag("left",1450, 945,1535, 945,1)


;am startservice --ez no_history true --ei lat 39571583 --ei long 2669035 -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.4; am force-stop com.lexa.fakegpsdonate ;casa Grace;
; am startservice --ez no_history true --ei lat 39583947 --ei long 2657041 -n com.lexa.fakegpsdonate/.FakeGPSService ;sleep 0.4; am force-stop com.lexa.fakegpsdonate ;casa Gabor

; Exit


; 	$str_hack = "function drop() { " &
; 	$str_hack = $str_hack & "input tap 1000 150;"
; 	$str_hack = $str_hack & "input tap " & $XCord & " " & $YCord & ";"
; 	$str_hack = $str_hack & "input tap 550 1550;"
; 	$str_hack = $str_hack & "busybox sleep 0.4; }" & @CRLF


; DropItems_bluestack("U8", 60, 'recicle')
; DropItems_bluestack("U8", 400,'drop',1);llaves


; DropItems_bluestack("U8", 50)

; X10 = Shield

; DropItems_bluestack("X10", 50)
; DropItems_bluestack("R1", 50)
; DropItems_bluestack("R2", 10)
; DropItems_bluestack("R3", 10)
; DropItems_bluestack("R4", 10)
; DropItems_bluestack("X1", 60)
; DropItems_bluestack("X2", 60)
; DropItems_bluestack("X3", 40)
; DropItems_bluestack("X4", 40)

; DropItems_bluestack("C1", 40)
; DropItems_bluestack("C2", 5)
; DropItems_bluestack("C3", 5)
; DropItems_bluestack("C4", 5)




; DropItems_bluestack("R1", 11, 'recicle')
; DropItems_bluestack("R2", 10, 'recicle')
; DropItems_bluestack("R3", 10, 'recicle')
; DropItems_bluestack("R4", 25, 'recicle')
; DropItems_bluestack("R5", 115, 'recicle')


; DropItems_bluestack("X8", 200,0)
; Up_Items_bluestacks(50)
; reciclar_bluestacks(73)

; exit


Func DropItems_bluestack($item, $cant = 1, $accion = 'drop',$key_or_normal = 0) ;1 = KEY
	$XCord = 28380 + 750
	$YCord = 6575 - 5650

	$i_esp = 0
	For $lvl = 1 To 17
		If StringInStr($item, $lvl) Then $XCord = $XCord - ($lvl * 750)
	Next

	If StringInStr($item, "R") Then $YCord = $YCord + (5650)
	If StringInStr($item, "X") Then $YCord = $YCord + (5650 * 2)
	If StringInStr($item, "U") Then $YCord = $YCord + (5650 * 3)
	If StringInStr($item, "C") Then $YCord = $YCord + (5650 * 4)
	If StringInStr($item, "M") Then $YCord = $YCord + (5650 * 5)

	For $i = 1 To $cant
		$i_esp = $i_esp + 1
		If $i_esp > 10 and $accion = 'drop' Then
			Sleep(4500)
			$i_esp = 0
			$cant = $cant - 10
		EndIf

		; 		touch_x_y(31051, 30481) ;OPS
		touch_x_y(31228, 31021) ;OPS
		Sleep(600)

		touch_x_y($XCord, $YCord) ;ITEM
		Sleep(800)

if $accion = 'drop'  then
		If $key_or_normal Then
			Sleep(1200)
			touch_x_y(5637, 16321);Llave
			Sleep(3200)
		Else
			; touch_x_y(3343, 16820);Otros
			touch_x_y(3050,	23921);Drop
			Sleep(500)
		EndIf
endif

if $accion = 'recicle' then
		If $key_or_normal Then
			touch_x_y(5637, 16296);Llave
			Sleep(3200)
		Else
			; touch_x_y(3343, 16820);Otros
			touch_x_y(3050,	28925);Drop
			Sleep(500)
			Sleep(1500) ; normal client ingress
		EndIf
endif




	Next
EndFunc   ;==>DropItems_bluestack


Func Up_Items_bluestacks($cant = 1)
	For $i = 1 To $cant
		touch_x_y(10355, 17635)
		Sleep(300)
		; touch_x_y(5500, 17635);llave
		; touch_x_y(9000, 17635)
		; touch_x_y(3670, 17635)
		touch_x_y(3690, 17635)
		Sleep(2000)
	Next

EndFunc   ;==>Up_Items_bluestacks




Func touch_x_y($X_mouse, $Y_mouse)

	cworsend2("sendevent /dev/input/event1 3 0 " & $X_mouse)
	cworsend2("sendevent /dev/input/event1 3 1 " & $Y_mouse)
	cworsend2("sendevent /dev/input/event1 1 272 1")
	cworsend2("sendevent /dev/input/event1 0 0 0")
	cworsend2("sendevent /dev/input/event1 1 272 0")
	cworsend2("sendevent /dev/input/event1 0 0 0")

EndFunc   ;==>touch_x_y

Func cworsend2($var)
	;    Send($var)
	StdinWrite($pid, $var & @CRLF)
EndFunc   ;==>cworsend2

Func reciclar_bluestacks($veces, $key_or_normal = 0)
	For $i = 1 To $veces
		
		If $key_or_normal = 0 Then
			touch_x_y(25920, 12397)
			Sleep(800)
			touch_x_y(3277, 26714)
			Sleep(600)
		Else
			touch_x_y(31228, 31021) ;OPS
			Sleep(1000)
			touch_x_y(18710, 16470);lLAVE
			Sleep(1000)
			touch_x_y(5015, 30750) ;Recycle
			Sleep(1000)
			touch_x_y(13239, 8846) ;Confirm
			Sleep(1000)
		EndIf
	Next
EndFunc   ;==>reciclar_bluestacks
