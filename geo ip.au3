#include <File.au3>
#include <Array.au3>
Global $aRecords
Global $aiResult, $filetoarray, $handle, $XML, $newtext

Global $oXML = ObjCreate("Microsoft.XMLHTTP")
$oXML.Open("GET", "<a href='http://maps.google.com/maps/api/directions/xml?origin=48143,Muenster&destination=23560,Luebeck&sensor=false' class='bbc_url' title='External link' rel='nofollow external'>http://maps.google.com/maps/api/directions/xml?origin=48143,Muenster&destination=23560,Luebeck&sensor=false</a>", 0)
$oXML.Send

$XML = $oXML.responseText


$array = StringSplit ($XML,"</distance>",1) ; splits at every instance of /distance

$array2 = stringsplit ($array[$array[0]-1], "<text>", 1) ; selects the last split segment, which contains the total distance, and splits it down by text occurrences

;_ArrayDisplay ($array2) ; just to demo

$Distance = StringTrimRight($array2[$array2[0]],11) ; picks last instance and trims the end tags.


Msgbox(0,'Results:', $distance)