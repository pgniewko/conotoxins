Copyright (c) 2012CBDD03, Computational Biology and Drug Design Group, 
Central South University, China.
All rights reserved.

INSTRUCTION

The rapidly increasing amount of publicly available data in biology and chemistry enables researchers 
to revisit interaction problems by systematic integration and analysis of heterogeneous data. Herein, 
we developed a comprehensive python package to emphasize the integration of chemoinformatics and 
bioinformatics into a molecular informatics platform for drug discovery. PyDPI (Drug-Protein 
Interaction with Python) is a powerful python toolkit for computing commonly-used structural and 
physicochemical features of proteins and peptides from amino acid sequences, molecular descriptors of 
drug molecules from their topology, and protein-protein interaction and protein-ligand interaction 
descriptors. It computes six protein feature groups composed of fourteen features that include 
fifty-two descriptors and 9890 descriptor values, nine drug feature groups composed of eleven 
descriptors that include 530 descriptor values. In addition, it provides seven types of molecular 
fingerprint systems for drug molecules, including topological fingerprints, electro-topological state 
(E-state) fingerprints, MACCS keys, FP4 keys, atom pairs fingerprints, topological torsion fingerprints 
and Morgan/circular fingerprints. By combining different types of descriptors from drugs and proteins 
in different ways, interaction descriptors representing protein-protein or drug-protein interactions 
could be conveniently generated. These computed descriptors can be widely used in various fields 
relevant to chemoinformatics, bioinformatics and chemogenomics.

If you have any problem, Please contact Dongsheng Cao (oriental-cds@163.com)

#############################################FEATURES################################################
The protein descriptors calculated by pydpi:
(1) AAC: amino acid composition descriptors (20)
(2) DPC: dipeptide composition descriptors (400)
(3) TPC: tri-peptide composition descriptors (8000)
(4) MBauto: Normalized Moreau-Broto autocorrelation 
descriptors (depend on the given properties, the default is 240)
(5) Moranauto: Moran autocorrelation descriptors
(depend on the given properties, the default is 240)
(6) Gearyauto: Geary autocorrelation descriptors
(depend on the given properties, the default is 240)
(6) CTD: Composition, Transition, Distribution descriptors 
(CTD) (21+21+105=147)
(7) SOCN: sequence order coupling numbers 
(depend on the choice of maxlag, the default is 60)
(8) QSO: quasi-sequence order descriptors 
(depend on the choice of maxlag, the default is 100)
(9) PAAC: pseudo amino acid composition descriptors 
(depend on the choice of lamda, the default is 50)
(10) APAAC: amphiphilic pseudo amino acid composition descriptors
(depend on the choice of lamda, the default is 50) 
(11) CT: conjoint triad features (343)
######################################################################################################
The drug descriptors calculated by pydpi:
(1) Constitutional descriptors (30)
(2) Topologcial descriptors (25)
(3) Molecular connectivity descriptors (44)
(4) Kappa descriptors(7)
(5) E-state descriptors (237)
(6) Autocorrelation descriptors (96) 
including Moreau-Broto, Moran and Geary autocorrelation descriptors
(7) Charge descriptors (25)
(8) Molecular property descriptors (6)
(9) MOE-type descriptors (60)
(10) Daylight fingerprint (2048)
(11) MACCS keys (166)
(12) FP4 fingerprints (307) 
(13) E-state fingerprints (79)
(14) Atom Paris fingerprints and Morgan fingerprints
######################################################################################################
Install the pydpi package
pydpi has been successfully tested on Linux and Windows systems. 
The author could download the pydpi package via:
http://code.google.com/p/pydpi/downloads/list (.zip and .tar.gz). 

The install process of pydpi is very easy:
*********************************************************************
*You first need to install RDkit, Openbabel, and pybel successfully.*
*********************************************************************
Openbabel and pybel can be downloaded via: http://openbabel.org/wiki/Main_Page
RDkit can be downloaded via: http://code.google.com/p/rdkit/


On Windows:
(1): download the pydpi package (.zip)
(2): extract or uncompress the .zip file 
(3): cd pydpi-1.0
(4): python setup.py install

On Linux:
(1): download the pydpi package (.tar.gz) 
(2): tar -zxf pydpi-1.0.tar.gz 
(3): cd pydpi-1.0 
(4): python setup.py install or sudo python setup.py install 
######################################################################################################
Example:
For more examples, please see the user guide.
######################################################################################################
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the computational biology and drug design group nor the
      names of the authors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL COPYRIGHT HOLDERS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
######################################################################################################
