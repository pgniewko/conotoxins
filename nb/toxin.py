from pydpi.pypro import PyPro

class Toxin():
    def __init__(self,
                 seq,
                 name,
                 toxin_class,
                 organism,
                 geneSuperfamily,
                 cysteineFramewrok,
                 pharmacologicalFamily,
                 isoelecticPoint,
                 clean_seq=True): 
                 ): 

        self.seq = seq
        self.name = name
        self.toxin_class = toxin_class
        self.organism = organism
        self.geneSuperfamily = geneSuperfamily
        self.cysteineFramewrok = cysteineFramewrok
        self.pharmacologicalFamily = pharmacologicalFamily
        self.isoelecticPoint = isoelecticPoint
        self.clean_seq = clean_seq

        self.features = None

    def get_features(self):
        if self.features is not None:
            return self.features
        else:
            self._calc_features()
            return self.features
        return None

    def _calc_features(self, long_feats=False):
        cds = PyPro()
        if self.clean_seq:
            self._clean_seq()
        cds.ReadProteinSequence(self.seq)

        all_feats = cds.GetALL()
        tpc_feats = cds.GetTPComp()

        all_feats_list = list(all_feats.values())
        if long_feats:
            tpc_feats_list = list(tpc_feats.values())
        else:
            tpc_feats_list = []
        self.features = all_feats_list + tpc_feats_list
        return self.features

    def _clean_seq(self):
        #TODO: This is temporary.
        self.seq = self.seq.replace('X','')


    def __len__(self):
        if self.seq is not None:
            return len(self.seq)
        else:
            return 0

    def __str__(self):
        if self.seq is not None:
            return self.seq
        else:
            return None
