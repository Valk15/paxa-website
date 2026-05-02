Set-Location "C:\Users\lenovo\OneDrive\Desktop\Ai Projects\paxa-website"

# Force remove lock file
$lockFile = ".git\index.lock"
if (Test-Path $lockFile) {
    Remove-Item -Force $lockFile
    Write-Host "Lock file removed." -ForegroundColor Green
} else {
    Write-Host "No lock file found." -ForegroundColor Yellow
}

# Git operations
git add blog/separation-anxiety-vs-boredom-dogs/index.html
git add blog/index.html
git add images/separation-anxiety-vs-boredom-dogs.jpg
git add sitemap.xml
git status
git commit -m "Add blog post: Dog Separation Anxiety vs Boredom (SEO-optimised)"
git push origin main
Write-Host ""
Write-Host "=== COMPLETE ===" -ForegroundColor Green
Read-Host "Press Enter to close"
