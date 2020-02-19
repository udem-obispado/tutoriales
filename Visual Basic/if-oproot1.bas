Attribute VB_Name = "Module1"
Private Sub sqroot()

  Randomize

  Dim raptor_prompt_variable_zzyz As String
  Dim root
  Dim REAL
  
  raptor_prompt_variable_zzyz = "Dame un número real"
  REAL = InputBox(raptor_prompt_variable_zzyz)
  
  If REAL < 0 Then
    root = "imaginario"
    MsgBox ("La raíz cuadrada del número introducido es un número " + root), vbCritical
  Else:
    root = Sqr(REAL)
    MsgBox ("La raíz cuadrada del número introducido es " & root)
  End If
  
End Sub

