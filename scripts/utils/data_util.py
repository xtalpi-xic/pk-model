import numpy as np
from rdkit import Chem, RDLogger
from rdkit.Chem.rdchem import Mol

RDLogger.DisableLog("rdApp.*")
import hashlib
import os
import re
import sys
from typing import List, Tuple, Union

import pandas as pd
from chembl_structure_pipeline import standardizer as chembl_stand
from loguru import logger
from rdkit.Chem.SaltRemover import SaltRemover


def mkdir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
        return True
    return False

def chembl_smi_standardizer(smi: str, isomericSmiles:bool=True, sanitize:bool=True) -> str:
    """Standardize SMILES using ChEMBL standardizer.
    Args:
        smi: SMILES string to be standardized.
        isomericSmiles: return the isomeric smiles. Defaults to True.
        sanitize: applies sanitization using the ChEMBL standardizer. Defaults to True.
    Returns:
        standardized SMILES string.
    """    
    try:
        # logger.info(smi)
        mol = Chem.MolFromSmiles(smi)
    except Exception as e:   
        logger.error('Could not parse smiles:%s error:%s '%(smi,e))
        return None
    try:
        standard_mol = chembl_stand.standardize_mol(mol, sanitize=sanitize)
        standard_smiles = Chem.MolToSmiles(
            standard_mol, kekuleSmiles=False, canonical=True, isomericSmiles=isomericSmiles
        )
    except Exception as e:  
        logger.error('Could not standardize_mol smiles:%s erro:%s '%(smi,e))
        return None
    # else:  
    #     # 如果没有异常发生，执行这里的代码  
    # finally:  
    # 无论是否有异常发生，都会执行这里的代码 
    
    # rdkit.Chem.MolToSmiles()方法是用于将RDKit分子对象转换为SMILES字符串的方法。它的参数如下：
    # mol：必需，要转换为SMILES字符串的RDKit分子对象。
    # isomericSmiles：bool类型，是否生成同分异构体SMILES，默认为False，即不生成同分异构体SMILES。
    # kekuleSmiles：bool类型，是否生成Kekule SMILES，默认为False，即生成熔合环上的芳香性保持未指定的杂化，如果是True，则生成使用Kekule表示法的SMILES。
    # canonical：bool类型，是否生成规范化的SMILES，默认为True，即生成规范化的SMILES。
    # allBondsExplicit：bool类型，是否为所有化学键添加显式的方向性和序数，即无论它们是单键、双键还是三键。默认为False。
    # allHsExplicit：bool类型，是否为所有氢原子添加显式的表示，默认为False。
    # sanitize：bool类型，是否在生成SMILES之前对分子进行净化，默认为True。净化操作将包括在分子中添加氢原子、移除未配对的电荷、设置正确的杂化和检查化学键长度等。
    return standard_smiles

def is_valid_smiles(sm):
    try:
        Chem.SanitizeMol(Chem.MolFromSmiles(sm))
    except:
        return False
    else:
        return True
    

def get_clean_df(
    df: pd.DataFrame , 
    X_COLS,
    drop_invalid_smiles: bool = True, 
    drop_missing_x: bool = True) -> pd.DataFrame:
    """Prune raw data for later processing.
    Column actions: drop some info columns
    Row actions: remove duplicated and / or SMILES, drop missing x
    """
    logger.info("original record nums:%s"%df.shape[0])
    df = df.loc[~df.SMILES.duplicated(keep=False), ]
    logger.info("after drop_duplicated record nums:%s"%df.shape[0])
    if drop_invalid_smiles:
        df = df.loc[df["SMILES"].apply(is_valid_smiles), ]
    logger.info("after drop_invalid_smiles record nums:%s"%df.shape[0])
    if drop_missing_x:
        x_cols = X_COLS
        df = df.dropna(axis='index', subset=x_cols)
    logger.info("after drop_missing_x record nums:%s"%df.shape[0])
    # df=df[df.MW<=900]
    # logger.info("after MW<=900 record nums:%s"%df.shape[0])
    return df

def upper_clip_outliers(df: pd.DataFrame,cols) -> pd.DataFrame:
    """Upper clip the outliers in 3 variables by 90% percentile:
    """

    newdf = df.drop(cols, axis=1)
    for colname in cols:
        upper_bound = round(np.percentile(df[colname], 90)) + 1
        newdf[colname] = df[colname].apply(
            lambda ele: ele if ele < upper_bound else upper_bound
        )
    return newdf

def get_log_y(colname: str, df: pd.DataFrame) -> pd.Series:
    """log10 transform .
    Args:
        colname:colname
        df: data containing target column
    """

    logger.info(df[colname].dropna().shape)
    return df[colname].dropna().apply(np.log10)


 
 

 
 
 
