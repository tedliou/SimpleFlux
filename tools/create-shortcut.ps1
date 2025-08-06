# 建立 COM 物件
$shell = New-Object -COM WScript.Shell

# 取得桌面路徑 (PowerShell 變數)
$desktopPath = [System.Environment]::GetFolderPath('Desktop')

# 取得當前工作目錄 (PowerShell 變數)
$currentDirectory = Get-Location

# 建立捷徑物件
$shortcut = $shell.CreateShortcut("$desktopPath\SimpleLux.lnk")

# 設定目標路徑，使用 PowerShell 變數
$shortcut.TargetPath = "$currentDirectory\SimpleLux.exe"

# 儲存捷徑
$shortcut.Save()
