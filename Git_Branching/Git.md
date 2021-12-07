# Git

Learning notes from [Learn Git Branching](https://learngitbranching.js.org/?NODEMO=&locale=zh_CN) ([Github](https://github.com/pcottle/learnGitBranching))



## Basic Commands

### Commit

- `git commit`: Commit a new modification (child) node in the current branch

### Branch

- `git branch <branchname>`: Create a new branch
- `git checkout <branchname>`: Turn to the specific branch
- `git checkout -b <branchname>`: Create and turn to a new branch

### Merge

- `git merge <branchname>`: Merge the specific branch to the current branch (e.g. merging to `main` branch means that now `main` branch includes all modifications from the other branch)

### Rebase

Take out series of modification records and duplicate to store in another place (make more linearlized committing history)

- `git rebase <branchname>`: Transfer the current branch node to the node that right after the one in the specific branch (actually duplication)
- `git rebase <branchname_A> <branchname_B>`: B (as well as nodes above B) will be placed after A



## Features

Move on the commit tree

### HEAD

`HEAD` always points to the latest commit record. Most of the commit commands start from changing the direction of `HEAD`. Usually `HEAD` points to the branchname.

- `cat .git/HEAD` or `git symbolic-ref HEAD`: The pointing direction of `HEAD`

 **Splitting `HEAD`:** 

- `git checkout <node_Hash>`: Make it points to a specific <u>commit node</u> rather than the branch

### Relative Reference

From the previous section, if want to specific a node in the commit log, Hash value is needed. (Not convenient)

- `git log`: Checkout the Hash value of a specific commit log (SHA-1, 40 digits)

**Relative reference:** (e.g., `git checkout HEAD^`)

- `^`: 1 node (commit) upward (e.g., `main^` is the parental node of `main`, also `main^^` can be used)
- `~<num>`: several nodes upward

**Forced branch position change** (`-f`)

- `git branch -f main HEAD~3`: Force `main` branch points to `HEAD~3` position

### Reset Changes

- `git reset HEAD~1`: Back to the previous node, the current node cannot be found (actually still exist, but not added to temp)  (Not works in remote)
- `git revert HEAD`: Create a new commit after the current node, but the new node is the copy of the previous node (e.g., revert C2, than create C2’ with same status as C1)



##  Organize Commit Tree

### Cherry-pick

- `git cherry-pick <commit_Hash>`: Duplicate some commits under the current position (`HEAD`) (Good for commits with known Hash values)

### Interactive Rebase

- `--interactive` or `-i` (after the commands): Open a text file (in *Vim*) for commit log (Good for commits w/o. known Hash values)

  (e.g., `git rebase -i HEAD~4`: The interactive mode will show 4 steps before `HEAD` (including `HEAD`))

Used for: (actually creates a new “current” branch)

- Adjust the order of the commits
- Delete unwanted commits (through switching the `pick` mode): `omit` / `pick`
- Merge commits



## Techniques and Tips

### Local Stack Commit

When debugging some debug sentences were added and printed in the `bugFix` branch, but they shouldn’t be included in the `main` branch after debugging. (If use fast-forward)

Solution: Only duplicate the final commit which solved all problems (in the `bugFix` branch)

- `git rebase -i`
- `git cherry-pick`

### Modify

On a node a commit is done, a new branch is created and another commit on that branch is done. But we want to modify this old node.

- `rebase -i`

  Steps: (Requires 2 times of re-ordering, not convenient)

  1. `git rebase -i`: Re-order the commits and rank up the commit which is wanted to be modified
  2. `git commit --amend`: Small modifications are done
  3. `git rebase -i`: Re-order to the original sequence
  4. Move `main` to the latest modification (e.g., `git branch -f main HEAD` or `git rebase main <node>`)

- `cherry-pick`

  Step: (`cherry-pick` could be applied anywhere except for the upstream of `HEAD`)

  1. `git cherry-pick`: Pick the one needed to be modified
  2. `git commit --amend`
  3. `git cherry-pick`: Pick again to re-order the following nodes to the modified node (This time the `main` is directly on the latest node)

### Tags

Sometimes we want some permanent links pointing to some specific commits. (Role of anchor points)

- `git tag <tag_name> <commit_Hash>`: If no `commit` is specified, the tag is pointed to `HEAD` (Usually use `v1` to represent the Version 1.0)

### Describe

- `git describe <ref>`: Describe the nearest tag (Good to be used with `git bisect`)

  (`git bisect`: A command to find the commit record that generated the bug)

- `<ref>`: Any stuff which can be recognized by Git as the commit record (`HEAD` if not specified)

Output: `<tag>_<numCommits>_g<hash>` (when `ref` has a `tag`, the output will be only the tag name)

- `tag`: Closest `tag` with `ref`
- `numCommits`: The number of commits from the `ref` to the `tag`
- `hash`: the leading digits of the hash value of the `ref`

### Parental Commit

`^` can also be followed by some digits. It means the specific parental commit node (after merging there will be several parental nodes)

`^n` & `~n` can be combined to use in complicated branch networks. This also supports chain operation (e.g., `HEAD^2~3`)



## Remote (Push & Pull)

### Clone

When using GitHub, we want a copy from the remote repository

- `git clone`: Copy the remote repository to local

### Remote Branch

After `git clone`, a new branch `origin/main` in the original repository is generated. It is so called “remote branch”. It reflects the state from the latest communication. Another feature of remote branches is that when log out, `HEAD` will be splitted automatically. 

- `origin/main`: `<remote_name>/<branch_name>`, `origin` is usually the name of the remote repository

If in the current repository, for `origin/main`, `git commit` only creates commit with a splitted `HEAD` and both `main` & `orgin/main` does not move. Neither does `main` in the remote repo. The update will be done only after the corresponding branch in the remote repository updates.

### Fetch

Fetch data from the remote repository. Usually through `http://` or `git://` protocol

- `git fetch`: If new commits are in the remote repository, the change will be synchornized to the local repository and local `origin/main` points to where the `main` in the remote repository points to. 

This only downloads what is missing and modifies the remote branch pointers. It doesn’t modify the local files, or update the local `main` branch

### Pull

After fetching data, we should update to the practical work

Conventionally, the operations can be 

- `git cherry-pick origin/main`
- `git rebase origin/main`
- `git merge origin/main`

To combine the fetching and merging operations:

- `git pull` == `fetch` + `merge`

### Push

- `git push`: Update the local change to specific remote repository

  if not specify, `git push` will call configuration file `push.default` (depending on the Git version, here is `upstream`)

### Deviation

If there is too much deviation from the previous sync. from between the local and the remote repository (or another commit has already written at the same position), `push` can be failed.

- `rebase`

  Adjust the working branch based on the latest remote branch

  1. `git fetch`: Fetch the latest remote branch
  2. `git rebase origin/main`: move our work to the new commit record
  3. `git push`

  OR

  1. `git pull --rebase` (`fetch` + `rebase`) 
  2.  `git push`

- `merge` 

  Tells that the changes in the latest commits have already been merged in the new commit and the new commit has 2 parental nodes (same as the normal merge)

  1. `git fetch`
  2. `git merge origin/main`
  3. `git push`

  OR

  1. `git pull` (`fetch` + `merge`) 
  2. `git push`

### Locked Main

**Remote Rejected**: If working in a big team, this can be a reason of the locked `main`. It requires some Pull Request processes to modify. If just commit to local and push, error messages can appear.

Solution: Create a new branch and apply for the pull request

### Practically

The process should be:

1. Modify the files locally
2. `git add <file_name>`
3. `git commit` or `git commit --amend`
4. `git push` (better to `pull` before `push`)



## Advanced Operations in Remote

### Rebase (in Remote)

In practical work, usually developers work in a feature branch splitted from the `main` branch. Only one time of combination should be applied. But sometimes some developers only `push`/`pull` on the `main` branch.

The following workflow integrates 2 steps:

1. Integrate all feature branches into `main`
2. Push and update the remote branch

Operations:

1. `git pull --rebase`: `rebase` our work to the latest commit of the remote branch
2. `git push`

### Merge (in Remote)

Differences between `rebase` & `merge`

- `rebase`: Makes the commit tree in neat in one line, but modifies the commit order
- `merge`: Good for those who love maintaining all history of commits

### Tracking

`main` is set to track `o/main` (This property is configured when cloning)

In default:

> - `local branch "main" set to track remote branch "o/main"` (when clone succeeded)

If want to specify a new branch name:

- `git checkout -b <new_branch_name> o/main`: Specify a new branch to track `o/main` 

  In this case, `git pull` has `o/main` and the new branch updated with remote repository, but `main` is not updated (also valid for `git push` to push a not `o/main` branch to the remote repository)

-  `git branch -u o/main <new_branch_name>`: The new branch is tracking `o/main`. (If currently in this branch `git branch -u o/main` is enough)

### Push Parameters

- `git push <remote> <place>`: Setting the remote repository and branch without locating at the corresponding position

  (e.g., `git push origin main`: Checkout `main` in the local repository. Compare all commits with that in the `main` branch of the remote repository “`origin`” and add the missing ones)

- `git push <remote> <source>:<destination>`: Stuff in `<place>` (refspec) is now specified. This time can push a source branch to a destination branch with different name (`<source>`, `<destination>` and other “refspecs” can be relative reference, and the `<destination>` can be a new branch)

### Fetch Parameters

Similar to the `push` parameters, but the uploads become downloads

- `git fetch <remote> <place>`: Download the missing files from the remote repository to local `o/<place>`

  (If use `<source>:<destination>` for `<place>`, the `<source>` should be the remote position)

 ### Empty Source

No `<source>`, but remain `:<destination>`

e.g.,

- `git push origin :side`: Delete the remote `side` branch
- `git fetch origin :bugFix`: Create a new branch `bugFix` in local repository

### Pull Parameters

`pull` only focus on the final commit position

- `git pull origin foo` == `git fetch origin foo; git merge o/foo` (no matter what happened in the `<destination>`, finally will be merged to the original branch)
- `git pull origin bar~1:bugFix` == `git fetch origin bar~1:bugFix; git merge bugFix`

