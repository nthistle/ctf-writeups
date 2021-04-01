# Mod 26

## Challenge

> Author: Pandu
>
> Points: 10
>
> Description: Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}`

## Solution

[ROT13](https://en.wikipedia.org/wiki/ROT13) is a very common basic cipher, which just consists of shifting letters halfway through the alphabet. We can use an online tool such as [this one](https://cryptii.com/pipes/rot13), or we can write some basic Python code:

```python
import string
alphabet = string.ascii_lowercase

def rot13(s):
    out = ""
    for ch in s:
        if ch in alphabet:
            idx = alphabet.index(ch)
            out += alphabet[(idx + 13) % 26]
        elif ch.lower() in alphabet:
            idx = alphabet.index(ch.lower())
            out += alphabet[(idx + 13) % 26].upper()
        else:
            out += ch
    return out

print(rot13("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}"))
```

Which gives us the flag, `picoCTF{next_time_I'll_try_2_rounds_of_rot13_Aphnytiq}`.

