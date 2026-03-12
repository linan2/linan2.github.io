@echo off
echo ====================================
echo Deploy to GitHub Pages
echo ====================================
echo.

REM Check if git is initialized
if not exist ".git" (
    echo Git repository not found. Initializing...
    git init
    git config user.name "linan2"
    git config user.email "linanvae@163.com"
)

REM Check if remote is configured
git remote -v | findstr "origin" >nul
if %errorlevel% neq 0 (
    echo.
    echo Configuring remote repository...
    git remote add origin https://github.com/linan2/linan.github.io.git
)

REM Stage all changes
echo Staging changes...
git add .

REM Commit changes
echo Committing changes...
git commit -m "Update website"

REM Push to GitHub
echo.
echo Pushing to GitHub...
git branch -M main
git push -u origin main

echo.
echo ====================================
echo Deployment complete!
echo ====================================
echo.
echo Your website should be available at:
echo https://linan.github.io
echo.
echo If this is your first deployment, make sure to:
echo 1. Create the repository on GitHub: https://github.com/new
echo 2. Name it exactly: linan.github.io
echo 3. Enable GitHub Pages in repository settings
echo 4. Set source to 'main' branch and '/ (root)' folder
echo.
pause
