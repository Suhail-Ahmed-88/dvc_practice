# DVC-for-data-version-control

This repo is for practice data version control

1. Create git repo and clone in in local
2. create mycode.py and add code to it. (it will save a csv file to a new "data"forlder")
3. Do a git add-commit-push before initializing dvc.
4. pip install dvc
5. now we do "dvc init" (Creates  .dvcignore, .dvc)
6. Now do "mkdir S3" (Creates a new S3 directory)
7. Now we do "dvc remote add -d myremote S3"
8. Next "dvc add data/"
