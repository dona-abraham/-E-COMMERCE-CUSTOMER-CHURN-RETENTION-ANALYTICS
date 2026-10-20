@echo off
title Push Customer Churn Project to GitHub
color 0b
echo =======================================================================
echo   E-COMMERCE CUSTOMER CHURN ^& RETENTION ANALYTICS - GITHUB PUSH
echo =======================================================================
echo.
echo Target Repository:
echo   https://github.com/dona-abraham/-E-COMMERCE-CUSTOMER-CHURN-RETENTION-ANALYTICS.git
echo.
echo Local Folder:
echo   %~dp0
echo.
echo -----------------------------------------------------------------------
echo NOTE: GitHub requires a Personal Access Token (PAT) as the password.
echo If prompted:
echo   Username: dona-abraham
echo   Password: [Your GitHub Personal Access Token]
echo -----------------------------------------------------------------------
echo.

cd /d "C:\Users\Lenovo\OneDrive\Desktop\DAV\Customer_Churn_And_Retension_Analysis"

"C:\Users\Lenovo\MinGit\cmd\git.exe" push -u origin main

echo.
if %ERRORLEVEL% EQU 0 (
    echo =======================================================================
    echo   SUCCESS! All project files have been successfully pushed to GitHub!
    echo =======================================================================
) else (
    echo =======================================================================
    echo   Push failed or cancelled. Please verify your GitHub token.
    echo =======================================================================
)
echo.
pause
