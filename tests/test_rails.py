from qec_tensor.naming import IndexRegistry
from qec_tensor.components.rails import make_eye_rails

def test_make_eye_rails_7():
    reg = IndexRegistry(7)
    tn, data_in, data_out = make_eye_rails(7, reg)
    assert len(data_in)  == 14 and len(data_out) == 14
    # all indices appear in the TN
    inds = set(tn.all_inds())
    for s in data_in + data_out:
        assert s in inds

