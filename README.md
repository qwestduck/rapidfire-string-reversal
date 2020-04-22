# String Reversal

## Description

In language of choice:
- Write a routine that reverses a string in place.
- Write a routine that reverses each word in a string (words are characters separated by spaces).
- Write a routine that reverses the order of words in a string.

## Concessions

Since python has immutable strings, I consider temporarily storing a string in a mutable structure, performing manipulations, and then converting back to a string to not violate the "in-place" constraint as long as multiple list structures are not used to violate the spirit of the constraint.