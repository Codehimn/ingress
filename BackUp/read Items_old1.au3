;~ 883 - 83
;~ 918 - 118


RunWait("adb shell screencap -p /sdcard/screen.png", @ScriptDir, @SW_SHOW)
RunWait("adb pull /sdcard/screen.png", @ScriptDir, @SW_SHOW)
RunWait("adb shell rm /sdcard/screen.png", @ScriptDir, @SW_SHOW)

$img = ObjCreate("ImageMagickObject.MagickImage.1")

$ret = $img.Convert("screen.png", _  ;      "-crop", "35x98+883+83", _        
        "-rotate", "-90" , _          ; "-negate",  _        
        "-unsharp", "3x1+12" ,  _      
        "crop_page.png")

Local $Items [8][5]

RunWait("tesseract.exe "&  " crop_page.png "  & " Numeros " , @ScriptDir, @SW_HIDE)
			$file = FileOpen(@ScriptDir & "\Numeros.txt", 0)

			While 1
    Local $line = FileReadLine($file)
    If @error = -1 Then ExitLoop
    MsgBox(0, "Line read:", $line)
WEnd

			$Numeros = FileReadLine($file)
			FileClose($file)	

