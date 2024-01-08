<!--
 * @Author: zonghu.wang zonghu.wang@xtalpi.com
 * @Date: 2024-01-05 09:37:42
 * @LastEditors: zonghu.wang zonghu.wang@xtalpi.com
 * @LastEditTime: 2024-01-08 17:54:31
 * @FilePath: /pk-model/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# pk-model
Code for the paper "A Combination of Machine Learning and PBPKModeling Approach for PharmacokineticsPrediction of Small Molecules in Humans"

Code organization:
## Code Organization
```
The structure of the repository is as follows:
├── dataset # The folder that contains data files
├── environment.yml # The file that defines the conda environment
├── model # The folder that contains trained models
├── pk.ipynb # Jupyter notebook for PK analysis
├── result # The folder that contains output results
└── scripts # The folder that contains scripts
        ├── 1_smiles_data_process.ipynb #  SMILES data clean\eda
        ├── 2_chemprop_train.ipynb #  D-MPNN model training
        ├── 3_chemprop_param_search.ipynb #  D-MPNN parameter search
        ├── 4_ml_train.ipynb #  machine learning model(d SVR, RF, XGB, GBM) training
        ├── 5_admet_predict.ipynb #  ADMET prediction with best model(D-MPNN)
        └── 6_drug_pk_predict.ipynb #  drug PK prediction 



## Installation

Make sure to use python 3.8 or later:
```
conda env create -f environment.yml
conda activate pkmodel
```

Check out and install this repository:
```
git clone https://github.com/xtalpi-xic/pk-model.git
cd pk-model

## Usage
you can find train process in chemprop_train.ipynb\chemprop_param_search.ipynb\ml_train.ipynb
predict with best model in admet_predict.ipynb
drug PK prediction in drug_pk_predict.ipynb


```

## Acknowledgments

A special note of appreciation to the `chemprop` project and its contributors. The `chemprop` repository has been instrumental in advancing our understanding of machine learning in the context of chemical property prediction, and it has provided valuable insights and tools that have informed the development of our own models. We are grateful for the hard work and dedication of the `chemprop` team.

If you find our project useful, we encourage you to also check out [chemprop on GitHub](https://github.com/chemprop/chemprop) for deep learning-based molecular property prediction.


## Citation

If you found this work useful, please consider citing:

-------------------------------------------------

```bibtex
@article{pharmaceutical_research,
  title={A Combination of Machine Learning and PBPK Modeling Approach for Pharmacokinetics Prediction of Small Molecules in Humans}, 
  author={Yuelin Li, Zonghu Wang, Yuru Li, Jiewen Du, Xiangrui Gao, Yuanpeng Li, Lipeng Lai},
  year={2024},
  journal={Pharmaceutical Research}
}

If you use aspects of `chemprop` in your work or our project has been informed by `chemprop`, please consider citing their work as well as ours:

```plaintext
@misc{chemprop,
  author = {Chemprop Contributors},
  title = {chemprop: An open-source package for deep learning-based molecular property prediction},
  year = {Year of publication},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/chemprop/chemprop}},
}
