

#include <INet.au3>
#include <String.au3>
#include <Constants.au3>
#include <Array.au3>

HotKeySet("{F3}", "TogglePause")
Global $Paused

;~ Local $file = FileOpen("portales diciembre.au3", 0)
Local $file = FileOpen("portales barcelona.au3", 0)
;~ Local $file = FileOpen("portales barcelona2.au3", 0)
;~ $String_portal = ClipGet()
$String_portal = FileRead($file)

$Limitar_equipo = ''; '<td style="text-align:center;">2</td>' ; 1 azul 2 verde
$Limitar_Deploids = '%</td><td>(.*?)</td><td'

;Defino array con datos de los portales
Local $Portales[1][5]
$Portales[0][0] = "X"
$Portales[0][1] = "Y"
$Portales[0][2] = "Deploid"
$Portales[0][3] = "Hacks"
$Portales[0][4] = "Tiempo de hack"

$Deploids = 0
$Hacks_posibles = 5
$segundos_entre_Hacks = 300
$tiempo_ultimo_hack = _DateAdd('s', ($segundos_entre_Hacks * -1) - 1, _NowCalc())
$distancia_con_portal_anterior = 0.001 ;(7 Segundos)
$Portal_anterior = ""

;~ '\[(.*?)\]'		'[(\d.*?\,.*?\d)\].*?'
$array_temp = StringRegExp($String_portal, 'Capture(.*?)help apGain', 3)
;~ _ArrayDisplay($array_temp)

For $i = 0 To UBound($array_temp) - 1
	$temp = StringRegExp($array_temp[$i], '\[(.*?\,.*?)\]', 3)
	$temp = StringSplit($temp[0], ",")
;~ if StringInStr()Enemy,Friendly
	If IsArray($temp) Then
		$Dep_temp = StringRegExp($array_temp[$i], $Limitar_Deploids, 3)
		$cant_deploid = 8 - $Dep_temp[0]
		ReDim $Portales[UBound($Portales) + 1][5]
		$Portales[UBound($Portales) - 1][0] = $temp[1]
		$Portales[UBound($Portales) - 1][1] = $temp[2]
		$Portales[UBound($Portales) - 1][2] = $cant_deploid
		$Portales[UBound($Portales) - 1][3] = $Hacks_posibles
		$Portales[UBound($Portales) - 1][4] = $tiempo_ultimo_hack
	EndIf
Next


;~ _ArrayDisplay($Portales)
;~ Exit
_ArrayDelete($Portales, 0) ; para quitar las cabeceras


$X = 0

If WinExists("C:\Users\Codehimn\Dropbox\ingress\adb.exe") Then WinClose("C:\Users\Codehimn\Dropbox\ingress\adb.exe")
$pid = Run("C:\Users\Codehimn\Dropbox\ingress\adb shell", "", @SW_SHOW, $STDIN_CHILD + $STDOUT_CHILD)
cworsend2("su")

;~ cworsend("echo 1 > /sys/devices/i2c-0/0-0036/leds/lm3533-lcd-bl/brightness" & @CRLF)
;~ cworsend("am start -a com.nianticproject.ingress -n com.nianticproject.ingress/com.nianticproject.ingress.NemesisActivity" & @CRLF)

 sing_out()

Exit

While 1
	$distancia_menor = 99999
	$Y_menor = 0
	$distancia_temp = 0

	$Portales[$X][3] = $Portales[$X][3] - 1
	$Portales[$X][4] = _NowCalc()

;~ 	_ArrayDisplay($Portales)

	Do
		For $Y = 0 To UBound($Portales) - 1

			If _DateDiff('h', $Portales[$Y][4], _NowCalc()) > 4 Then $Portales[$Y][4] = $Hacks_posibles
			If $Portales[$Y][3] >= 1 And _DateDiff('s', $Portales[$Y][4], _NowCalc()) > $segundos_entre_Hacks Then ;si quedan hacks disponibles, y si lleva mas de 5 min
				$distancia_temp = Abs($Portales[$X][0] - $Portales[$Y][0]) + Abs($Portales[$X][1] - $Portales[$Y][1])
				If $distancia_temp < $distancia_menor Then
					$Y_menor = $Y ; el Numero de ITEM
					$distancia_menor = $distancia_temp
				EndIf
				ConsoleWrite($Y & "," & ($Portales[$Y][3] >= 1) & "," & (_DateDiff('s', $Portales[$Y][4], _NowCalc()) > $segundos_entre_Hacks) & "," & Abs(@MIN - $Portales[$Y][4]) & "  " & $Portales[$Y][4] & @CRLF)
			EndIf
		Next
		ConsoleWrite($X & "-" & $Y_menor & "-------------------------- Sleep : " & Round($distancia_con_portal_anterior * 08000000, 5) & @CRLF)

		If $distancia_menor = 99999 Then Sleep(5000)
	Until $distancia_menor <> 99999

	$X = $Y_menor

	$lat = StringReplace(StringFormat("%.6f", $Portales[$X][0]), ".", "")
	$long = StringReplace(StringFormat("%.6f", $Portales[$X][1]), ".", "") ;  - 300 ,

	$DistanciaMS = Round($distancia_con_portal_anterior * 08000000, 5)
	$distancia_con_portal_anterior = $distancia_menor ;Para el tiempo del proximo hackeo , no del actual

