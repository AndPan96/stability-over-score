# stability-over-score
Portfolio ml project on tabular data.


## Dataset
UCI Adult Income dataset[1](#references) from: [link](https://archive.ics.uci.edu/dataset/2/adult)


## Versioning
- Python==3.12.0 ([doc](https://docs.python.org/3.12/))
- matplotlib==3.10.8 ([doc](https://matplotlib.org/stable/index.html))
- pandas==2.3.3 ([doc](https://pandas.pydata.org/pandas-docs/version/2.3/index.html))
- scikit-learn==1.8.0 ([doc](https://scikit-learn.org/stable/api/index.html))

All packages except Python can be installed with: 
```
pip install -r "requirements.txt"
```


## Preprocessing
Target class y is named "class".\
y has 0 (0%) null values: no row has been filtered.\
Other features X have 0 (0%) null values: no drop or imputation is required.


## Models
### Logistic Regression
With:
- C in {0.1, 1, 10}
### RandomForest
With:
- n_estimators in {200, 400, 600}
- criterion in {"gini", "entropy", "log_loss"}
### Gradient Boosting
With:
- n_estimators in {200, 400, 600}
- subsample in {0.4, 0.7, 1}
### Multi Layer Perceptron
With:
- hidden_layer_sizes in {(32,),(64,),(128,),(64,32)}
- alpha in {0.0001, 0.001}


## Setup
10 seeds have been randomly generated in the interval [0,1_000_000] and hardcoded in the SEEDS constant.\
In a Step 1, all models configurations, obtained as the cartesian product of all their hyperparameters (grid search), are trained on the 3 seeds (0-2).\
Not number features get preprocessed by 1-hot encoding, while, only in Logistic Regression and Multi Layer Perceptron, number features get centered and scaled.\
Models are considered to be divided in families corresponding to their Hp class prototypes.\
For each family, the top 30% models in accuracy (rounding by excess) get selected and pass to Step 2.\
In Step 2, models are trained on the remaining 7 seeds (3-9).\
Models are evaluated using as a score accuracy mean - 1.5 std, to promote stability.\
The top 2 (at most) get selected for plotting, using the training Mode y as a baseline.

## Results
Relative Confusion Matrix entries get plot (mean and +- 3 std).\
All models are Pareto Optimal wrt the Mode, showing effective training.\
None of the selected models shows high variability over seeds, which suggests robustness under iid assumptions.\
None of the selected models shows high variability within families, which suggests that the more stable configurations of each family did not benefit from inductive bias apart, not accounted by the family selection.\
GradientBoosting show a slight but systematic better performance than other families, that suggests the inductive bias of the boosting family may be more effective to model the underlying distribution.
![not found in path](fig\plot.png)


## References
1. Becker, B. & Kohavi, R. (1996). Adult [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5XW20.
