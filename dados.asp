<%@ Language=VBScript%>
<%
'-----------------------------------------------
On Error Resume Next
'-----------------------------------------------
%>
<!--#Include File="Lib/connection.asp" -->
<!--#Include File="Lib/functions_sms.asp" -->
<%
'-----------------------------------------------
DIM CONN, BusinessMarket
DIM RREFER,RRETURNCODE
DIM BMARKET,RCOD,RFD,TipoFiltro
'-----------------------------------------------

'-----------------------------------------------
strUser     	= Request.ServerVariables("AUTH_USER")
strPassword	= Request.ServerVariables("AUTH_PASSWORD")
strHOST		= Request.ServerVariables("HTTP_HOST")
If strHOST	= "production.netsafe.com.br" Then
	strHOST = "partnerserver.d-saas.net"
End if 
RREFER			= Request.ServerVariables("REMOTE_ADDR")
'-----------------------------------------------

'-----------------------------------------------
ValidateXML	= True
SMESSAGE		= ""
SSTATUS		= "SUCCESS"
strXMLName		= ""
sConfirmation	= ""
Fim 			= 0
CONN 			= ""
RetPARAMVALUE	= ""
'-----------------------------------------------
SCONFIRMATION	= ""
RCUSTOMERID	= ""
RPARTNERREF	= ""		
REMAIL			= ""	
RREQUESTTYPE	= ""	
SSTATUS 		= ""	
SMESSAGE		= ""	
McREF			= ""	


'-----------------------------------------------
'                   PERFECT XML
'-----------------------------------------------
If ValidateXML Then

	'-----------------------------------------------
	Set objXMLDOM = Server.CreateObject("Microsoft.XMLDOM")
	objXMLDOM.load Request	
	objXMLIncoming 	= objXMLDOM.xml
	RPARTNERID			= objXMLDOM.selectSingleNode("SOAP:Envelope/SOAP:Body/m:NSStatus/HEADER/RPARTNERID").Text
	RCUSTOMERID		= objXMLDOM.selectSingleNode("SOAP:Envelope/SOAP:Body/m:NSStatus/HEADER/RCUSTOMERID").Text
	RCOD				= objXMLDOM.selectSingleNode("SOAP:Envelope/SOAP:Body/m:NSStatus/HEADER/RCOD").Text
	RFD					= objXMLDOM.selectSingleNode("SOAP:Envelope/SOAP:Body/m:NSStatus/HEADER/RFD").Text
	Set objXMLDOM 	= Nothing
	'-----------------------------------------------
	
	'-----------------------------------------------
	If Err.Number <> 0 Then
		RRETURNCODE	= "100"
		SMESSAGE		= "ERROR 100 - malformed requests ["&Err.Number&Err.Description&"]"
		SSTATUS		= "FAIL"
		ValidateXML	= False
		Err.Clear
	End If
	'-----------------------------------------------

	'-----------------------------------------------
   	' create confirmation number
   	'-----------------------------------------------
	strYear   = Year(Now)
	strYear=Right(strYear,2)
	strMonth  = Month(Now)
	If Len(strMonth) < 2 Then strMonth = "0"&strMonth
	strDay    = Day(Now)
	If Len(strDay) < 2 Then strDay = "0"&strDay
	'-----------------------------------------------
	strLevel  		= UCase(Left(Level,1))
	strHour   		= Hour(Now):If Len(strHour) < 2 Then strHour= "0"&strHour
	strMinute 		= Minute(Now):If Len(strMinute) < 2 Then strMinute = "0"&strMinute
	strSecond 		= Second(Now):If Len(strSecond) < 2 Then strSecond = "0"&strSecond
	strXMLName 	= UCASE("STATUS_"&strYear&strMonth&strDay&strHour&strMinute&strSecond&"_"&RPARTNERID)
	'-----------------------------------------------
	
	
	'-----------------------------------------------
   	' write incoming log
   	'-----------------------------------------------
	'Dim fso, fs, LogFileName 
	'LogFileName = LogIncomingFilePath&strXMLName&".xml"
	'Set fso = Server.CreateObject("Scripting.FileSystemObject")
	'Set fs  = fso.CreateTextFile(LogFileName, True, True)
	'fs.WriteLine (objXMLIncoming)
	'fs.Close
   	'Set fso = Nothing
   	'-----------------------------------------------
   	
   	
   	'-----------------------------------------------
   	' send incoming log
   	'-----------------------------------------------
   	'strTemp = SendBulkEmail("henrique.carvalho@titansgroup.com.br",objXMLIncoming,IncomingText)
	'-----------------------------------------------
	
End If
'-----------------------------------------------
If Err.Number <> 0 Then
	RRETURNCODE	= "199"
	SMESSAGE		= "ERROR 199 - Fatal Error"
	SSTATUS		= "FAIL"
	ValidateXML	= False
	Err.Clear
End If
'-----------------------------------------------


