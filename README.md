# Code-Coverage_Testing

## This demo assesses how different data generation algorithms fare in testing code coverage

## Folder Structure
- input_code_files/
    - include/
        - generate_data.py
        - make_data_missing.py
    - input_data.py
- coverage-algorithms/
    - apriori/
    - fp-growth/
    - inverse_sampling/
    - variational_autoencoder/
    - multiple_imputations/
    - bayesian_network/
- code-coverage/
    - coverage-types/
    - main-code-coverage-wrapper.py (spark parallelization)
- tracer/
    - node_traversal.py (assess code coverage with visual)
- README.md
- requirements.txt
- .gitignore