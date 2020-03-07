Attribute VB_Name = "Module1"
Private Sub sqroot()

  Randomize

  Dim raptor_prompt_variable_zzyz As String
  Dim root
  Dim REAL
  '"Dim" declara las variables
  
  raptor_prompt_variable_zzyz = "Dame un número real"
  REAL = InputBox(raptor_prompt_variable_zzyz)
  '"InputBox" generará un cuadro para escribir el número
  
  If REAL < 0 Then
    root = "imaginario"
    MsgBox ("La raíz cuadrada del número introducido es un número " + root), vbCritical
	'"MsgBox" generará un cuadro con el resultado
	'"vbCritical" convertirá el MsgBox en un cuadro de alerta
  Else:
    root = Sqr(REAL)
    MsgBox ("La raíz cuadrada del número introducido es " & root)
	'"Sqr" sacará la raíz cuadrada del número que escribiste antes
  End If
  
End Sub