;~ 	$new_distance = Int(getDistance(StringReplace($Portales[$Y_menor], ",8", ""), StringReplace($Portal_anterior, ",8", "")))
;~ 	$DistanciaMS =$DistanciaMS $new_distance / 0.002

;~ 	ConsoleWrite($Portales[$X][0] & "," & $Portales[$X][1] & "  espera = " & $DistanciaMS& @crlf)


	cworsend2("am startservice --ei lat " & $lat & " --ei long " & $long & " -n com.lexa.fakegpsdonate/.FakeGPSService")
	cworsend2("am force-stop com.lexa.fakegpsdonate")
	Sleep($DistanciaMS)
	touch_x_y(10814, 16413)
	Sleep(1500)
	cworsend2('sqlite3 /data/data/com.android.providers.settings/databases/settings.db "' & "update secure set value=0 where name='mock_location' " & '" ;')
	cworsend2("am startservice --ei lat " & $lat & " --ei long " & $long & " -n com.lexa.fakegpsdonate/.FakeGPSService")
	cworsend2('sqlite3 /data/data/com.android.providers.settings/databases/settings.db "' & "update secure set value=0 where name='mock_location' " & '" ;')

	For $i_clicks = 1 To 12
		Sleep(100)
		touch_x_y(21560, 30440)
	Next

	cworsend2("am force-stop com.lexa.fakegpsdonate")
	touch_x_y(2589, 15598) ;abajo de hack
	Sleep(500)
	touch_x_y(2589, 15598) ;abajo de hack
	Sleep(500)
	touch_x_y(2589, 15598) ;abajo de hack


;~ 	touch_x_y(31785, 30207);ops
;~ 	cworsend2('input keyevent 4')
;~ 	$(( $RANDOM % 10 ));

WEnd



Func cworsend2($var)
;~    Send($var)
	StdinWrite($pid, $var & @CRLF)
EndFunc   ;==>cworsend2

Func TogglePause()
	$Paused = Not $Paused
	While $Paused
		Sleep(100)
		ToolTip('Script is "Paused"', 0, 0)
		_ArrayDisplay($Portales)
		ExitLoop
	WEnd
	ToolTip("")
EndFunc   ;==>TogglePause


Func touch_x_y($X_mouse, $Y_mouse, $X_mouse2 = "", $Y_mouse2 = "")
	cworsend2("sendevent /dev/input/event1 3 0 " & $X_mouse)
	cworsend2("sendevent /dev/input/event1 3 1 " & $Y_mouse)
	cworsend2("sendevent /dev/input/event1 0 0 0")
	cworsend2("sendevent /dev/input/event1 0 0 0")
	cworsend2("sendevent /dev/input/event1 1 272 1")
	cworsend2("sendevent /dev/input/event1 0 0 0")
	If $X_mouse2 <> "" Then
		cworsend2("sendevent /dev/input/event1 3 0 " & $X_mouse2)
		cworsend2("sendevent /dev/input/event1 3 1 " & $Y_mouse2)
		cworsend2("sendevent /dev/input/event1 0 0 0")
	EndIf
	cworsend2("sendevent /dev/input/event1 1 272 0")
	cworsend2("sendevent /dev/input/event1 0 0 0")
EndFunc   ;==>touch_x_y

Func getDistance($start, $stop = "")
	If $stop = "" Then Return (20)

	$source = _INetGetSource("http://maps.googleapis.com/maps/api/distancematrix/xml?origins=" & _URLEncode($start) & "&destinations=" & _URLEncode($stop) & "&sensor=false&mode=walking")
	$source = _StringBetween($source, "<text>", "</text>")
	If UBound($source) <> 2 Then
		MsgBox(0, "Error", "Ein Fehler ist aufgetreten. Falsche Angaben?")
	Else
;~         _ArrayDisplay($source)
		ConsoleWrite(@CRLF & $source[0])
		Return ($source[0])
	EndIf


EndFunc   ;==>getDistance

Func _URLEncode($sData)
	; Prog@ndy
	Local $aData = StringSplit(BinaryToString(StringToBinary($sData, 4), 1), "")
	Local $nChar
	$sData = ""
	For $i = 1 To $aData[0]
		$nChar = Asc($aData[$i])
		Switch $nChar
			Case 45, 46, 48 - 57, 65 To 90, 95, 97 To 122, 126
				$sData &= $aData[$i]
			Case 32
				$sData &= "+"
			Case Else
				$sData &= "%" & Hex($nChar, 2)
		EndSwitch
	Next
	Return $sData
EndFunc   ;==>_URLEncode


;### Tidy Error: Func statement without parentheses ().
Func sing_out()
	touch_x_y(31051, 30481) ;OPS
	Sleep(200)
touch_x_y(32100, 27800, 32100, 5600)
Sleep(200)
touch_x_y(28000,24150)

;### Tidy Error: "endfunc" is likely missing it's opening statement. next line creates a negative tablevel.
EndFunc   ;==>
