# https://crackmes.one/crackme/6a5101752c3088f968e13412

recently i tried to solve this crackme, and find that it crushes after entering name, so i browse logic and here is what i got

1. We have an alphabet which contains accepted symbols
while ("ABCDEFGHJKLMNPQRSTUVWXYZ23456789"[iVar15] != (char)iVar5)

2. I find how many symbols can serial take
if (uVar26 != 0x1e)

3. I found and analyse algorithm of coding serial
FUN_140004880(local_b0, &amp;local_90) (for hashing)
FUN_140005640(&amp;local_90, &amp;local_110) (base32 convertation)

Then i wrote a keygen which will convert my name to the serial and i got this:
┌──(Nosoul㉿work)-[~/whatever]
└─$ python3 keygen.py
Name: xivi
Serial: 2LTG8-HXB32-LUPJC-ND63B-4BNYM-D8P35

Answer: name: xivi | serial: 2LTG8-HXB32-LUPJC-ND63B-4BNYM-D8P35 (probably can be not valid, but i could't check it ^^)
