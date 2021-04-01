# Mind your Ps and Qs

## Challenge

> Author: Sara
>
> Points: 20
>
> In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](values)

## Solution

If you're familiar with [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)), the challenge description basically gives it away, but first thing we do is open up `values`, and see this:

```
Decrypt my super sick RSA:
c: 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n: 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e: 65537
```

We notice immediately that `n` is small. _Really_ small.

```python
>>> (769457290801263793712740792519696786147248001937382943813345728685422050738403253).bit_length()
269
```

Normally, I check [factordb.com](http://factordb.com/) first, and sure enough, it's [there](http://factordb.com/index.php?query=769457290801263793712740792519696786147248001937382943813345728685422050738403253). If you wanted to factor it yourself though, [SageMath](https://www.sagemath.org/) (which any self-respecting cryptographer should have installed) can do it, on my computer it takes about 12 minutes:

```python
sage: factor(769457290801263793712740792519696786147248001937382943813345728685422050738403253)
1617549722683965197900599011412144490161 * 475693130177488446807040098678772442581573
```

Once we have `n` factorized, decryption is straightforward:

```python
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
p = 1617549722683965197900599011412144490161
q = 475693130177488446807040098678772442581573

assert n == p * q

c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
e = 65537

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

m = pow(c, d, n)

import binascii
print(binascii.unhexlify(hex(m)[2:]))
```

Which gives us the flag, `picoCTF{sma11_N_n0_g0od_45369387}`

