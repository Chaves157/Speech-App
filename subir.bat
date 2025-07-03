@echo off
cd /d %~dp0

REM === Solicita mensagem de commit
set /p MSG=Digite a mensagem do commit: 

REM === Data e hora atuais
for /f "tokens=1-5 delims=/ " %%a in ("%date% %time%") do (
    set DIA=%%a
    set MES=%%b
    set ANO=%%c
    set HORA=%%d
)

set VERSAO=Versão: %MSG% – Atualizado em %DIA%/%MES%/%ANO% às %HORA%

REM === Substitui a linha da versão no index.html
powershell -Command "(Get-Content templates\index.html) -replace 'Versão: .*? às .*?</div>', '%VERSAO%</div>' | Set-Content templates\index.html"

REM === Executa push para o GitHub
git add .
git commit -m "%MSG%"
git push origin main

echo.
echo ✅ Código enviado com sucesso com a nova versão!
pause
