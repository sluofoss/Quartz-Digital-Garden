---
title: Windows git uses wrong SSH after Github config instructions
created: 2024-10-13T21:40
updated: 2024-10-13T21:41
---

# reconfiguring git on laptop after years of inactivity
After changing github username, github changing rsa ip, and some other potential things, I need to create another ssh key for laptop windows ps, for some reason by following the github [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), it run into `git@github.com: Permission denied (publickey)` .

By checking output of `ssh -vT git@gitlab.com` that behaves correctly it lead me to suspect something else is preventing the config from getting called from git. This windows related answer on SO fixed it. [https://stackoverflow.com/a/61163458/10249728](https://stackoverflow.com/a/61163458/10249728)