Private Sub SendHelloWorld()
	
	Dim sck As MSWinsockLib.Winsock
	
	Set sck = New MSWinsockLib.Winsock
	
	'Set the remote host address and port
	sck.RemoteHost = "127.0.0.1"
	sck.RemotePort = 5000
	
	'Connect to the remote host
	sck.Connect
	
	'Send the message
	sck.SendData "Hello World"
	
	'Disconnect from the remote host
	sck.Close
	
	Set sck = Nothing
	
End Sub

Private Sub ReceiveHelloWorld()

	Dim sck As MSWinsockLib.Winsock
	Dim data As String
	
	Set sck = New MSWinsockLib.Winsock
	
	'Set the local listening port
	sck.LocalPort = 5000
	
	'Listen for incoming connections
	sck.Listen
	
	'Accept the incoming connection
	sck.Accept
	
	'Receive the data
	Do While sck.State = sckConnected
		If sck.BytesReceived > 0 Then
			data = sck.GetData
			If InStr(data, "Hello World") > 0 Then
				MsgBox "Received message: " & data
			End If
		End If
	Loop
	
	'Disconnect from the remote host
	sck.Close
	
	Set sck = Nothing
	
End Sub
