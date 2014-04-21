#Include <GuiToolBar.au3>

#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>
#include <GuiListView.au3>


HotKeySet("{ESC}", "_Quit")

Opt("WinTitleMatchMode", 4)
Global $hTray = WinGetHandle("[CLASS:Shell_TrayWnd]")
Global $hToolbar = ControlGetHandle($hTray, "", "[CLASSNN:ToolbarWindow321]")
Global $iCnt = _GUICtrlToolbar_ButtonCount($hToolbar)
ConsoleWrite("Debug: $iCnt = " & $iCnt & @LF)
Global $iCmdVolume = -1
Global $sMsg, $sText, $iCmd

GUICreate("List Box Get Sel", 400, 296)
$listview = GUICtrlCreateListView("Index|CommandID|Text", 2, 2, 396, 296)

For $n = 0 To $iCnt - 1
    $sMsg = "Index: " & $n
    $iCmd = _GUICtrlToolbar_IndexToCommand($hToolbar, $n)
    $sMsg &= "  CommandID: " & $iCmd
    $sText = _GUICtrlToolbar_GetButtonText($hToolbar, $iCmd)
    If StringInStr($sText, "LogMeIn") Then $iCmdVolume = $iCmd
    $sMsg &= "  Text: " & $sText
    ConsoleWrite("Debug: " & $sMsg & @LF)

GUICtrlCreateListViewItem($n & "|"&$iCmd&"|"&$sText, $listview)

Next
GUISetState()

Do
Until GUIGetMsg() = $GUI_EVENT_CLOSE
GUIDelete()

ConsoleWrite ( @CRLF & _GUICtrlListView_GetItemText($listview, _GUICtrlListView_GetSelectedIndices($listview) , 1))


Exit


ConsoleWrite("Debug: $iCmdVolume = " & $iCmdVolume & @LF)

Global $bolVisible = True
While 1
    $bolVisible = Not $bolVisible
    If $bolVisible Then
        _GUICtrlToolbar_SetButtonState($hToolbar, $iCmdVolume, $TBSTATE_ENABLED)
    Else
        _GUICtrlToolbar_SetButtonState($hToolbar, $iCmdVolume, $TBSTATE_HIDDEN)
    EndIf
    Sleep(1000)
WEnd

Func _Quit()
    _GUICtrlToolbar_SetButtonState($hToolbar, $iCmdVolume, $TBSTATE_ENABLED)
_GUICtrlToolbar_DeleteButton($hToolbar, $iCmdVolume)
    Exit
EndFunc





Exit




#include <GuiListBox.au3>
#include <GUIConstantsEx.au3>


_Main()

Func _Main()
Local $hListBox

; Create GUI
GUICreate("List Box Get Sel", 400, 296)
$hListBox = GUICtrlCreateList("", 2, 2, 396, 296, BitOR($LBS_STANDARD, $LBS_EXTENDEDSEL))
GUISetState()

; Add strings
_GUICtrlListBox_BeginUpdate($hListBox)
For $iI = 1 To 9
_GUICtrlListBox_AddString($hListBox, StringFormat("%03d : Random string", Random(1, 100, 1)))
Next
_GUICtrlListBox_EndUpdate($hListBox)

; Select a few items
_GUICtrlListBox_SetSel($hListBox, 3)
_GUICtrlListBox_SetSel($hListBox, 4)
_GUICtrlListBox_SetSel($hListBox, 5)

; Show the item selection state
MsgBox(4160, "Information", "Item 5 Selected: " & _GUICtrlListBox_GetSel($hListBox, 4))

; Loop until user exits
Do
Until GUIGetMsg() = $GUI_EVENT_CLOSE
GUIDelete()
EndFunc   ;==>_Main
