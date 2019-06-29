# Avalanche Stemmer

Presumably generation 3 of Porter Stemmer. 

## Strategies

1. Adding in `overrides_defensive` to prevent overstemming

2. Remove `prefixes` if aggressive label set

3. Adding in `startwith_x` predefined and well-tested stems to prevent understemming

4. Detailed rules for undeterminate `startwith_` stems

5. Revised `postfix` stemming rules tested by hundrends of experiments with massive real Engish words

