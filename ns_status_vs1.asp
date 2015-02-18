<%@ Language=VBScript%>
<%
On Error Resume Next
Dim LogIncomingFilePath, LogResponseFilePath
Dim IncomingText, ResponseText
'-----------------------------------------------
%>
<!--#Include File="../nswebservice/Lib/connection.asp" -->
<!--#Include File="../nswebservice/Lib/functions_status.asp" -->
<%
'-----------------------------------------------
DIM CONN, BusinessMarket
DIM ITEM(50), SKU(50), PRODUCT(50), NAME(50)
DIM BUNDLE(50), TRIAL(50), OFFER(50), AUTORENEWAL(50)
DIM MAQUINAS(50)
DIM RREFER
'-----------------------------------------------

'-----------------------------------------------
DIM OrderItem,OrderConf(20),OrderSTATUS(20),OrderMESSAGE(20)
DIM OrderNSREFERENCE(20),OrderREFERENCE(20),OrderDate(20),OrderTYPE(20)
'-----------------------------------------------
DIM RetSTATUSMcafee,RetPartnerOrderID,RetOrderDate,RetDOWNLOADURL,RetMcafeeOrderID	
DIM RetConfirmationNumber,RetIpOrigem,RetRequestType,RetSTATUS,RetPARAMVALUE
'-----------------------------------------------
DIM CustomerNSID,CustomerCUSTOMERID,CustomerEMAIL
'-----------------------------------------------
DIM BMARKET,RCOD,RFD,TipoFiltro
'-----------------------------------------------
strUser     	= Request.ServerVariables("AUTH_USER")
strPassword	= Request.ServerVariables("AUTH_PASSWORD")
strHOST		= Request.ServerVariables("HTTP_HOST")
RREFER			= Request.ServerVariables("REMOTE_ADDR")
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


'======================================================
'                   PERFECT XML
'======================================================
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
		SMESSAGE		= "ERROR 100 - malformed request ["&Err.Number&Err.Description&"]"
		SSTATUS		= "FAIL"
		ValidateXML	= False
		Err.Clear
	End If
	'-----------------------------------------------
	
	'-----------------------------------------------
	If ValidateXML Then
		
		If Len(RPARTNERID)	< 5	Then ValidateXML	= False:SMESSAGE	= "ERROR 101 - invalid RPARTNERID"
		If Len(RCUSTOMERID)	< 5	Then ValidateXML	= False:SMESSAGE	= "ERROR 102 - invalid RCUSTOMERID"
		
		TipoFiltro = "0"
		If RCOD = "" 			Then TipoFiltro = "1"
		If RCOD = "Order"		Then TipoFiltro = "2"
		If RCOD = "SKU"		Then TipoFiltro = "3"
		If TipoFiltro = "0"	Then ValidateXML = False:SMESSAGE = "ERROR 103 - invalid RCOD"
		
		If TipoFiltro = "2" AND Len(RFD) < 3 Then ValidateXML = False:SMESSAGE = "ERROR 104 - invalid RFD"
		If TipoFiltro = "3" AND Len(RFD) < 3 Then ValidateXML = False:SMESSAGE = "ERROR 104 - invalid RFD"
		
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
   	'strTemp = SendBulkEmail("webservice@netsafe.com.br",objXMLIncoming,IncomingText)
	'-----------------------------------------------
	
End If
'======================================================
If Err.Number <> 0 Then
	SMESSAGE		= "ERROR 199 - Fatal Error"
	SSTATUS		= "FAIL"
	ValidateXML	= False
	Err.Clear
End If
'======================================================


'-----------------------------------------------
' Open Connection
'-----------------------------------------------
strTemp = OpenConnection()
'-----------------------------------------------


