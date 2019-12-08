## Molecular targets of conotoxins       

>Notice: This is research code that will not necessarily be maintained in the future.
>The code is under development so make sure you are using the most recent version.
>I welcome bug reports and PRs but make no guarantees about fixes or responses.

## Table of contents       

[Raw data](#data-preparation-and-model-training)           
[Datasets](#datasets) information       
[Results](https://github.com/pgniewko/conotoxins/blob/master/nb/tSNE-MLR.ipynb)      
[Papers](#papers)    
[Ideas](#ideas)
[License](#license)    

### Datasets      
1. Data downloaded from [ConoServer](http://www.conoserver.org/?page=download) (access date 11/19/19)      
2. The original dataset was also [extracted](https://github.com/pgniewko/conotoxins/blob/master/data/ASA.PJS.2019.txt) from the paper.    


### Papers
1. **Predicting the Molecular Targets of Conopeptides by using Principal Component Analysis
and Multiclass Logistic Regression**           
Xavier Eugenio Asuncion, Abdul-Rashid Sampaco III, Henry Adorna, Joselito Magadia, Vena Pearl Bongolan, and Arturo Lluisma.      
*Philippine Journal of Science, 148 (S1): 237-245, 2019*        
[[paper]](http://philjournalsci.dost.gov.ph/images/pdf/special_issue/148_S1/predicting_molecular_targets_.pdf)    

2. **Recent Advances in Conotoxin Classification by Using Machine Learning Methods**           
Fu-Ying Dao, Hui Yang, Zhen-Dong Su, Wuritu Yang, Yun Wu, Hui Ding, Wei Chen, Hua Tang and Hao Lin       
*Molecules 2017, 22, 1057; doi:10.3390/molecules2207105*      
[[paper]](https://www.mdpi.com/1420-3049/22/7/1057)       

3. **iLearn: an integrated platform and meta-learner for feature engineering, 
machine-learning analysis and modeling of DNA, RNA and protein sequence data**        
Zhen Chen, Pei Zhao, Fuyi Li, et al.          
*Briefings in Bioinformatics, 00(00), 2019, 1–11*      
[[paper]](https://academic.oup.com/bib/advance-article-abstract/doi/10.1093/bib/bbz041/5475015?redirectedFrom=fulltext)        
[[repo]](https://github.com/Superzchen/iLearn)        


### Ideas:      
1. Do more comprehensive statistical analysis      
2. Check what analysis we can do with the ideas from this [paper]().
3. tSNE with all available seq.Color known, leave unknown grey.      
4. Do more comprehensive bioinformatics study. Can we predict the post-translational modyfications?
5. Do ML for  other properties, like cysteine frameworks etc.    
6. Follow up on pydpi (re)implementation.     

### License
The library is open-source for academic and education users. If you want to use the library in any of your work please cite: *Pawel Gniewek*, _Machine learning study in conotoxins_, https://github.com/pgniewko/deep-toxin.        


