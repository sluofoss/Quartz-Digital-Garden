---
title: Diagrams as Code
created: 2024-10-13T22:01
updated: 2024-12-26T00:55
tags:
  - diagram
---

# potential diagrams in #markdown
> [!IMPORTANT] Commonmark out of box doesn't seem to support any diagram render capability. Hence everything here is targeting some flavour of markdown.


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
    - the two source describes calling web api with multiline url. Not sure if that ever worked but currently it doesnt in github markdown nor quartz compilation. Also gravizo's readme shows a different method of feeding the link of the github readme into their website to generate the plot instead, but this is not viable cos the url for a digital garden **SHOULD NOT** be hardcoded.
  - looking to see if there are method to export diagram from [[Terraform]] in mermaid instead.
    - conversion tool from `dot` (graphviz) to mermaid not found.
    - https://github.com/RoseSecurity/Terramaid
      - custom install to convert terraform to mermaid (i.e. use this instead of `terraform graph`)
      - https://github.com/RoseSecurity/Terramaid/issues/25
        - does not support opentofu yet
    - https://github.com/hashicorp/terraform/issues/30519#issuecomment-2442465590
      - mentions 
        - terramaid
        - sed approach
          - https://www.heaton.dev/2022/05/use-terraform-graph-in-mermaidjs/
  - https://kroki.io/ has api taking diagram encoded using deflate + base64 algorithm. This can act as a substitute until one learn how to use `sed` to do dirty conversion from `dot` to `mermaid` as described in 
  - #Obsidian has plugins that support graphviz. However, to render output from custom obsidian plugin feels complicated. 
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

# example of rendering the diagram via kroki.io

> bash script that generate kroki link from .dot file(can be self hosted)
```bash

# syntax used here is bash parameter expansion
# https://stackoverflow.com/questions/2013547/assigning-default-values-to-shell-variables-with-a-single-command-in-bash
file="${1:-content/Learn/DevOps/example2.dot}"
cat $file | python -c "import sys; import base64; import zlib; print(base64.urlsafe_b64encode(zlib.compress(sys.stdin.read().encode('utf-8'), 9)).decode('ascii'))" | sed 's/^/ https:\/\/kroki.io\/graphviz\/svg\//'

```
> example .dot file of terraform graph
<details>

```dot
digraph {
compound = "true"
newrank = "true"
subgraph "root" {
  "[root] aws_instance.example"
  [label = "aws_instance.example", shape = "box"]
  "[root] aws_security_group.instance"
  [label = "aws_security_group.instance", shape =a "box"]
  "[root] provider.aws"
  [label = "provider.aws", shape = "diamond"]
  "[root] aws_instance.example" ->
  "[root] aws_security_group.instance"
  "[root] aws_security_group.instance" ->
  "[root] provider.aws"
  "[root] meta.count-boundary (EachMode fixup)" ->
  "[root] aws_instance.example"
  "[root] provider.aws (close)" ->
  "[root] aws_instance.example"
  "[root] root" ->
  "[root] meta.count-boundary (EachMode fixup)"
  "[root] root" ->
  "[root] provider.aws (close)"
  }
}
```

</details>



> result

![rendered diagram]( https://kroki.io/graphviz/svg/eNqVksFqwzAMhu95CuFTB2veYLvtuCcopSi22pgllpHtNmX03etQypbGK9nNSP__-ReSsQdB38J3pbn3nJyBN1BREqnK0UnQff0UQmpuaiXMUWUTgNqM7y3gKeysCxGdppoG7H2XHQCbDhvqRkZR8QqhRU9jv-FBbR-IgXQSG8-7g3Dy9d0-B_8lfML3wkdrSOrsnwInnV8EY7FnZ2YpZ1PB-n35IEtkU-Bj8nu9p4i1zkuM62ZcJcoZVh-o2082BHs7JP9SyFZaW-krWOmOA_0XcbuViWVR0OeIYrDcv1SXK9Ck8_s=)