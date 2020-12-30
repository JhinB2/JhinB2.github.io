models = [{"make":"Nokia","model":216},{"make":"Mi Max","model":2}]
sorted_models = sorted(models, key=lambda x: x['model'])
print(sorted_models)