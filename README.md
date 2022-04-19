# Usage

1. Sign up to dstack.ai

2. Add AWS credentials in `Settings` | `AWS`

3. Add a limit for the `m5.large` `Instance type` with the `Maximum` set to at least `3` in `Settings` | `AWS` | `On-demand runners`

4. Clone this repository

5. Install and configure the CLI:

```
pip install dstack
dstack config --token <token>
```

6. Run the `hello` workflow from the repository folder:

```
dstack run hello
```
