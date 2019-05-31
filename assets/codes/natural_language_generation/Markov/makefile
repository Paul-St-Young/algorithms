all: simple_generator ngram_generator

simple_generator: simple_generator.C
	g++ simple_generator.C -o simple_generator

ngram_generator: ngram_generator.C
	g++ ngram_generator.C -o ngram_generator

clean:
	rm simple_generator
	rm ngram_generator
