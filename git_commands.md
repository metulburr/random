
#add new url
```
git remote set-url --add <new_url>
```
#remove old url
```
git remote set-url --delete <old_url>
```
#set upstream
```
git remote add upstream <url>
```
#get upstream updates
```
git fetch upstream
git checkout master
git rebase upstream/master
```
#new branch
#####create branch/ and switch to branch
```
git checkout -b branch_name
```
#####add feature and push branch
```
git add .
git commit -m "msg"
git push origin branch_name
```
#####delete branch
```
git push origin :branch_name
```
