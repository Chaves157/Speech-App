@echo off
cd /d %~dp0
echo ================================
echo Fazendo commit e push para o GitHub...
echo ================================

set /p MSG=Digite a mensagem do commit: 
git add .
git commit -m "%MSG%"
git push origin main

echo.
echo ✅ Código enviado com sucesso!
pause
