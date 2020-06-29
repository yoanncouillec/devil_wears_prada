ARCHIVE=search_challenge.tar.gz
DIR=testdir

index:
	python create_index.py

test:
	python search.py "yellow toywatch"
	python search.py "asos skinny jeans"
	python search.py "toyota car"
	python search.py "floral dress"
	python search.py "prada shirt"
	python search.py "red prada clutch"
	python search.py "prada perforated runway duffel bag"
	python search.py "guess top"
	python search.py "ralph lauren vest"
	python search.py ""
	python search.py "a"
	python search.py "aaa"
	python search.py "zzz"

build:
	tar czvf $(ARCHIVE) Makefile create_index.py search.py search_dataset.json requirements.txt

extract:
	mkdir $(DIR) && tar -C $(DIR) -xzvf $(ARCHIVE)

clean:
	rm index.json
