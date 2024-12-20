---
title: Dash
created: 2024-12-20
updated: 2024-12-20
tags:
    - plotly
---


# Features
- deploy via container
- each instance by principle should be independent
- each session by principle should be independent
- shared data access can be achieved using dcc.store and #redis or #flask cache


# how to build reuseable modularized component
https://dash.plotly.com/all-in-one-components

# how to separate callback and layout into separate files
❓ Should this even be necessary if one can do component composition?

below mentions `because now you have stuff scattered all over.`
> https://community.plotly.com/t/splitting-callback-definitions-in-multiple-files/10583/5
https://stackoverflow.com/questions/62102453/how-to-define-callbacks-in-separate-files-plotly-dash


# free hosting
https://render.com/pricing
https://community.plotly.com/t/free-hosting-platforms-for-python-web-app/75850/2

# give custom name to downloaded table file
https://stackoverflow.com/questions/67025512/how-to-change-filename-of-exported-dash-datatable
https://github.com/plotly/dash-table/issues/636