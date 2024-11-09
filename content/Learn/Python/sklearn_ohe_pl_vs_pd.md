---
title: sklearn_ohe_pl_vs_pd
created: 2024-09-30T21:35
updated: 2024-09-30T21:53
---


```python
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import polars as pl

rows = 1_000_000
kv = {
    chr(i+65): list([str(x%i) for x in range(rows)]) 
    #i: list([str(x%i) for x in range(rows)]),
    #i: list([chr(x%26+65) for x in range(rows)]),
    for i in range(2,23)
}
kv['id'] = list(range(rows))
x_pd = pd.DataFrame(kv)
x_pl = pl.DataFrame(kv)
```


```python
cat_columns = [ x for x in kv.keys() if x not in ('id')]
```


```python
len(cat_columns)
```




    21



# pandas


```python
import sklearn
sklearn.set_config(transform_output='pandas')
tf = OneHotEncoder(sparse_output=False)
X_out = tf.fit_transform(x_pd[cat_columns])
```


```python
X_out
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C_0</th>
      <th>C_1</th>
      <th>D_0</th>
      <th>D_1</th>
      <th>D_2</th>
      <th>E_0</th>
      <th>E_1</th>
      <th>E_2</th>
      <th>E_3</th>
      <th>F_0</th>
      <th>...</th>
      <th>W_2</th>
      <th>W_20</th>
      <th>W_21</th>
      <th>W_3</th>
      <th>W_4</th>
      <th>W_5</th>
      <th>W_6</th>
      <th>W_7</th>
      <th>W_8</th>
      <th>W_9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>999995</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>999996</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>999997</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>999998</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>999999</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>1000000 rows × 252 columns</p>
</div>




```python
tf.categories_
```




    [array(['0', '1'], dtype=object),
     array(['0', '1', '2'], dtype=object),
     array(['0', '1', '2', '3'], dtype=object),
     array(['0', '1', '2', '3', '4'], dtype=object),
     array(['0', '1', '2', '3', '4', '5'], dtype=object),
     array(['0', '1', '2', '3', '4', '5', '6'], dtype=object),
     array(['0', '1', '2', '3', '4', '5', '6', '7'], dtype=object),
     array(['0', '1', '2', '3', '4', '5', '6', '7', '8'], dtype=object),
     array(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], dtype=object),
     array(['0', '1', '10', '2', '3', '4', '5', '6', '7', '8', '9'],
           dtype=object),
     array(['0', '1', '10', '11', '2', '3', '4', '5', '6', '7', '8', '9'],
           dtype=object),
     array(['0', '1', '10', '11', '12', '2', '3', '4', '5', '6', '7', '8', '9'],
           dtype=object),
     array(['0', '1', '10', '11', '12', '13', '2', '3', '4', '5', '6', '7',
            '8', '9'], dtype=object),
     array(['0', '1', '10', '11', '12', '13', '14', '2', '3', '4', '5', '6',
            '7', '8', '9'], dtype=object),
     array(['0', '1', '10', '11', '12', '13', '14', '15', '2', '3', '4', '5',
            '6', '7', '8', '9'], dtype=object),
     array(['0', '1', '10', '11', '12', '13', '14', '15', '16', '2', '3', '4',
            '5', '6', '7', '8', '9'], dtype=object),
     array(['0', '1', '10', '11', '12', '13', '14', '15', '16', '17', '2', '3',
            '4', '5', '6', '7', '8', '9'], dtype=object),
     array(['0', '1', '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '2', '3', '4', '5', '6', '7', '8', '9'], dtype=object),
     array(['0', '1', '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '19', '2', '3', '4', '5', '6', '7', '8', '9'], dtype=object),
     array(['0', '1', '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '19', '2', '20', '3', '4', '5', '6', '7', '8', '9'], dtype=object),
     array(['0', '1', '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '19', '2', '20', '21', '3', '4', '5', '6', '7', '8', '9'],
           dtype=object)]




```python
tf.get_feature_names_out()
```




    array(['C_0', 'C_1', 'D_0', 'D_1', 'D_2', 'E_0', 'E_1', 'E_2', 'E_3',
           'F_0', 'F_1', 'F_2', 'F_3', 'F_4', 'G_0', 'G_1', 'G_2', 'G_3',
           'G_4', 'G_5', 'H_0', 'H_1', 'H_2', 'H_3', 'H_4', 'H_5', 'H_6',
           'I_0', 'I_1', 'I_2', 'I_3', 'I_4', 'I_5', 'I_6', 'I_7', 'J_0',
           'J_1', 'J_2', 'J_3', 'J_4', 'J_5', 'J_6', 'J_7', 'J_8', 'K_0',
           'K_1', 'K_2', 'K_3', 'K_4', 'K_5', 'K_6', 'K_7', 'K_8', 'K_9',
           'L_0', 'L_1', 'L_10', 'L_2', 'L_3', 'L_4', 'L_5', 'L_6', 'L_7',
           'L_8', 'L_9', 'M_0', 'M_1', 'M_10', 'M_11', 'M_2', 'M_3', 'M_4',
           'M_5', 'M_6', 'M_7', 'M_8', 'M_9', 'N_0', 'N_1', 'N_10', 'N_11',
           'N_12', 'N_2', 'N_3', 'N_4', 'N_5', 'N_6', 'N_7', 'N_8', 'N_9',
           'O_0', 'O_1', 'O_10', 'O_11', 'O_12', 'O_13', 'O_2', 'O_3', 'O_4',
           'O_5', 'O_6', 'O_7', 'O_8', 'O_9', 'P_0', 'P_1', 'P_10', 'P_11',
           'P_12', 'P_13', 'P_14', 'P_2', 'P_3', 'P_4', 'P_5', 'P_6', 'P_7',
           'P_8', 'P_9', 'Q_0', 'Q_1', 'Q_10', 'Q_11', 'Q_12', 'Q_13', 'Q_14',
           'Q_15', 'Q_2', 'Q_3', 'Q_4', 'Q_5', 'Q_6', 'Q_7', 'Q_8', 'Q_9',
           'R_0', 'R_1', 'R_10', 'R_11', 'R_12', 'R_13', 'R_14', 'R_15',
           'R_16', 'R_2', 'R_3', 'R_4', 'R_5', 'R_6', 'R_7', 'R_8', 'R_9',
           'S_0', 'S_1', 'S_10', 'S_11', 'S_12', 'S_13', 'S_14', 'S_15',
           'S_16', 'S_17', 'S_2', 'S_3', 'S_4', 'S_5', 'S_6', 'S_7', 'S_8',
           'S_9', 'T_0', 'T_1', 'T_10', 'T_11', 'T_12', 'T_13', 'T_14',
           'T_15', 'T_16', 'T_17', 'T_18', 'T_2', 'T_3', 'T_4', 'T_5', 'T_6',
           'T_7', 'T_8', 'T_9', 'U_0', 'U_1', 'U_10', 'U_11', 'U_12', 'U_13',
           'U_14', 'U_15', 'U_16', 'U_17', 'U_18', 'U_19', 'U_2', 'U_3',
           'U_4', 'U_5', 'U_6', 'U_7', 'U_8', 'U_9', 'V_0', 'V_1', 'V_10',
           'V_11', 'V_12', 'V_13', 'V_14', 'V_15', 'V_16', 'V_17', 'V_18',
           'V_19', 'V_2', 'V_20', 'V_3', 'V_4', 'V_5', 'V_6', 'V_7', 'V_8',
           'V_9', 'W_0', 'W_1', 'W_10', 'W_11', 'W_12', 'W_13', 'W_14',
           'W_15', 'W_16', 'W_17', 'W_18', 'W_19', 'W_2', 'W_20', 'W_21',
           'W_3', 'W_4', 'W_5', 'W_6', 'W_7', 'W_8', 'W_9'], dtype=object)



# polars


```python
import sklearn
sklearn.set_config(transform_output='polars')
tf = OneHotEncoder(sparse_output=False)
X_out = tf.fit_transform(x_pl[cat_columns])
```


```python
X_out
```




<div><style>
.dataframe > thead > tr,
.dataframe > tbody > tr {
  text-align: right;
  white-space: pre-wrap;
}
</style>
<small>shape: (1_000_000, 252)</small><table border="1" class="dataframe"><thead><tr><th>C_0</th><th>C_1</th><th>D_0</th><th>D_1</th><th>D_2</th><th>E_0</th><th>E_1</th><th>E_2</th><th>E_3</th><th>F_0</th><th>F_1</th><th>F_2</th><th>F_3</th><th>F_4</th><th>G_0</th><th>G_1</th><th>G_2</th><th>G_3</th><th>G_4</th><th>G_5</th><th>H_0</th><th>H_1</th><th>H_2</th><th>H_3</th><th>H_4</th><th>H_5</th><th>H_6</th><th>I_0</th><th>I_1</th><th>I_2</th><th>I_3</th><th>I_4</th><th>I_5</th><th>I_6</th><th>I_7</th><th>J_0</th><th>J_1</th><th>&hellip;</th><th>V_14</th><th>V_15</th><th>V_16</th><th>V_17</th><th>V_18</th><th>V_19</th><th>V_2</th><th>V_20</th><th>V_3</th><th>V_4</th><th>V_5</th><th>V_6</th><th>V_7</th><th>V_8</th><th>V_9</th><th>W_0</th><th>W_1</th><th>W_10</th><th>W_11</th><th>W_12</th><th>W_13</th><th>W_14</th><th>W_15</th><th>W_16</th><th>W_17</th><th>W_18</th><th>W_19</th><th>W_2</th><th>W_20</th><th>W_21</th><th>W_3</th><th>W_4</th><th>W_5</th><th>W_6</th><th>W_7</th><th>W_8</th><th>W_9</th></tr><tr><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>&hellip;</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td></tr></thead><tbody><tr><td>1.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>&hellip;</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>0.0</td><td>1.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>&hellip;</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>&hellip;</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>0.0</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>&hellip;</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>&hellip;</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td></tr><tr><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>&hellip;</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td></tr><tr><td>1.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>&hellip;</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td></tr><tr><td>0.0</td><td>1.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>&hellip;</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td></tr><tr><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>&hellip;</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>0.0</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>1.0</td><td>0.0</td><td>&hellip;</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></tbody></table></div>



# sparse numpy

### onehot is faster in pandas than polars


```python
import sklearn
sklearn.set_config(transform_output='default')
tf = OneHotEncoder(sparse_output=True)
X_out = tf.fit_transform(x_pl[cat_columns])
print(X_out)
```

    <Compressed Sparse Row sparse matrix of dtype 'float64'
    	with 21000000 stored elements and shape (1000000, 252)>
      Coords	Values
      (0, 0)	1.0
      (0, 2)	1.0
      (0, 5)	1.0
      (0, 9)	1.0
      (0, 14)	1.0
      (0, 20)	1.0
      (0, 27)	1.0
      (0, 35)	1.0
      (0, 44)	1.0
      (0, 54)	1.0
      (0, 65)	1.0
      (0, 77)	1.0
      (0, 90)	1.0
      (0, 104)	1.0
      (0, 119)	1.0
      (0, 135)	1.0
      (0, 152)	1.0
      (0, 170)	1.0
      (0, 189)	1.0
      (0, 209)	1.0
      (0, 230)	1.0
      (1, 1)	1.0
      (1, 3)	1.0
      (1, 6)	1.0
      (1, 10)	1.0
      :	:
      (999998, 188)	1.0
      (999998, 199)	1.0
      (999998, 222)	1.0
      (999998, 232)	1.0
      (999999, 1)	1.0
      (999999, 2)	1.0
      (999999, 8)	1.0
      (999999, 13)	1.0
      (999999, 17)	1.0
      (999999, 20)	1.0
      (999999, 34)	1.0
      (999999, 35)	1.0
      (999999, 53)	1.0
      (999999, 54)	1.0
      (999999, 70)	1.0
      (999999, 77)	1.0
      (999999, 101)	1.0
      (999999, 118)	1.0
      (999999, 126)	1.0
      (999999, 150)	1.0
      (999999, 169)	1.0
      (999999, 172)	1.0
      (999999, 200)	1.0
      (999999, 209)	1.0
      (999999, 233)	1.0



```python
import sklearn
sklearn.set_config(transform_output='default')
tf = OneHotEncoder(sparse_output=True)
X_out = tf.fit_transform(x_pd[cat_columns])
print(X_out)
```

    <Compressed Sparse Row sparse matrix of dtype 'float64'
    	with 21000000 stored elements and shape (1000000, 252)>
      Coords	Values
      (0, 0)	1.0
      (0, 2)	1.0
      (0, 5)	1.0
      (0, 9)	1.0
      (0, 14)	1.0
      (0, 20)	1.0
      (0, 27)	1.0
      (0, 35)	1.0
      (0, 44)	1.0
      (0, 54)	1.0
      (0, 65)	1.0
      (0, 77)	1.0
      (0, 90)	1.0
      (0, 104)	1.0
      (0, 119)	1.0
      (0, 135)	1.0
      (0, 152)	1.0
      (0, 170)	1.0
      (0, 189)	1.0
      (0, 209)	1.0
      (0, 230)	1.0
      (1, 1)	1.0
      (1, 3)	1.0
      (1, 6)	1.0
      (1, 10)	1.0
      :	:
      (999998, 188)	1.0
      (999998, 199)	1.0
      (999998, 222)	1.0
      (999998, 232)	1.0
      (999999, 1)	1.0
      (999999, 2)	1.0
      (999999, 8)	1.0
      (999999, 13)	1.0
      (999999, 17)	1.0
      (999999, 20)	1.0
      (999999, 34)	1.0
      (999999, 35)	1.0
      (999999, 53)	1.0
      (999999, 54)	1.0
      (999999, 70)	1.0
      (999999, 77)	1.0
      (999999, 101)	1.0
      (999999, 118)	1.0
      (999999, 126)	1.0
      (999999, 150)	1.0
      (999999, 169)	1.0
      (999999, 172)	1.0
      (999999, 200)	1.0
      (999999, 209)	1.0
      (999999, 233)	1.0


- sparse pd < sparse polars < pd < polars 
