# Git-Tutorial

##  A) Git rewriting Files

- Using git rebase 

<p>
1. git rebase -i HEAD~n (n stands for last n commits)<br>
2. git rebase todo file is opened in code editor<br>
3. use the followinfg commands<br>

#### Commands:<br>
p, pick <commit> = use commit<br>
r, reword <commit> = use commit, but edit the commit message<br>
e, edit <commit> = use commit, but stop for amending<br>
s, squash <commit> = use commit, but meld into previous commit<br>
f, fixup <commit> = like "squash", but discard this commit's log message<br>
x, exec <command> = run command (the rest of the line) using shell<br>
b, break = stop here (continue rebase later with 'git rebase --continue')<br>
d, drop <commit> = remove commit<br>
l, label <label> = label current HEAD with a name<br>
t, reset <label> = reset HEAD to a label<br>
m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]<br>
.       create a merge commit using the original merge commit's<br>
.       message (or the oneline, if no original merge commit was<br>
.       specified). Use -c <commit> to reword the commit message.<br>
<br>
4. After doing required changes save and close it.<br>
5. push the commit<br>
</p>


##  B) Changing remote origin
#### this will fail because `origin` is not set / `origin` does not match
- $git push origin master

#### you need to use
- $git push myOrigin master
<br>

#### If you want to rename the remote or change the remote's URL, you'll want to first remove the old remote, and then add the correct one.

1. git remote -v<br>
2. git remote add origin ssh://git@example.com:1234/myRepo.git
3. git push origin master


## C) Undo Last n commits

- $git reset --soft HEAD~n


