powershell Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
powershell Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
SET PATH=%PATH%;%UserProfile%\scoop\shims