'-----------------------------------------------
' check fields
'-----------------------------------------------
If ValidateXML Then
		
	If Len(RPARTNERID) < 5 Then
		RRETURNCODE	= "200"
		ValidateXML	= False
		SMESSAGE		= "ERROR 200 - invalid RPARTNERID"
	End If
	
	TipoFiltro = "0"
	If RCOD = "PHONE" Then TipoFiltro = "1"

	If TipoFiltro = "0"	Then
		RRETURNCODE	= "210"
		ValidateXML	= False
		SMESSAGE 		= "ERROR 210 - invalid RCOD"
	End If
	
	If TipoFiltro = "1" Then
		If Len(RFD) < 13 or Len(RFD) > 14 Then
			RRETURNCODE	= "220"
			ValidateXML 	= False
			SMESSAGE 		= "ERROR 220 - invalid RFD"
		End If	
	End If
		
End If
'-----------------------------------------------
	

'-----------------------------------------------
strTemp = OpenMobileConnection()
'-----------------------------------------------

'-----------------------------------------------
'             PROCESS ORDER FOR PARTNER
'-----------------------------------------------
If ValidateXML Then

	strTemp = CheckPhoneStatus(RFD)
	If strTemp = "Not Found" Then
		SMESSAGE 		= "850 - Not Found"
		RRETURNCODE	= "850"
		SSTATUS="SUCCESS"
	Else
		RRETURNCODE = "899":SMESSAGE = "899 - Unavailable"
		If strTemp = "Not Active" 	Then RRETURNCODE	= "810":SMESSAGE = "810 - Not Active"
		If strTemp = "Active" 		Then RRETURNCODE	= "800":SMESSAGE = "800 - Active"
		SSTATUS="SUCCESS"
	End If
	
	
End If
'--------------------------------------------------------
If Err.Number <> 0 Then
	RRETURNCODE	= "900"
	SMESSAGE		= "ERROR 900 - Fatal Error ["&Err.Number&Err.Description&"]"
	SSTATUS		= "FAIL"
	ValidateXML	= False
	Err.Clear
End If
'--------------------------------------------------------

'--------------------------------------------------------
sXMLOutput = "<?xml version='1.0'?>"
sXMLOutput = sXMLOutput & "<NSPRODUCTS>"
sXMLOutput = sXMLOutput & "<HEADER>"
sXMLOutput = sXMLOutput & "<PARTNERID>"		& RPARTNERID		& "</PARTNERID>"
sXMLOutput = sXMLOutput & "<RETURNCODE>"		& RRETURNCODE		& "</RETURNCODE>"
sXMLOutput = sXMLOutput & "<STATUS>"			& SSTATUS			& "</STATUS>" 
sXMLOutput = sXMLOutput & "<CONFIRMATION>" 	& strXMLName		& "</CONFIRMATION>"
sXMLOutput = sXMLOutput & "<MESSAGE>" 		& SMESSAGE			& "</MESSAGE>" 
sXMLOutput = sXMLOutput & "</HEADER>"
sXMLOutput = sXMLOutput & "</NSPRODUCTS>"
'--------------------------------------------------------


'********************************************************************************
'                                  Grava Log 
'********************************************************************************
GravaLog=true
If GravaLog Then

	'-------------------------------------------
	strSQL = "INSERT INTO WebLog ("
	strSQL = strSQL & "DataPost,"
	strSQL = strSQL & "ConfirmationNumber,"
	strSQL = strSQL & "CustomerID,"
	strSQL = strSQL & "OrderID,"
	strSQL = strSQL & "Email,"
	strSQL = strSQL & "Request,"
	strSQL = strSQL & "Status,"
	strSQL = strSQL & "Mensagem,"
	strSQL = strSQL & "McREF,"
	strSQL = strSQL & "XMLIn,"
	strSQL = strSQL & "XMLSend,"
	strSQL = strSQL & "XMLRec,"
	strSQL = strSQL & "XMLOut"
	'-------------------------------------------
	strSQL = strSQL & ") VALUES ("
	'-------------------------------------------
	strSQL = strSQL & " '" & NOW 				& "'"	
	strSQL = strSQL & ",'" & strXMLName		& "'"
	strSQL = strSQL & ",'" & RCUSTOMERID 		& "'"	
	strSQL = strSQL & ",'" & ""			 		& "'"		
	strSQL = strSQL & ",'" & RFD 				& "'"	
	strSQL = strSQL & ",'" & "update"			& "'"	
	strSQL = strSQL & ",'" & SSTATUS 			& "'"	
	strSQL = strSQL & ",'" & SMESSAGE	 		& "'"	
	strSQL = strSQL & ",'" & RCOD	 			& "'"	
	strSQL = strSQL & ",'" & replace(objXMLIncoming,chr(39),chr(34))	& "'"	
	strSQL = strSQL & ",'" & ""		& "'"	
	strSQL = strSQL & ",'" & ""		& "'"	
	strSQL = strSQL & ",'" & replace(sXMLOutput,chr(39),chr(34))		& "')"
	'-------------------------------------------
	Set rs = conn.Execute(strSQL)
	Set rs = Nothing
	'-------------------------------------------
	
End If
'********************************************************************************

'--------------------------------------------------------
strTemp = CloseMobileConnection()
'--------------------------------------------------------
	
'--------------------------------------------------------
Response.ContentType = "Text/XML"
Response.Write (sXMLOutput)
'--------------------------------------------------------
%>

