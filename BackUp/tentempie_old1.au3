#include <Constants.au3>

HotKeySet("{F4}", "StopCommand")
HotKeySet("1", "ReDoCommand")

Local $pid

;~ $pid = Run(@ComSpec & " /k ", "", @SW_SHOW, $STDIN_CHILD + $STDOUT_CHILD)
;~ StdinWrite($pid, "C:\Users\Codehimn\Dropbox\ingress\adb shell" & @CRLF)

$pid = Run("C:\Users\Codehimn\Dropbox\ingress\adb shell" ,"", @SW_SHOW, $STDIN_CHILD + $STDOUT_CHILD)
StdinWrite($pid, "su" & @CRLF)
;~ StdinWrite($pid, "cd /data/data/com.android.providers.settings/databases" & @CRLF)
;~ StdinWrite($pid, 'sqlite3 /data/data/com.android.providers.settings/databases/settings.db "' & "Select value from secure where name='mock_location' " & '" ;' & @CRLF)
While 1
StdinWrite($pid, 'sqlite3 /data/data/com.android.providers.settings/databases/settings.db "' & "update secure set value=0 where name='mock_location' " & '" ;' & @CRLF)
;~ sqlite3 /data/data/com.android.providers.settings/databases/settings.db "update secure set value=0 where name='mock_location';"
Sleep(5000)
WEnd

While 1
    $msg = StdoutRead($pid)
    If $msg <> "" Then ConsoleWrite($msg & "-")
;~ 	if StringInStr
    Sleep(50)
WEnd



Func ReDoCommand()
    StdinWrite($pid, "ping -t google.com" & @CRLF)
EndFunc




Exit