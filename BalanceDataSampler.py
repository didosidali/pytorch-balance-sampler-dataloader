from torch.utils.data import Sampler
import numpy as np

class BalanceDataSampler(Sampler):
    def __init__(self, dataset_targets, max_class=None):
        self.prob = []
        count = np.histogram(
            dataset_targets,
            len(set(dataset_targets))
        )[0]
        
        if max_class == None:
            max_class = count.max()
            
        modulos = max_class % count
        
        for key, y in enumerate(dataset.y):
            self.prob += [key for i in range(max_class // count[y] + (modulos[y] > 0))]
            modulos[y] -= 1
        
    def __len__(self):
        return len(self.prob)
    
    def __iter__(self):
        return iter(np.array(self.prob)[np.random.permutation(len(self.prob))].tolist())
