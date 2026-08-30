# https://crackmes.one/crackme/6a768ab608712c1a17cbacdd

Interesting crackme, there is solving steps:

1) Disassembly XorGate and found main function
2) Then I analyzed code and look for XORing methods and then i saw that pretty logic:

for (local_450 = 0; local_450 &lt; sVar2; local_450 = local_450 + 1) {
snprintf(local_218 + local_458,0x200 - local_458,"%02x",
(ulong)(byte)(local_422[local_450 + 10] ^ 0x23));
local_458 = local_458 + 2;
}
builtin_strncpy(local_422,"@password",10);
for (local_448 = 0; local_448 &lt; 9; local_448 = local_448 + 1) {
local_218[local_458] = local_422[local_448];
local_458 = local_458 + 1;
}

so the algorithm is simple:
1) Program take user input
2) XOR each char in users input with 0x23 offset
3) Converts each XORed byte to a 2-character hex string
4) Appends the string @password to the hex string
5) And then compares this with the password input

so i write a simple python program which will generate password for any username, I used xivi and got 5b4a554a@password and... It works! Program said that i solved this and gave me a flag.

Answer: FLAG{SoulReaper_XOR_Crackme}
