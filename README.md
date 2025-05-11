# DVC-for-data-version-control

This repo is for practice data version control

1. Create git repo and clone it in local.
2. Create mycode.py and add code to it. (it will save a csv file to a new "data" folder)
3. Do a git add-commit-push before initializing dvc.
4. pip install dvc
5. Now we do "dvc init" (creates .dvcignore, .dvc)
6. Now do "mkdir S3" (creates a new S3 directory)
7. Now we do "dvc remote add -d myremote S3"
8. Next "dvc add data/"
   Now it will ask to do: ("git rm -r --cached 'data'" and "git commit -m "stop tracking data"")
   Because initially we were tracking data/ folder from git so now we remove it for DVC to handle.
9. Again we do "dvc add data/" (creates data.dvc) then "git add .gitignore data.dvc"
10. Now - "dvc commit" and then "dvc push"
11. Do a git add-commit-push to mark this stage as first version of data.
12. Now make changes to mycode.py to append a new row in data, check changes via "dvc status"
13. Again - - "dvc commit" and then "dvc push"
14. Then git add-commit-push (we're saving V2 of our data at this point)
15. Check dvc/git status, everything should be upto date.
16. Now repeat step 10-12 for v3 of data.

git log --oneline

git checkout `<hash> -git checkout master`

dvc pull
