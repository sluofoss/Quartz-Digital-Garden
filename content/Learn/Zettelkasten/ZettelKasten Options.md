---
created: 2024-10-17T01:27
updated: 2024-11-09T22:22
---
# Requirements:

## mandatory

- uses #markdown
- support back linking between codes
- support note linkage graph
- auto update time on edit
- 

## optional

- #obsidian-dataview
- #obsidian-templater
- #excalidraw

# Options:

- #Obsidian

  - proprietary
  - more plugins.
  - ### Publish

    - easily publish digital garden using foss with quartz.
- #Logseq

  - foss
  - the graph view after publish seems much better.
  - growing github star

    - [GitHub Star History (star-history.com)](https://star-history.com/#logseq/logseq&Date)
  - ### Publish


    - https://discuss.logseq.com/t/how-to-publish-your-logseq-as-selfhosted-site/16412
    - https://docs.logseq.com/#/page/publishing
    - https://candideu.github.io/logseq-demo-graph-site-export/#/page/publishing%20your%20graph%20online
  - ### good features


    - have docker container that can be used to self host.
      - cloudflare tunnel authentication access
      - [Is it possible to allow access only to specified users? - Zero Trust - Cloudflare Community](https://community.cloudflare.com/t/is-it-possible-to-allow-access-only-to-specified-users/640574)
      - [Setup your Domain using Cloudflare Tunnels and Zero Trust (noted.lol)](https://noted.lol/cloudflare-tunnel-and-zero-trust/)
      - [selfhost remote logseq instance - auth : r/logseq (reddit.com)](https://www.reddit.com/r/logseq/comments/1ajx9qx/selfhost_remote_logseq_instance_auth/)
      - [Restricting Access with HTTP Basic Authentication | NGINX Documentation](https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/)
      - [logseq/docs/docker-web-app-guide.md at master · logseq/logseq (github.com)](https://github.com/logseq/logseq/blob/master/docs/docker-web-app-guide.md)
    - temporary web version
      - [https://demo.logseq.com/#/](https://demo.logseq.com/#/)
    - also have excalidraw plugin
    - [haydenull/logseq-plugin-excalidraw (github.com)](https://github.com/haydenull/logseq-plugin-excalidraw)
  - ### current issues


    - doesnt work on firefox properly? There are talk to migrate it from electron (chromium based) to Tauri.
      - https://v2.tauri.app/
      - https://github.com/logseq/logseq/discussions/5875
      - https://www.reddit.com/r/logseq/comments/1frzi3j/firefox_not_supported/
    - logseq not on google play, but on apple store
    - logseq apk performance on mobile apparent have issues on low spec devices.
    - people are getting impatient for feature development. Apparently the database (db) version (speed up local caching) has been in development for a while.
      - [Database version (closed alpha test started) on Logseq Roadmap | Trello](https://trello.com/c/0hUluTN4/1128-database-version-closed-alpha-test-started)
- vscode/vscodium + #foam

  - version 0.26 graph have issue in github codespace (local works fine)
    - revert to vsix version 0.25.12 solves the issue.
  - use .vscode/settings.json to filter out folders that should not be included in the graph
    - need to include file name as part of the title tag in frontmatter
    - (try not to include emoji cos that might mess with file path on some system)
- vscode/vscodium + #foam + #logseq + #loam

  - #loam is vscode extension
- vscode/vscodium + #dendron

  - in maintenance mode, no longer in active development.
- #Joplin

  - foss
- #tana

  - https://tana.inc/engineering
  - https://www.reddit.com/r/logseq/comments/1epxcm5/when_logseq_db_will_be_available_to_the_public_in/
