# SM_interview_prep_2023
My Interview Prep for 2023

* Run CMD as administrator and then run the following commands:
 - pip install poetry
 - pip install pre-commit

```bash
pre-commit install
pre-commit run --all-files
poetry run black .
poetry run isort .
git add .
pre-commit run --all-files
git commit
git push
```
