
#add new url
git remote set-url --add <new_url>
#remove old url
git remote set-url --delete <old_url>
#set upstream
git remote add upstream <url>
#get upstream updates
git fetch upstream
git checkout master
git rebase upstream/master
