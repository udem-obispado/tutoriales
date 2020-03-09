Attribute VB_Name = "Module1"
Private Sub sqroot()

  Randomize

  Dim prompt As String
  Dim root
  Dim coin
  Dim REAL
  '"Dim" declara las variables
  
  prompt = "Dame un número real"
  REAL = InputBox(prompt)
  '"InputBox" generará un cuadro para escribir el número
  
  If REAL < 0 Then
    coin = Sqr(REAL * (-1))
    root = coin & "i"
    MsgBox ("La raíz cuadrada del número introducido es " + root)
	'"MsgBox" generará un cuadro con el resultado
	'Los números imaginarios también se pueden denotar escribiendo "i" después de la raíz cuadrada del número sin el signo negativo
	'"Sqr" sacará la raíz cuadrada del número que escribiste antes
  Else:
    root = Sqr(REAL)
    MsgBox ("La raíz cuadrada del número introducido es " & root)
  End If
  
End Sub
