@echo off
echo ====================================
echo Push to GitHub Repository
echo ====================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git is not installed or not in PATH
    echo Please install Git from: https://git-scm.com/
    pause
    exit /b 1
)

REM Check if in correct directory
if not exist ".git" (
    echo ❌ Not in a Git repository
    echo Please navigate to the project directory
    pause
    exit /b 1
)

REM Check for uncommitted changes
echo Checking for changes...
git status --porcelain | findstr /r /c:"." >nul
if %errorlevel% equ 0 (
    echo ✅ Found uncommitted changes
    echo.
    
    REM Stage all changes
    echo Staging changes...
    git add .
    
    REM Commit changes
    set /p commit_msg="Enter commit message (or press Enter for default): "
    if "%commit_msg%"=="" (
        set "commit_msg=Update website"
    )
    echo Committing: %commit_msg%
    git commit -m "%commit_msg%"
) else (
    echo ℹ️  No changes to commit
)

REM Push to GitHub
echo.
echo Pushing to GitHub...
git push origin main

if %errorlevel% equ 0 (
    echo.
    echo ====================================
    echo ✅ Push completed successfully!
    echo ====================================
    echo.
    echo Your website should be available at:
    echo https://linan2.github.io
    echo.
) else (
    echo.
    echo ====================================
    echo ❌ Push failed
    echo ====================================
    echo.
    echo Common solutions:
    echo 1. Check your network connection
    echo 2. Verify your GitHub credentials
    echo 3. Try using SSH instead of HTTPS
    echo 4. Use GitHub Desktop for easier authentication
    echo.
    echo For detailed instructions, see PUSH.md
)

pause
