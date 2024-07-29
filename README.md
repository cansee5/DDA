# Enhancing Training Data Attribution for Large Language Models with Fitting Error Consideration

### 1. Building hallucination dataset using `dataset_construction.py` in `dataset`.

### 2. Use the instruction template in `model_train` and the constructed training set of hallucination xsum to construct the instruction fine-tuning data of LLaMA-Factory.

### 3. Use `error_validation_data_generate.sh` from `dataset` to generate positive and negative samples with the trained model in Step 2.

### 4. Use the positive and negative samples in Step 3 to train a ground model and an error model respectively on the trained model in Step to form a pair of comparison models. The instruction template and training framework during the training process are the same as those in Step 2 of the training process.

### 5. Repeat step 4 for all models of the training epoch in Step 2 to obtain a series of ground models and error models.

### 6. For the ground model and error model of each epoch in Step 5, use `influences_scores.py` in `influences scores` to calculate their influence scores.

### 7. Use `debias_and_denoise.py` to calculate the recall metrics of the AUC metrics for the results in all epochs in Step 6.

### NOTE: Note that the paths in the code are all virtual paths, please change them according to the actual situation.
