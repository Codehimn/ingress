
#include <Constants.au3>
#include <Array.au3>

HotKeySet("{F3}", "TogglePause")
Global $Paused

Local $file = FileOpen("portales diciembre.au3", 0)
;~ $String_portal = ClipGet()
$String_portal = FileRead($file)


$Limitar_equipo = ''; '<td style="text-align:center;">2</td>' ; 1 azul 2 verde
$Limitar_Deploids = '%</td><td>(.*?)</td><td'


Local $Portales[1]
Local $array[1]
$Deploids = 0


;~ '\[(.*?)\]'		'[(\d.*?\,.*?\d)\].*?'
$array_temp = StringRegExp($String_portal, 'Capture(.*?)help apGain', 3)
;~ _ArrayDisplay($array_temp)

For $i = 0 To UBound($array_temp) - 1

	$temp = StringRegExp($array_temp[$i], '\[(.*?\,.*?)\]', 3)

;~ if StringInStr()Enemy,Friendly

	If IsArray($temp) Then
;~ 		_ArrayDisplay($temp)
		$Dep_temp = StringRegExp($array_temp[$i], $Limitar_Deploids, 3)
		$cant_deploid = 8 - $Limitar_Deploids
		_ArrayAdd($array, _ArrayToString($temp) & "," & $cant_deploid)
	EndIf
Next

;~ cworsend("Local $Portales[1]" & @CRLF)
For $i = 1 To UBound($array) - 1

	_ArrayAdd($Portales, $array[$i])
;~ 	cworsend("_ArrayAdd($Portales , '" & $array[$i] & "')" & @CRLF)
;~ 	cworsend($array[$i] & @CRLF)
Next

;~ _ArrayDisplay($Portales)
;~ Exit

$X = StringSplit($Portales[1], ",")
_ArrayDelete($Portales, $Portales[1])

$distancia_con_portal_anterior = 0.001 ;(7 Segundos)





$pid = Run("C:\Users\Codehimn\Dropbox\ingress\adb shell", "", @SW_SHOW, $STDIN_CHILD + $STDOUT_CHILD)
cworsend2("su")

;~ cworsend("echo 1 > /sys/devices/i2c-0/0-0036/leds/lm3533-lcd-bl/brightness" & @CRLF)
;~ cworsend("am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity" & @CRLF)






For $i = 1 To UBound($Portales) - 1

	$distancia_menor = 1
	$Y_menor = 0
	For $i2 = 1 To UBound($Portales) - 1
		$distancia = 0
		$Y = StringSplit($Portales[$i2], ",")

		If $X[1] < 0 Then $X[1] = $X[1] * -1
		If $Y[1] < 0 Then $Y[1] = $Y[1] * -1
		If $X[2] < 0 Then $X[2] = $X[2] * -1
		If $Y[2] < 0 Then $Y[2] = $Y[2] * -1

		If $X[1] > $Y[1] Then
			$distancia = $distancia + $X[1] - $Y[1]
		Else
			$distancia = $distancia + $Y[1] - $X[1]
		EndIf

		If $X[2] > $Y[2] Then
			$distancia = $distancia + $X[2] - $Y[2]
		Else
			$distancia = $distancia + $Y[2] - $X[2]
		EndIf

		If $distancia < $distancia_menor Then
			$Y_menor = $i2 ; el Numero de ITEM
			$distancia_menor = $distancia
		EndIf
;~ 		EndIf
	Next

	ConsoleWrite($Portales[$Y_menor])
;~ 	$Portales[$Y_menor] = StringReplace($Portales[$Y_menor],".","")
	$X = StringSplit($Portales[$Y_menor], ",")
	$lat = StringReplace(StringFormat("%.6f", $X[1]), ".", "")
	$long = StringReplace(StringFormat("%.6f", $X[2]), ".", "") ;  - 300 ,

	$DistanciaMS = Round($distancia_con_portal_anterior * 7000000, 5)
	$DistanciaS = Round($DistanciaMS / 1000)
;~ 	cworsend($Portales[$Y_menor])
;~ 	cworsend("Hacer_Todo('"   & $X[1] &  ","  & $X[2] & "' , " & $X[3] & " , " & $DistanciaMS & " ) " & @CRLF)


	If $DistanciaMS < 1 Then $DistanciaMS = 1

;~ cworsend("am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity"& @CRLF)
;~ Funcion3("busybox sleep " & $DistanciaMS / 1000 & @CRLF)

;~ RunWait("am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity" )
	cworsend2("am startservice --ei lat " & $lat & " --ei long " & $long & " -n com.lexa.fakegpsdonate/.FakeGPSService")
	cworsend2("am force-stop com.lexa.fakegpsdonate")

	Sleep($DistanciaMS)
	WinActivate("BlueStacks")
	Sleep(2000)
	touch_x_y(10814, 16413)
;~ 	MouseClick("left", 1630, 695, 1, 0)
	Sleep(2000)
	cworsend2("am startservice --ei lat " & $lat & " --ei long " & $long & " -n com.lexa.fakegpsdonate/.FakeGPSService")
	cworsend2('sqlite3 /data/data/com.android.providers.settings/databases/settings.db "' & "update secure set value=0 where name='mock_location' " & '" ;')

	For $i = 1 To 20
;~ 		MouseClick("left", 1877, 373, 1, 0)
		touch_x_y(21560,30440)
		Sleep(100)
	Next
	cworsend2("am force-stop com.lexa.fakegpsdonate")
	Sleep(1000)
;~ MouseClick("left",1331, 57,1,0)
;~ 	MouseClick("left", 1873, 62, 1, 0)
	touch_x_y(31785,30207)
	Sleep(2000)
	Send("{esc}")

;~ 	$(( $RANDOM % 10 ));

	_ArrayDelete($Portales, $Y_menor)

	$distancia_con_portal_anterior = $distancia_menor

;~ Exit

Next

;~ cworsend("input keyevent 26" & @CRLF & @CRLF)


Func cworsend2($var)
;~    Send($var)
	StdinWrite($pid, $var & @CRLF)
EndFunc   ;==>cworsend2

Func TogglePause()
	$Paused = Not $Paused
	While $Paused
		Sleep(100)
		ToolTip('Script is "Paused"', 0, 0)
	WEnd
	ToolTip("")
EndFunc   ;==>TogglePause


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