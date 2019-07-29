# [Questions](https://github.com/keikeito/Questions/wiki)

# [i18n Builder](https://github.com/keikeito/Questions/tree/master/i18n%20Builder)
## the format of the IDs I chose is MD5 
* The text to be translated was replaced with a unique ID using MD5, which has a hash function that generates 128-bit values based on text of arbitrary length.
* You can always get the same value from the same input value, but you can get a completely different value from a slightly different input value.
* By determining the hash value from the input value and output value, it is possible to detect whether the text of markup has been changed, so it is possible to determine whether it is already translated text or not.
*　You can create translated language files in json format and manage them for each language.
