# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 00:27:37 2012

@author: orient
"""

from distutils.core import setup


packagedata = {"pydpi": ["html/*", "data/*", "manual/*", "drug/*", "protein/*"]}


setup(
    name="pydpi",
    version="1.0",
    description="A powerful tool for chemoinformatics, bioinforamtics and chemogenomics study",
    author="Dongsheng Cao",
    author_email="oriental-cds@163.com",
    url="http://cbdd.csu.edu.cn/index",
    license="GPL",
    packages=["pydpi"],
    package_data=packagedata,
    # 	data_files = datafiles,
    package_dir={"pydpi": "src/pydpi"},
    scripts=[],
    py_modules=[],
)
