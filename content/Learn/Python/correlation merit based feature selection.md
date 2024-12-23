---
title: correlation merit based feature selection
created: 2024-09-30T21:35
updated: 2024-11-06T00:24
tags:
  - data-science
---


# general info on feature selection
https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/

Attempt was made at using the below algorithm for a 500 feature dataset. 
https://johfischer.com/2021/08/06/correlation-based-feature-selection-in-python-from-scratch/
The time complexity is questionable at best.

Hence, an attempt was made at only considering best combo suggested by dendrogram from hierarchical cluster based on feature correlation.
https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html
https://www.kaggle.com/code/sgalella/correlation-heatmaps-with-hierarchical-clustering
- [ ] code tba

also, the following implementation of the same algo (I think?) is found. maybe it's faster? need further investigation when free.
https://github.com/ZixiaoShen/Correlation-based-Feature-Selection/blob/master/CFSmethod/CFS.py

This only considers binary classification.
