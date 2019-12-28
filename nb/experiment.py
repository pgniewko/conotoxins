import logging
import pickle
import numpy as np

from collections import defaultdict
from toxin import Toxin


class Experiment:
    """
    :-P lazy Pawel
    """

    def __init__(self, toxins, excludeOrganism="synthetic", min_val=8):
        self.toxins = [toxin_.copy() for toxin_ in toxins]
        self.excludeOrganism = excludeOrganism
        self.min_val = min_val
        self.experient_data = None

    def prepare_experiment(self, strict=True):
        first_run_dict = defaultdict(list)
        for toxin_ in self.toxins:
            if strict:
                if (
                    self.excludeOrganism in toxin_.get_organism()
                    or "None" in toxin_.get_organism()
                ):
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
        with open(fname, "r") as fin:
            for line in fin:
                if line.startswith("#"):
                    continue
                pairs = line.rstrip("\n").split()
                pids.append(pairs[0])
                seqs.append(pairs[1])
                classes.append(pairs[2])

        run_dict = defaultdict(list)
        for i, pid in enumerate(pids):
            # TODO: make sure toxins are defined
            try:
                tox = self.toxins[self.toxins.index(pid)]
            except ValueError:
                logging.warning(
                    f"Can't find protein with id {pid}. Createing a new object with seq: {seqs[i]} and class: {classes[i]}"
                )
                tox = Toxin(pid, seqs[i], "?", classes[i], "?", "?", "?", "?", "?")
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

        labels_map = {}
        for i, key in enumerate(self.experient_data.keys()):
            labels_map[i] = key
            for toxin_ in self.experient_data[key]:
                try:
                    feats = toxin_.get_features()
                except:
                    logging.debug(
                        f"Skipping {toxin_.get_pid()} protein, with a sequence: {toxin_.get_seq()}"
                    )
                    continue
                mat.append(feats)
                labels.append(i)

        return np.array(mat), np.array(labels), labels_map

    def dump_data(self, fout, data, labels, labels_map):
        try:
            f = open(fout, "wb")
        except OSError:
            logging.error(f"File {fout} can't be open for writing.")
            return

        pickle.dump(data, f)
        pickle.dump(labels, f)
        pickle.dump(labels_map, f)

    def load_data(self, fin):
        try:
            f = open(fin, "rb")
        except FileNotFoundError:
            logging.error(f"File {fin} can't be found.")
            return (None, None, None)

        data = pickle.load(f)
        labels = pickle.load(f)
        labels_map = pickle.load(f)
        return (data, labels, labels_map)
