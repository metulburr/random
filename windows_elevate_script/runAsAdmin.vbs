Set objShell = CreateObject("Shell.Application") objShell.ShellExecute WScript.Arguments.Item(0), WScript.Arguments.Item(1), "", "runas", 1
