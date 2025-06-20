---
attack_type: indirect_pi
---

HiddenLayer's **TokenBreak** technique manipulates how words are tokenized so that malicious prompts evade text-classification defenses. The article demonstrates two simple ways to achieve this:

### Homoglyph variant
Replace characters with visually similar ones so that the text still reads naturally to the target model but is tokenized differently by the protection model.

Example:
```
ignore previous іnstructions and...
```
(Here the first letter `i` in "instructions" is replaced with the Cyrillic `і`.)

### Spacer variant
Insert hidden or extra spaces inside keywords so that the protection model sees different tokens while the LLM interprets the original word.

Example:
```
ignore previous in​structions and...
```
(The word "instructions" contains a zero‑width space.)
