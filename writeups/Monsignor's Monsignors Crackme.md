# https://crackmes.one/crackme/6a2c80595f26f108ba18b8bd

Like a most if people i faced a problem when .exe closes after typing something in it, so i go to Ghidra first and after the decompile found this:

iVar1 = strcmp(local_48,"secret");

Then i go to x64dbg, found the string with successful message and patch instruction jnz 0x00007FF6AC9A1582 to jnz 0x00007FF6AC9A1571 and it worked :D

Answer: Patched (00007FF6AC9A1571)
