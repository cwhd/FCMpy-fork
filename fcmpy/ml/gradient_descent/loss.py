from abc import ABC, abstractmethod


class Loss(ABC):
    """
        Interface for computing the loss.
    """
    @abstractmethod
    def compute(**kwargs):
        raise NotImplementedError('compute method is not defined.')


class MSE(Loss):
    """
        Class for computing the MSE
    """
    @staticmethod
    def compute(**kwargs):
        """
            Parameters
            ----------
            observed: np.array
                        the observed data
            
            predicted: np.array
                        the predicted data
        """
        assert len(obs) == len(pred)
        
        obs = kwargs['observed']
        pred = kwargs['predicted']
        n = kwargs['n']
        return sum(sum((obs-pred)**2))/n