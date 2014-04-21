
;~ getevent /dev/input/event2
;~ 0003 0039 0000024f [FD] FingerDown (24f)
;~ 0003 0035 00000163 [X] X coordinate
;~ 0003 0036 000001dd [Y] Y coordinate

;~ // NOTE LINE

;~ 0000 0000 00000000 [S] Separator

;~ 0003 0039 ffffffff [FU] FingerUp (24f)
;~ 0000 0000 00000000 [S] Separator
;~ ^C


;~ 1000 150

;~ adb shell sendevent /dev/input/event1 3 1000 150
;~ adb shell sendevent /dev/input/event1 3 35 163
;~ adb shell sendevent /dev/input/event1 3 36 000001dd
;~ adb shell sendevent /dev/input/event1 0 0 0 
;~ adb shell sendevent /dev/input/event1 3 39 ffffffff 
;~ adb shell sendevent /dev/input/event1 0 0 0 


;~ sendevent /dev/input/event1 3 0 150
;~ sendevent /dev/input/event1 3 1 1000
;~ sendevent /dev/input/event1 1 330 1
;~ sendevent /dev/input/event1 0 0 0
;~ sendevent /dev/input/event1 1 330 0
;~ sendevent /dev/input/event1 0 0 0

;~ sendevent /dev/input/event1 3 0 1000
;~ sendevent /dev/input/event1 3 1 150
;~ sendevent /dev/input/event1 1 330 1
;~ sendevent /dev/input/event1 0 0 0
;~ sendevent /dev/input/event1 1 330 0
;~ sendevent /dev/input/event1 0 0 0











;~ algo2("sendevent /dev/input/event1 0003 0039 00004dcb")
;~ algo2("sendevent /dev/input/event1 0003 0035 00000261")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004fe")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000040")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0035 0000025f")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004fd")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000041")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0035 0000025d")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000042")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0035 0000025b")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004fc")
;~ algo2("sendevent /dev/input/event1 0003 0030 00000005")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0035 00000259")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004fb")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000043")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0035 00000258")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004f9")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004f8")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004f7")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0035 00000256")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004f5")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000044")
;~ algo2("sendevent /dev/input/event1 0003 0031 00000004")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004f3")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000043")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004f1")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000042")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004ef")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000041")
;~ algo2("sendevent /dev/input/event1 0003 0030 00000004")
;~ algo2("sendevent /dev/input/event1 0003 0034 00000000")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004ed")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004eb")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004e9")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000040")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004e7")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000041")
;~ algo2("sendevent /dev/input/event1 0003 0030 00000005")
;~ algo2("sendevent /dev/input/event1 0003 0034 00000001")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004e4")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000040")
;~ algo2("sendevent /dev/input/event1 0003 0030 00000004")
;~ algo2("sendevent /dev/input/event1 0003 0031 00000003")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004dd")
;~ algo2("sendevent /dev/input/event1 0003 0030 00000005")
;~ algo2("sendevent /dev/input/event1 0003 0031 00000002")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004d1")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0035 00000255")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004bf")
;~ algo2("sendevent /dev/input/event1 0003 0031 00000003")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0035 00000254")
;~ algo2("sendevent /dev/input/event1 0003 0036 000004ad")
;~ algo2("sendevent /dev/input/event1 0003 0031 00000004")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 0000049d")
;~ algo2("sendevent /dev/input/event1 0003 0031 00000003")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 0000048c")
;~ algo2("sendevent /dev/input/event1 0003 0031 00000002")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0035 00000256")
;~ algo2("sendevent /dev/input/event1 0003 0036 00000477")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0035 00000257")
;~ algo2("sendevent /dev/input/event1 0003 0036 00000461")
;~ algo2("sendevent /dev/input/event1 0003 0030 00000004")
;~ algo2("sendevent /dev/input/event1 0003 0031 00000004")
;~ algo2("sendevent /dev/input/event1 0003 0034 00000000")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0035 00000258")
;~ algo2("sendevent /dev/input/event1 0003 0036 0000044e")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000041")
;~ algo2("sendevent /dev/input/event1 0003 0030 00000005")
;~ algo2("sendevent /dev/input/event1 0003 0031 00000003")
;~ algo2("sendevent /dev/input/event1 0003 0034 00000001")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 00000440")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000040")
;~ algo2("sendevent /dev/input/event1 0003 0031 00000002")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 00000434")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 0000042a")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 00000421")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 00000419")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 00000413")
;~ algo2("sendevent /dev/input/event1 0003 0031 00000003")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 0000040d")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000041")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 00000409")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 00000406")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 00000404")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 00000402")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 00000400")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000042")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000003fe")
;~ algo2("sendevent /dev/input/event1 0003 003a 00000041")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0036 000003fc")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")
;~ algo2("sendevent /dev/input/event1 0003 0039 ffffffff")
;~ algo2("sendevent /dev/input/event1 0000 0000 00000000")

Func algo2($Var)
   $algo = StringSplit($var , " ")
   ConsoleWrite("sendevent /dev/input/event1 "&  Dec($algo[1]) & " " & Dec($algo[2]) & " " & Dec($algo[3]) & @crlf)
EndFunc




algo2("0003 0039 000002ba")
algo2("0003 0035 000000e6") ;x
algo2("0003 0036 00000290") ;y
algo2("0003 0030 00000032")
algo2("0003 003a 00000003")
algo2("0000 0000 00000000")
algo2("0003 0035 000000fb") ;x
algo2("0003 0036 00000296") ;y
algo2("0000 0000 00000000")
algo2("0003 0035 00000120")
algo2("0003 003a 00000004")
algo2("0000 0000 00000000")
algo2("0003 0035 00000161") ;x
algo2("0003 0036 00000292") ;y
algo2("0003 003a 00000003")
algo2("0000 0000 00000000")
algo2("0003 0035 000001aa") ;x
algo2("0003 0036 0000029a") ;y
algo2("0003 0030 00000018")
algo2("0003 003a 00000001")
algo2("0000 0000 00000000")
algo2("0003 0039 ffffffff")
algo2("0000 0000 00000000")




