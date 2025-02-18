# Instructions on setting up Habitat simulator
This setup is working for headless method. This means that there is no UI but I'm sure even GUI version also works(Not tested yet).
## 1. Environment Setup

1. Create a conda environment with the following versions. Remember
the versions are important:
- python - 3.9
- cmake - 3.14.0

For reference, the command is `conda create env -n habitat_sim_env python=3.9 cmake=3.14.0`

2. The following command is taken from their website itself. Run this command to install the habitat simulator package

```conda install habitat-sim headless -c conda-forge -c aihabitat```

This will install with some specific versions. The problem this directly doesn't work is because there are version problems conflict with `numba==0.53.1` and `llvmlite--0.36.9`. 

3. To fix this, we just upgrade the `numba` and `llvmlite` libraries:
```conda update -c conda-forge numba llvmlite```

This should install the following versions: `numba==0.59.1` and `llvmlite==0.42.0`

4. Now the simulator should work according to the documentation. To verify, run the folllowing command.

```python examples/example.py --scene ./habitat-test-scenes_v1.0/skokloster-castle.glb```

This should output something similar to this at the end:
```
 ========================= Performance ======================== 
 640 x 480, total time 1.90 s, frame time 1.903 ms (525.5 FPS)
 ==============================================================
```