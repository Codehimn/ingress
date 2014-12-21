;~ 883 - 83
;~ 918 - 118

#include <Array.au3>

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
$Items[0][1] = "B"
$Items[0][2] = "U"
$Items[0][3] = "C"
$Items[0][4] = "M"

RunWait("tesseract.exe " & " crop_page.png " & " Numeros ", @ScriptDir, @SW_HIDE)
$file = FileOpen(@ScriptDir & "\Numeros.txt", 0)

While 1
	Local $line = FileReadLine($file)
	If @error = -1 Then ExitLoop
	; MsgBox(0, "Line read:", $line)
	If StringInStr($line, "L1") Then ExitLoop
WEnd



For $i = 1 To 8
	$temp1 = StringSplit($line, ' ')
	For $i2 = 2 To 6
		$Items[$i][$i2 -2] = $temp1 [$i2]
		If $Items[$i][$i2 -2] > 100 Then
drop ($Items[0][$i2 -2]  & $i2 -2)
		endif
	Next
	Local $line = FileReadLine($file)
Next

; _ArrayDisplay($Items)
$Numeros = FileReadLine($file)
FileClose($file)


 