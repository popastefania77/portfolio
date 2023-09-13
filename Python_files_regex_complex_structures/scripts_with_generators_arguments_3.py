"""
Create a Moldavian-English dictionary, based on the Romanian-English dictionary. This dictionary won’t have the
key for ‘carte’, but will have the key for ‘doi’.
 E.g The Moldavian-English dictionary will look like:
 ‘mar’:’apple’, ‘masa’:’table’, ‘doi’:’two’
- Update Romanian-English dictionary with ‘doi’ key. (use dictionary comprehension)
"""
d_re = {'mar': 'apple', 'masa': 'table', 'carte': 'book'}
print(d_re)
d_me = {key: d_re[key] for key in ['mar', 'masa']}
d_me['doi'] = 'two'  # adaug cuvantul 'doi' in dictionar
print(d_me)
