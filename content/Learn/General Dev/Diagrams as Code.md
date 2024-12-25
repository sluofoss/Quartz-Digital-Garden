---
title: Diagrams as Code
created: 2024-10-13T22:01
updated: 2024-12-26T00:05
tags:
  - diagram
---

# potential diagrams in #markdown 
- prismjs (not a diagram but do syntax highlighting of the code itself)
- plantuml (really old and mature)
- mermaid (avail in github and gitlab)
- d2 
	- (need local install compiler to generate visual, not supported out of the box)
	- have a lot of additional features than mermaid
	- https://text-to-diagram.com/?example=code&b=mermaid
	- https://github.com/terrastruct/d2?tab=readme-ov-file#install
- https://kroki.io/
  - this seems to be a website (with self host option) that offer an api call to convert encoded diagram strings to visual image for a lot of different visualization DSL
- [[Terraform]] outputs plots in graphviz DOT format.
  - below 2 source describe a way to use external/self hosted services to embed the diagram in markdown as an api call to website. 
  - http://bijanebrahimi.github.io/blog/graphviz-in-markdown.html
  - https://github.com/TLmaK0/gravizo
  - #obsidian has plugins that support graphviz. However, to render output from custom obsidian plugin feels complicated. 
    - https://joschua.io/posts/2023/09/01/obsidian-publish-dataview
      - this is trying to:
        - use some api call of the dataview plugin to convert things into markdown, 
        - embedded in any markdown doc, 
        - and then use obsidian publish.
# example of failing to rendering graphviz diagram in github readme due to multi line inside link
![Alt text]("https://g.gravizo.com/svg?
  digraph G {
    size ="4,4";
    main [shape=box];
    main -> parse [weight=8];
    parse -> execute;
    main -> init [style=dotted];
    main -> cleanup;
    execute -> { make_string; printf}
    init -> make_string;
    edge [color=red];
    main -> printf [style=bold,label="100 times"];
    make_string [label="make a string"];
    node [shape=box,style=filled,color=".7 .3 1.0"];
    execute -> compare;
  }
")
