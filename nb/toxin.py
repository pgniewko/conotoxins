from pydpi.pypro import PyPro
import logging

AA_MODIFICATIONS = {
    "Benzoylphenylalanine": "F",
    "C-term amidation": "",
    "Sulfotyrosine": "Y",
    "4-Hydroxyproline": "P",
    "Pyroglutamic acid": "E",
    "Gamma carboxylic glutamic acid": "E",
    "Any": "G",
    "D-leucine": "L",
    "D-phenylalanine": "F",
    "D-methionine": "M",
    "D-tryptophan": "W",
    "D-tyrosine": "Y",
    "Bromotryptophan": "W",
    "glycosylated serine": "S",
    "2_2-dimethylthiazolidine": "G",
    "glycosylated threonine": "T",
    "Oxomethionine": "M",
    "Selenocystine (half)": "C",
    "gamma-hydroxy-D-valine": "V",
    "5-hydroxy-lysine": "K",
    "Norleucine": "L",
    "N-Acetate (on N-terminus)": "",
    "3-iodotyrosine": "Y",
    "5-amino-3-oxo-pentanoic acid": "G",
    "2-amino-DL-dodecanoic acid": "G",
    "Carbabridge [C2 unsaturated] (half)": "G",
    "alpha-aminobutyric acid": "G",
    "Asymmetric dimethylarginine": "R",
    "4-(R)-amino-proline": "P",
    "4-(S)-amino-proline": "P",
    "4-(R)-guanidino-proline": "P",
    "4-(R)-betainamidyl-proline": "P",
    "4-(R)-fluoro-proline": "P",
    "4-(S)-fluoro-proline": "P",
    "4-(R)-phenyl-proline": "P",
    "4-(S)-phenyl-proline": "P",
    "4-(R)-benzyl-proline": "P",
    "4-(S)-benzyl-proline": "P",
    "4-(R)-1-naphtylmehyl-proline": "P",
    "4-(S)-1-naphtylmehyl-proline": "P",
    "3-(R)-phenyl-proline": "P",
    "3-(S)-phenyl-proline": "P",
    "5-(R)-phenyl-proline": "P",
    "5-(S)-phenyl-proline": "P",
    "Diiodotyrosine": "Y",
    "D-alanine": "A",
    "Carbabridge [C4 unsaturated] (half)": "G",
    "Carbabridge [C4 saturated] (half)": "G",
    "Carbabridge [C7 unsaturated] (half)": "G",
    " L-4,5-dithiolnorvaline": "V",
}


class Toxin:
    def __init__(
        self,
        pid,
        seq,
        name,
        toxin_class,
        organism,
        geneSuperfamily,
        cysteineFramewrok,
        pharmacologicalFamily,
        isoelecticPoint,
        clean_seq=True,
    ):

        if pid is None:
            logging.debug("Protein id given: None")

        self.pid = pid
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
        self.modifications = []

    def get_pid(self):
        return self.pid

    def get_organism(self):
        return self.organism

    def get_seq(self):
        return self.seq

    def get_pharmacologicalFamily(self):
        return self.pharmacologicalFamily

    def get_features(self):
        if self.features is not None:
            return self.features
        else:
            self._calc_features()
            return self.features
        return None

    def add_modification(self, mod):
        self.modifications.append(mod)

    def _calc_features(self, long_feats=False):
        cds = PyPro()
        if self.clean_seq:
            self._clean_seq()
        cds.ReadProteinSequence(self.seq)

        try:
            all_feats = cds.GetALL()
            tpc_feats = cds.GetTPComp()
        except ZeroDivisionError as e:
            logging.warning(self.seq)
            raise

        all_feats_list = list(all_feats.values())
        if long_feats:
            tpc_feats_list = list(tpc_feats.values())
        else:
            tpc_feats_list = []
        self.features = all_feats_list + tpc_feats_list
        return self.features

    def _clean_seq(self):
        """For sequences that contain non-standard residues, the non-standard
        residues is replaced by their parent amino acids.
        In cases where no parent amino acids were available,
        these residues were either deleted or replaced by a glycine residue."""

        if self.seq is None:
            return

        seq_list = list(self.seq)

        for mod in self.modifications:
            position = int(mod["position"]) - 1
            name = mod["name"]
            orig_aa = AA_MODIFICATIONS[name]
            try:
                seq_list[position] = orig_aa
            except IndexError:
                continue

        self.seq = self.seq.replace("X", "")

    def __len__(self):
        if self.seq is not None:
            return len(self.seq)
        else:
            return 0

    def __str__(self):
        if self.seq is not None:
            out_string = f"{self.pid}\n{self.toxin_class}\n{self.geneSuperfamily}\n{self.organism}\n{self.seq}\n{self.pharmacologicalFamily}"
            return out_string
        else:
            return None

    def __eq__(self, pid):
        """Are pids the same"""
        if self.pid == pid:
            return True
        else:
            return False

    def copy(self):
        return Toxin(
            self.pid,
            self.seq,
            self.name,
            self.toxin_class,
            self.organism,
            self.geneSuperfamily,
            self.cysteineFramewrok,
            self.pharmacologicalFamily,
            self.isoelecticPoint,
            clean_seq=self.clean_seq,
        )
