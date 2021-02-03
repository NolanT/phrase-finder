# Phrase Finder

Utility which returns a list of the 100 most common three word sequences (phrases) from a given text

## Example Usage

one text file
```
python3 phrase_finder.py moby_dick.txt
```

multiple text files
```
python3 phrase_finder.py moby_dick.txt pride_and_prejudice.txt
```

stdin
```
cat pride_and_prejudice.txt | python3 phrase_finder.py 
```

wildcard text files
```
python3 phrase_finder.py *.txt
```

## Script Requirements

- [x] The program accepts as arguments a list of one or more file paths (e.g. ./solution.rb file1.txt file2.txt ...).
- [x] The program also accepts input on stdin (e.g. cat file1.txt | ./solution.rb).
- [x] The program outputs a list of the 100 most common three word sequences.
- [x] The program ignores punctuation, line endings, and is case insensitive (e.g. “I love\nsandwiches.” should be treated the same as "(I LOVE SANDWICHES!!)"). Watch out that contractions aren't changed into 2 words (eg. shouldn't should not become shouldn t).
- [x] The program should be well structured and understandable.