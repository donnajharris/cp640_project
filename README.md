# CP640 Machine Learning project (Spring 2022)

An indepedently researched and implemented machine learning project in the Master of Computer Science program at Wilfrid Laurier University.

## Overview

I took historical Major League Baseball data from a Kaggle dataset (as determined by the project requirements) and ran some experiments in an attempt to predict future batting success.

Kaggle dataset source: https://www.kaggle.com/datasets/darinhawley/mlb-batting-stats-by-game-19012021

The project, as submitted, was too large to be included on GitHub. As a result, the project .zip file (which includes the data files described in the Jupyter notebooks on GitHub) [is available for download here](https://donnajharris.xyz/cp640s22fp/harr2890_project.zip).

#### Project Deliverables

The complete set of project deliverables includes:

- [a proposal document](https://github.com/donnajharris/cp640_project/blob/main/deliverables/cp640_proposal_DonnaHarris.pdf)
- [the Jupyter notebook(s) and source data](https://donnajharris.xyz/cp640s22fp/harr2890_project.zip) (external link)
- [a final report document](https://github.com/donnajharris/cp640_project/blob/main/deliverables/harr2890_project_report.pdf), and
- [a video presentation](https://youtu.be/etkXKaxtyuI) (external link)

======================

# After Downloading the Project Zip

## Pre-conditions:

- Local Jupyter Notebook server is installed and running

- `harr2890_project.zip` is extracted locally, with structure intact, where notebooks can be run

- Can create/write to `data` subfolder within the `harr2890_project` folder

## Running harr2890_project Notebooks:

_Please run the Notebook series in sequential, step order._

**Step 1** [(harr2890_project_step1_data_prep)](https://github.com/donnajharris/cp640_project/blob/main/harr2890_project/harr2890_project_step1_data_prep.ipynb)

- General data preprocessing; must be run before all other steps

**Step 2** [(harr2890_project_step2_hof_data_prep)](https://github.com/donnajharris/cp640_project/blob/main/harr2890_project/harr2890_project_step2_hof_data_prep.ipynb)

- Hall of Fame Approach preprocessing; must be run before Step 3

**Step 3** [(harr2890_project_step3_hof_modelling)](https://github.com/donnajharris/cp640_project/blob/main/harr2890_project/harr2890_project_step3_hof_modelling.ipynb)

- Hall of Fame Approach modelling (selection and evaluation)

**Step 4** [(harr2890_project_step4_ops_data_prep)](https://github.com/donnajharris/cp640_project/blob/main/harr2890_project/harr2890_project_step4_ops_data_prep.ipynb)

- OPS Approach preprocessing; must be run before Step 5

**Step 5** [(harr2890_project_step5_ops_modelling)](https://github.com/donnajharris/cp640_project/blob/main/harr2890_project/harr2890_project_step5_ops_modelling.ipynb)

- OPS Approach modelling (selection and evaluation)
