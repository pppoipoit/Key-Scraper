## ตรวจไฟล์ทั้งหมด

### .clinerules/
Get-ChildItem -Path '.clinerules' -File | Select-Object Name | Format-Table -AutoSize

### docs/
Get-ChildItem -Path 'docs' -Recurse -File | Select-Object FullName | Format-Table -AutoSize
