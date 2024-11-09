---
title: enable TOC and File Explorer for quartz mobile
created: 2024-09-30T21:35
updated: 2024-09-30T21:53
---

# Incentive 

I noticed today that the table of content and explorer tab of quartz are not showing up in mobile web.

# reason

in the `quartz.layout.ts` file their quartz default are desktop only, i.e. 
    
```
Component.DesktopOnly(Component.Explorer()),
Component.DesktopOnly(Component.TableOfContents()),
```

However note that removing `Component.DesktopOnly` is not enough, because the explorer is by default open. We need it to be closed on mobile by default to save space (this class has parameter that allows it). However it does not look good in left, and `beforebody` section is below page title (this could lead to confusion). 

The effect on [quartz.eilleeenz.com/meta/Map](https://quartz.eilleeenz.com/meta/Map) looks interesting. Need to see how that can be replicated.
