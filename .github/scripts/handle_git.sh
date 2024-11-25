git config --global user.name "GitHub Actions"
git config --global user.email "actions@github.com"
git add .
git commit -m "Automated commit from GitHub Action"
git remote set-url origin https://$GITHUB_TOKEN@github.com/$REPO_FOR_PUSH
#git push origin main