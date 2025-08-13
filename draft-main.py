from qec_tensor.naming import IndexRegistry
from qec_tensor.components.rails import make_eye_rails

n = 7  # Steane example
reg = IndexRegistry(n)
tn, data_in, data_out = make_eye_rails(n, reg)

print("Number of tensors:", len(tn.tensors))
print("Sample tensor:", tn.tensors[0])
print("First 6 inds:", list(tn.all_inds())[:6])

# basic expectations
assert len(data_in) == 2 * n, "Expected 2 upstream rails per qubit"
assert len(data_out) == 2 * n, "Expected 2 downstream rails per qubit"
for s in data_in + data_out:
    assert s in tn.all_inds(), f"Missing index {s} in TN"

print("OK: rails built with explicit names.")

