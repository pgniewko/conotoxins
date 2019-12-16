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

### Conotoxins
(Make this part better)
Conotoxins are disulfide-rich small peptides that are invaluable channel-targeted peptides and target neuronal receptors.
They show prospects for being potent pharmaceuticals in the treatment of Alzheimer's disease, Parkinson's disease, and epilepsy. 
Accurate prediction of conotoxin superfamily would have many important applications towards the understanding of its biological and pharmacological functions.      


 Conotoxins are disulfide-rich small peptides, which are invaluable peptides that target ion channel and neuronal receptors. 
 Conotoxins have been demonstrated as potent pharmaceuticals in the treatment of a series of diseases, such as Alzheimer’s disease, Parkinson’s disease, and epilepsy. 
 In addition, conotoxins are also ideal molecular templates for the development of new drug lead compounds and play important roles in neurobiological research as well. 
 Thus, the accurate identification of conotoxin types will provide key clues for the biological research and clinical medicine. 
 Generally, conotoxin types are confirmed when their sequence, structure, and function are experimentally validated. 
 However, it is time-consuming and costly to acquire the structure and function information by using biochemical experiments.
 Therefore, it is important to develop computational tools for efficiently and effectively recognizing conotoxin types based on sequence information. 


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

4. **PredCSF: An integrated feature-based approach for predicting conotoxin superfamily**      
Fan YX, Song J, Shen HB, Kong X.      
*Protein Pept Lett. 2011, 18(3):261-7.*       
[[papers]](http://www.eurekaselect.com/87458/article)    
[[web-server]](http://www.csbio.sjtu.edu.cn/bioinf/PredCSF/)      

5. **iCTX-Type: A Sequence-Based Predictor for Identifying the Types of Conotoxins in Targeting Ion Channels**     
Hui Ding, En-Ze Deng,1 Lu-Feng Yuan, Li Liu, Hao Lin, Wei Chen, and Kuo-Chen Chou       
*BioMed Research International Volume 2014, *
[[paper]](https://www.hindawi.com/journals/bmri/2014/286419/)
[[web-server]](http://lin-group.cn/server/iCTX-Type)


### Ideas:      
1. Explore other dimensionality reduction techniques.     
2. Use the technique used in protein class classification with covariance matrix (Chou?).    
3. Compare the consistency between my automated way of creating benchmakrs and the manually curted one.    


### License
The library is open-source for academic and education users. If you want to use the library in any of your work please cite: *Pawel Gniewek*, _Machine learning study in conotoxins_, https://github.com/pgniewko/deep-toxin.        


