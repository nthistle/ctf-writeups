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
