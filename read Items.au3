; 883 - 83
; 918 - 118

#include <Array.au3>
#include <Drop ingress 2.au3>

$minimo_items = 30
;~ Up_Items_bluestacks(300)
 DropItems_bluestack("R7", 1) ;1 = KEY
Exit

touch_x_y(31228, 31021) ;OPS
Sleep(2000)

RunWait("adb shell screencap -p /sdcard/screen.png", @ScriptDir, @SW_SHOW)
RunWait("adb pull /sdcard/screen.png", @ScriptDir, @SW_SHOW)
RunWait("adb shell rm /sdcard/screen.png", @ScriptDir, @SW_SHOW)

$img = ObjCreate("ImageMagickObject.MagickImage.1")

$ret = $img.Convert("screen.png", _  ;      "-crop", "35x98+883+83", _
		"-rotate", "-90", _          ; "-negate",  _
		"-unsharp", "3x1+12", _
		"crop_page.png")

Local $Items[9][5]
$Items[0][0] = "R"
$Items[0][1] = "X"
$Items[0][2] = "U"
$Items[0][3] = "C"
$Items[0][4] = "M"

RunWait("tesseract.exe " & " crop_page.png " & " Numeros ", @ScriptDir, @SW_HIDE)
$file = FileOpen(@ScriptDir & "\Numeros.txt", 0)

While 1
	Local $line = FileReadLine($file)
	If @error = -1 Then ExitLoop
	; MsgBox(0, "Line read:", $line)
	If StringInStr($line, "L",1) Then ExitLoop
WEnd



For $i = 1 To 8
	$temp1 = StringSplit($line, ' ')
	For $i2 = 2 To 6
		$Items[$i][$i2 - 2] = $temp1[$i2]
		If $Items[$i][$i2 - 2] > $minimo_items Then
		ConsoleWrite($Items[0][$i2 - 2] & $i & "---" &  $Items[$i][$i2 - 2] -$minimo_items)
			DropItems_bluestack($Items[0][$i2 - 2] & $i, $Items[$i][$i2 - 2] -$minimo_items)
		EndIf
	Next
	Local $line = FileReadLine($file)
Next

; _ArrayDisplay($Items)
$Numeros = FileReadLine($file)
FileClose($file)



