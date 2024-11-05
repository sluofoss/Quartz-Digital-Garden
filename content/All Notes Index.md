---
created: 2024-11-05T21:45
updated: 2024-11-05T21:57
---

```dataview
table 
	file.folder as folder
	, dateformat(updated, "yyyy-MM-dd") as updated
	, dateformat(created, "yyyy-MM-dd") as created  
from ""
sort updated desc
```
