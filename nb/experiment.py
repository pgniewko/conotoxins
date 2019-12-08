
from collections import defaultdict
from toxin import Toxin

import numpy as np

class Experiment():
    """
    :-P lazy Pawel
    """
    def __init__(self, toxins, excludeOrganism='synthetic', min_val=8):
        self.toxins = [toxin_.copy() for toxin_ in toxins]
        self.excludeOrganism = excludeOrganism
        self.min_val=min_val
        self.experient_data = None

    def prepare_experiment(self):
        first_run_dict = defaultdict(list)
        for toxin_ in self.toxins:
            if self.excludeOrganism in toxin_.get_organism() or "None" in toxin_.get_organism():
                continue
            if "None" in toxin_.get_pharmacologicalFamily():
                continue
            if "None" in toxin_.get_seq():
                continue

            first_run_dict[toxin_.get_pharmacologicalFamily()].append(toxin_.copy())

        second_run_dict = defaultdict(list)
        for k, v in first_run_dict.items():
            if len(v) >= self.min_val:
                second_run_dict[k] = v

        self.experient_data = second_run_dict
        
        return self.experient_data

    def experiment_from_file(self, fname):
        pids = []
        seqs = []
        classes = []
        with open(fname, 'r') as fin:
            for line in fin:
                pairs = line.rstrip('\n').split()
                pids.append(pairs[0]) 
                seqs.append(pairs[1])
                classes.append(pairs[2])
       
        run_dict = defaultdict(list)
        for i, pid in enumerate(pids):
            # TODO: make sure toxins are defined
            try:
                tox = self.toxins[self.toxins.index(pid)]
            except ValueError:
                print(f"Can't find protein with id {pid}. Createing a new object with seq: {seqs[i]} and class: {classes[i]}")
                tax = Toxin(pid, seqs[i], "?", classes[i], "?", "?", "?", "?", "?")
            # TODO: make sure tox is not null
            run_dict[classes[i]].append(tox.copy())
        self.experient_data = run_dict
        return self.experient_data

    def num_classes(self):
        if self.experient_data is not None:
            return len(self.experient_data.keys())
        else:
            return 0

    def get_data(self):
        mat = []
        labels = []
        
        labels_dict = {}
        labels_map = {}
        for i, key in enumerate(self.experient_data.keys()):
            labels_map[i] = key
            for toxin_ in self.experient_data[key]:
                try:
                    feats = toxin_.get_features()
                except:
                    print(f'Skipping {toxin_.get_pid()} protein, with a sequence: {toxin_.get_seq()}')
                    continue
                mat.append(feats)
                labels.append(i)


        return np.array(mat), np.array(labels), labels_map


