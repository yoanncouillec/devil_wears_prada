ARCHIVE=search_challenge.tar.gz
DIR=testdir

index:
	python create_index.py

simple_test:
	python search.py "yellow toywatch"
	python search.py "asos skinny jeans"
	python search.py "toyota car"

more_test:
	python search.py "floral dress"
	python search.py "prada shirt"
	python search.py "red prada clutch"
	python search.py "prada perforated runway duffel bag"
	python search.py "guess top"
	python search.py "ralph lauren vest"

weird_test:
	python search.py ""
	python search.py "a"
	python search.py "aaa"
	python search.py "zzz"

all_test: test_simple_queries test_more_queries test_weird_queries

build:
	tar czvf $(ARCHIVE) Makefile create_index.py search.py search_dataset.json requirements.txt

extract:
	mkdir $(DIR) && tar -C $(DIR) -xzvf $(ARCHIVE)

clean:
	rm index.json || true
	rm *.tar.gz || true
	rm -r __pycache__ || true

mrproper: clean
	rm *~
