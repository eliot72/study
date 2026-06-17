LATEX ?= xelatex
FLAGS ?= -interaction=nonstopmode -halt-on-error
ROOTS = knowledge-guide classified-exams solutions

.PHONY: all clean

all: $(ROOTS:%=%.pdf)

%.pdf: %.tex content/metadata.tex content/common.tex
	$(LATEX) $(FLAGS) $<
	$(LATEX) $(FLAGS) $<

clean:
	rm -f *.aux *.log *.out *.toc *.pdf
