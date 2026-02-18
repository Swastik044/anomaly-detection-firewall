setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

data:
	python scripts/make_data.py

train:
	python scripts/train.py

evaluate:
	python scripts/evaluate.py

all: data train evaluate