'======================================================
'                 CHECK FIELDS
'======================================================
If ValidateXML Then

	
	'-------------------------------
	'       Valida Partner
	'-------------------------------
	If strMessage = "" Then
		strTemp = GetPartner(RPARTNERID,strUser)
		If strTemp = "" Then
			strMessage = "ERROR 200 - partner id [" & RPARTNERID & "]"
		Else
			MCAFEEID = strTemp
		End If
	End If
	'-------------------------------
	
	
	'-------------------------------
	'     Partner Business Market
	'-------------------------------
	If strMessage = "" Then
		strTemp = GetBusinessMarket(RPARTNERID)
		If strTemp = "" Then
			strMessage = "ERROR 201 - Invalid Customer Business Market"
		Else
			BMARKET = Trim(strTemp)
		End If
	End If
	'-------------------------------
	
	
	'-------------------------------
	'    Check for Error
	'-------------------------------
	If strMessage <> "" Then
		SMESSAGE	= "ERROR 202 - following fields are invalid "&strMessage
		SSTATUS	= "FAIL"
		ValidateXML	= False
		Err.Clear
	End If
	'-------------------------------
	
	
End If
'======================================================
If Err.Number <> 0 Then
	SMESSAGE		= "ERROR 299 - Fatal Error"
	SSTATUS		= "FAIL"
	ValidateXML	= False
	Err.Clear
End If
'======================================================


'======================================================
'             PROCESS ORDER FOR PARTNER
'======================================================
If ValidateXML Then

	strMessage	= ""
	'-------------------------------
	'       Valida URL
	'-------------------------------	
	If strHOST <> strHostPermitido Then strMessage="Host not allowed - strHOST"
   	'-------------------------------
	   	
   	'-----------------------------------------------
	'       Valida productionDB
	'-----------------------------------------------	
	If strMessage = "" Then
		If strHostPermitido	= "staging.netsafe.com.br"    Then strTemp = StagingDB(RPARTNERID)
		If strHostPermitido	= "production.netsafe.com.br" Then strTemp = ProductionDB(RPARTNERID)
		If strTemp <> "Y" Then strMessage = "Partner not allowed "&strHostPermitido
	End If
   	'-----------------------------------------------
   	
   	
   	'-----------------------------------------------
	' check product info
	'-----------------------------------------------
	OrderItem				= 0
	OrderConf(1)			= "Unavailable"
	OrderSTATUS(1)		= "Unavailable"
	OrderMESSAGE(1)		= "Unavailable"
	OrderNSREFERENCE(1)	= "Unavailable"
	OrderREFERENCE(1)		= "Unavailable"
	OrderDate(1)			= "Unavailable"
	OrderTYPE(1)			= "Unavailable"
	'-----------------------------------------------
	
	
   	'-----------------------------------------------
	' Check Partner Info
	'-----------------------------------------------
	If strMessage = "" Then
		strTemp = CheckCustomerStatus(RCUSTOMERID,RPARTNERID,TipoFiltro,RFD)
		If strTemp = "" Then
			strMessage="Invalid CCID"
			CustomerCUSTOMERID = RCUSTOMERID
		End If
	End If
	'-----------------------------------------------

	
	'-----------------------------------------------
	If strMessage <> "" Then
		SMESSAGE		= "ERROR 402 - Invalid data ["&strMessage&"]"
		SSTATUS		= "FAIL"
		ValidateXML	= False
	End If
	'-----------------------------------------------
	
End If
'======================================================
If Err.Number <> 0 Then
	SMESSAGE		= "ERROR  303 - Fatal Error ["&Err.Number&Err.Description&"]"
	SSTATUS		= "FAIL"
	ValidateXML	= False
	Err.Clear
End If
'======================================================


'======================================================
'                     ATUALIZA DB
'======================================================
If ValidateXML Then

	strMessage	= ""
	
   	'-------------------------------
	'      Grava Request Ordem
	'-------------------------------
	'strTemp = GetInsertConfirmation(strXMLName)
	'If strTemp <> "" Then
	'	strMessage = "Insert Confirmation"
	'End If
	'-------------------------------
	
	'-------------------------------
	'If strMessage <> "" Then
	'	SMESSAGE	= "ERROR 404 - DB "&strMessage
	'	SSTATUS		= "FAIL"
	'	ValidateXML	= False
	'End If
	'-------------------------------
	
End If
'======================================================
If Err.Number <> 0 Then
	SMESSAGE	= "ERROR  304 - Fatal Error ["&Err.Number&Err.Description&"]"
	SSTATUS		= "FAIL"
	ValidateXML	= False
	Err.Clear
