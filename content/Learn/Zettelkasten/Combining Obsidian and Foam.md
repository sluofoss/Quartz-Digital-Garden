---
created: 2024-11-09T22:45
updated: 2024-11-09T23:35
---
# Problems:
1. obsidian is closed source and require purchase commercial license to be used for work
	1. ✅foam or logseq is the viable future.
		1. foam work in vscode, (1 less app to be installed from company IT perspective)
		2. logseq can serve web client via docker.
2. compatibility issues in migration/coexist:
	1. ✅currently uses obsidian quartz to publish (have out of the bock graph and backlink support)
	2. ✅WYSIWYG:
		1. https://github.com/zaaack/vscode-markdown-editor
		2. ‼does render mermaid plot but need to be careful how it handles things.
	3. obsidian plugins:
		1. ✅dataview
			1. nothing so far to migrate
		2. ✅templater
			1. nothing so far to migrate
		3. ✅excalidraw
			1. vscode also has this extension
		4. ❓update time on edit
            1. this plugin does 2 things: 
                1. gen front matter field on creation
                    1. can be mimic via foam-template
						1. mock up of datetime in front matter led to some weird recursive calls
						2. think this is something to do with `:` been a functional special character in templating
						3. pause for now
                2. change `updated` on modification.
                    1. ??? 
                    2. maybe github hook?
