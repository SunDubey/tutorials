import mlflow
"""
Read documentation on https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.run
"""
if __name__ == '__main__':
    params_1 = {'alpha': 0.5,
              'l1_ratio': 0.01}

    # Run a project from GitHub Project
    mlflow.run("git://github.com/mlflow/mlflow-example.git", use_conda=False, parameters=params_1)
    # TODO
    # Add your GitHub MLflow Project here
    # mlflow.run(<YOUR_PROJECT_GIT_URI>, args...,args)
