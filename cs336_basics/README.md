# Build Transformer LM from Scratch

## What you can use

In particular, you may not use any definitions from `torch.nn`, `torch.nn.functional` or `torch.optim` except for the following:

- `torch.nn.Parameter`
- Container classes in `torch.nn` (e.g., 'Module', `ModuleList`, `Sequential`, etc.)
- `torch.optim.Optimizer` base class

## Code Architecture

- `cs336_basics/*`: where you will implement the Transformer LM
- `adapters.py`: a set of functionality that your code must have. For each piece of functionality, fill out its implementation by simply invoking your code in `cs336_basics/*`.

    - NOTE: your changes to `adapters.py` should not contain any substantive logic; this is glue code.

- `test_*.py`: This contains all the tests that you must pass (e.g., `test_scaled_dot_product_attention`), which will invoke the hooks defined in adapters.py. Don’t edit the test files.