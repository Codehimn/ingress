#include <Constants.au3>



; adb shell
; am startservice --ez no_history true --ei lat 41307258 --ei long 2002908 -n com.lexa.fakegpsdonate/.FakeGPSService ; am force-stop com.lexa.fakegpsdonate ;Barcelona
; am startservice --ez no_history true --ei lat 41492162 --ei long 2153385 -n com.lexa.fakegpsdonate/.FakeGPSService ; am force-stop com.lexa.fakegpsdonate ; Barcelona2
; am startservice --ez no_history true --ei lat 39580450 --ei long 2657550 -n com.lexa.fakegpsdonate/.FakeGPSService ; am force-stop com.lexa.fakegpsdonate ;calle caro
; am force-stop com.lexa.fakegpsdonate
; getevent -lp /dev/input/event1

; MouseClickDrag("left",1450, 945,1535, 945,1)



; Exit


; 	$str_hack = "function drop() { " &
; 	$str_hack = $str_hack & "input tap 1000 150;"
; 	$str_hack = $str_hack & "input tap " & $XCord & " " & $YCord & ";"
; 	$str_hack = $str_hack & "input tap 550 1550;"
; 	$str_hack = $str_hack & "busybox sleep 0.4; }" & @CRLF


If WinExists("C:\Users\Codehimn\Dropbox\ingress\adb.exe") Then WinClose("C:\Users\Codehimn\Dropbox\ingress\adb.exe")
$pid = Run("C:\Users\Codehimn\Dropbox\ingress\adb shell", "", @SW_SHOW, $STDIN_CHILD + $STDOUT_CHILD)
cworsend2("su")



; DropItems_bluestack("R7", 1, 0)
; Up_Items_bluestacks(250)
; reciclar_bluestacks(121)


Func DropItems_bluestack($item, $cant = 1, $key_or_normal = 0) ;1 = KEY
	$XCord = 28380 + 750
	$YCord = 6575 - 5650

	$i_esp = 0
	For $lvl = 1 To 8
		If StringInStr($item, $lvl) Then $XCord = $XCord - ($lvl * 750)
	Next

	If StringInStr($item, "R") Then $YCord = $YCord + (5650)
	If StringInStr($item, "X") Then $YCord = $YCord + (5650 * 2)
	If StringInStr($item, "C") Then $YCord = $YCord + (5650 * 4)
	If StringInStr($item, "M") Then $YCord = $YCord + (5650 * 5)

	For $i = 1 To $cant
		$i_esp = $i_esp + 1
		If $i_esp > 10 Then
			Sleep(4500)
			$i_esp = 0
			$cant = $cant - 10
		EndIf

; 		touch_x_y(31051, 30481) ;OPS
		touch_x_y(31228, 31021) ;OPS
		Sleep(250)

		touch_x_y($XCord, $YCord) ;ITEM
		Sleep(600)
		If $key_or_normal Then
; 		touch_x_y(5637,16296);Llave
; 			Sleep(3200)
		Else
			touch_x_y(3343, 16820);Otros
			Sleep(500)
		EndIf


	Next
EndFunc   ;==>DropItems_bluestack


Func Up_Items_bluestacks($cant = 1)
	For $i = 1 To $cant 
		touch_x_y(10355, 17635)
		Sleep(200)
		touch_x_y(6000,17635);llave
		; touch_x_y(9000, 17635)
		Sleep(1500)
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
		
		if $key_or_normal = 0 Then 
		touch_x_y(25920, 12397)
			touch_x_y(3277, 26714)
			Else
			touch_x_y(31228, 31021) ;OPS
			Sleep(250)
			$touch_x_y(18710, 16470);lLAVE
			Sleep(250)			
			$touch_x_y(5735, 26950) ;Recycle
			$touch_x_y(13239, 8846)	;Confirm
			Sleep(250)	
		EndIf
	Next
EndFunc   ;==>reciclar_bluestacks