End If
'======================================================


'--------------------------------------------------------
' Close Connection
'--------------------------------------------------------
strTemp = CloseConnection()


'--------------------------------------------------------
' Create XML respone back
'--------------------------------------------------------
Dim sXMLOutput	
sXMLOutput = "<?xml version='1.0'?>"
'--------------------------------------------------------
sXMLOutput = sXMLOutput & "<NSPRODUCTS>"
sXMLOutput = sXMLOutput & "<HEADER>"
sXMLOutput = sXMLOutput & "<PARTNERID>"		& RPARTNERID		& "</PARTNERID>"
sXMLOutput = sXMLOutput & "<STATUS>"			& SSTATUS			& "</STATUS>" 
sXMLOutput = sXMLOutput & "<CONFIRMATION>" 	& strXMLName		& "</CONFIRMATION>"
sXMLOutput = sXMLOutput & "<MESSAGE>" 		& SMESSAGE			& "</MESSAGE>" 
sXMLOutput = sXMLOutput & "</HEADER>"
'--------------------------------------------------------


sXMLOutput = sXMLOutput & "<DATA>"

'--------------------------------------------------------
sXMLOutput = sXMLOutput & "<CUSTOMER>"
sXMLOutput = sXMLOutput & "<CUSTOMERID>"	& CustomerCUSTOMERID	& "</CUSTOMERID>"
sXMLOutput = sXMLOutput & "<EMAIL>"		& CustomerEMAIL		& "</EMAIL>"
sXMLOutput = sXMLOutput & "</CUSTOMER>"
'--------------------------------------------------------


sXMLOutput = sXMLOutput & "<ORDER>"
'--------------------------------------------------------
	sXMLOutput = sXMLOutput & "<ORDERDATE>"				& RetOrderDate			& "</ORDERDATE>"
	sXMLOutput = sXMLOutput & "<CONFIRMATIONID>"			& RetConfirmationNumber	& "</CONFIRMATIONID>"
	
	sXMLOutput = sXMLOutput & "<STATUS>"					& RetSTATUS				& "</STATUS>"
	sXMLOutput = sXMLOutput & "<REQUESTTYPE>"				& RetRequestType			& "</REQUESTTYPE>"
	
	sXMLOutput = sXMLOutput & "<MESSAGE>"					& RetSTATUSMcafee			& "</MESSAGE>"
	
	sXMLOutput = sXMLOutput & "<PREFERENCE>"				& RetPartnerOrderID		& "</PREFERENCE>"
	sXMLOutput = sXMLOutput & "<NSREFERENCE>"				& RetMcafeeOrderID		& "</NSREFERENCE>"
	
	sXMLOutput = sXMLOutput & "<URL>"						& RetDOWNLOADURL			& "</URL>"
	sXMLOutput = sXMLOutput & "<IP>"						& RetIpOrigem				& "</IP>"
	sXMLOutput = sXMLOutput & "<PARAMVALUE><![CDATA["	& RetPARAMVALUE			& "]]></PARAMVALUE>"
'--------------------------------------------------------
sXMLOutput = sXMLOutput & "</ORDER>"


						
							
					
				
'--------------------------------------------------------
sXMLOutput = sXMLOutput & "</DATA>"
'--------------------------------------------------------
sXMLOutput = sXMLOutput & "</NSPRODUCTS>"
'--------------------------------------------------------


'--------------------------------------------------------
' write response log
'--------------------------------------------------------
'LogFileName = LogResponseFilePath&strXMLName&".xml"
'Set fso = Server.CreateObject("Scripting.FileSystemObject")
'Set fs  = fso.CreateTextFile(LogFileName , True, True)
'fs.WriteLine (sXMLOutput)
'fs.Close
'Set fso = Nothing
'--------------------------------------------------------


'--------------------------------------------------------
' send Output log
'--------------------------------------------------------
'strTemp = SendBulkEmail("fabio.rudge@targethosting.com.br",sXMLOutput,"production - Check Status")
'--------------------------------------------------------


'--------------------------------------------------------
Response.ContentType = "Text/XML"
Response.Write (sXMLOutput)
'======================================================
%>



