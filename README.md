###RUN

On windows or linux:
```
python main.py input_path1 input_path2 ... file_to_enrich
```
You have to specify at least two file paths. At least one file with already enriched code descriptions 
and one file with new code descriptions to enrich.
Otherwise algorithm will use default files specified in main.py

###PARAMETERS

Algorithm is run with two parameters as follows:

confidence_threshold = 0.3
manual_confidence_threshold = 0.5

They are hardcoded in main.py

Each attractor has to have confidence >= 0.3 to be added to a new code description.
Attractors must to have confidence >= 0.5 to be transferred automatically to enriched C*.


###CREATING T
1. Load N already enriched files. 
2. Replace all of the codeIds read from files with unique numerical code ids (Integer)
3. Create set of all (lower-cased) synonyms (attractors) in all of the N enriched files. 
4. Create matrix T of size M x N where M is the size of set of synonyms.
5. Each element in the matrix T is 0 when a synonym is not present in a taxonomy, and the numerical code id when it is.
Matrix T is a numpy matrix for time and speed purposes. 

**For simplified solution I assumed that one synonym is present only in one code description in each taxonomy.
In reality it's not true but number of duplicates was so small that I decided that it's not relevant
for this proof-of-concept solution.**


###CREATING C

1. Load file to enrich
2. Replace all of the codeIds read from files with unique numerical code ids (but store old ids in dictionary where
key is the new codeId and value is the old codeId)


###ENRICHING

a) For each code description d in the new code table C, we choose the
synonym in the matrix T that has the highest string
similarity to d. This identifies the string attractor a for d.

String similarity is based on normalized Levenshtein distance. 
Before calculating the distance I clean the code descriptions (lower-case, remove punctuations, parentheses etc.)
At this point one synonym can be added to multiple code descriptions (hence the duplicates in already enriched taxonomies)

b) For each unused synonym s in T find which already chosen
attractor a in C* has the best confidence as an attractor.

Confidence is calculated taking into account confidence of previously matched attractor (parent_confidence) 
and average of string similarity and number of shared codes in synonyms' rows in T. 
Number of shared codes and string distance are both normalized to <0,1>.


```python
def get_confidence(distance, parent_confidence=1.0, shared_codes=None):
    if shared_codes is None:
        current_confidence = 1-distance
    else:
        current_confidence = (shared_codes+(1-distance))/2
    return current_confidence*parent_confidence
```

For example:
In part a) for new code description 'developer' we are finding that synonym 'software developer' has the highest string similarity.
string distance between 'developer' and 'software developer' = 0.3
It's a first attractor so parent_confidence = 1.0 and shared codes = None
so confidence = 0.7


###Output
Enriched C* is automatically saved to xml file in generated_files folder. 
Transfer type is based on confidence and manual_confidence_threshold parameter.


