from typing import List, Tuple
import numpy as np
import quimb.tensor as qtn
from ..naming import IndexRegistry

def make_eye_rails(n: int, reg: IndexRegistry | None = None) -> Tuple[qtn.TensorNetwork, List[str], List[str]]:
    '''
    Build n-qubit superoperator rails (identity on ket & bra).
    '''
    if reg is None:
        reg = IndexRegistry(n)

    eye = np.eye(2, dtype=np.complex128)  # one cached identity
    tensors: List[qtn.Tensor] = []
    for i in range(n):
        nm = reg.rails(i)
        tensors.append(qtn.Tensor(eye, inds=[nm.op, nm.Op], tags=["EYE"]))  # ket rail
        tensors.append(qtn.Tensor(eye, inds=[nm.od, nm.Od], tags=["EYE"]))  # bra rail

    tn = qtn.TensorNetwork(tensors)
    return tn, reg.upstream_inputs(), reg.downstream_outputs()

