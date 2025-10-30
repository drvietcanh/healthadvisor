@echo off
echo ========================================
echo   HEALTHADVISOR - DEPLOY SCRIPT
echo ========================================
echo.

echo [DONE] Git da khoi tao
echo [DONE] Code da commit thanh cong
echo [DONE] Branch main da san sang
echo.

echo ========================================
echo   CAC BUOC BAN CAN LAM TIEP:
echo ========================================
echo.

echo BUOC 1: TAO GITHUB REPOSITORY
echo ------------------------------
echo 1. Mo trinh duyet: https://github.com/new
echo 2. Dang nhap GitHub
echo 3. Dien thong tin:
echo    - Repository name: healthadvisor
echo    - Description: Ung dung tu van suc khoe AI
echo    - Chon: Public
echo    - KHONG tich: Add README, .gitignore
echo 4. Click: Create repository
echo.
pause

echo.
echo BUOC 2: LAY USERNAME GITHUB
echo --------------------------
set /p GITHUB_USER="Nhap username GitHub cua ban: "
echo.

echo BUOC 3: KET NOI VOI GITHUB
echo --------------------------
echo Dang ket noi voi GitHub...
git remote add origin https://github.com/%GITHUB_USER%/healthadvisor.git

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Ket noi that bai!
    echo Neu da co remote, chay lenh:
    echo   git remote remove origin
    echo Roi chay lai script nay.
    pause
    exit /b 1
)

echo [DONE] Ket noi thanh cong!
echo.

echo BUOC 4: PUSH LEN GITHUB
echo -----------------------
echo Dang push code len GitHub...
echo (Neu hoi password, dung GitHub Personal Access Token)
echo.

git push -u origin main

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Push that bai!
    echo.
    echo >>> HUONG DAN LAY TOKEN:
    echo 1. Mo: https://github.com/settings/tokens
    echo 2. Click: Generate new token ^(classic^)
    echo 3. Ten: healthadvisor-deploy
    echo 4. Chon: repo ^(tich tat ca^)
    echo 5. Click: Generate token
    echo 6. COPY token ^(chi hien 1 lan!^)
    echo 7. Git hoi password: DAN TOKEN vao
    echo.
    echo Sau do chay lai lenh:
    echo   git push -u origin main
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   PUSH THANH CONG!
echo ========================================
echo.
echo Code da len GitHub: https://github.com/%GITHUB_USER%/healthadvisor
echo.

echo BUOC 5: DEPLOY TREN STREAMLIT CLOUD
echo ------------------------------------
echo.
echo 1. Mo: https://share.streamlit.io
echo 2. Click: Sign in with GitHub
echo 3. Click: New app
echo 4. Chon:
echo    - Repository: %GITHUB_USER%/healthadvisor
echo    - Branch: main
echo    - Main file path: app.py
echo 5. Click: Deploy!
echo.
echo Cho 2-5 phut de deploy xong.
echo.

echo ========================================
echo   HOAN THANH!
echo ========================================
echo.
echo App cua ban se LIVE tai:
echo https://YOUR-APP-NAME.streamlit.app
echo.
echo [TUY CHON] Them OpenAI API Key:
echo - Vao Settings ^> Secrets tren Streamlit Cloud
echo - Them: OPENAI_API_KEY = "sk-your-key"
echo.

pause

