this crackme can be solved 2 ways.
1) u can just patch JZ LAB_140018397 to NOP and u will get "Accesses granted" message
2) the second way -
local_1e0 = 0x61;
local_1df = 0x23;
local_1de = 0x6c;
local_1dd = 0x36;
local_1dc = 0x37;
local_1db = 0x27;
local_1da = 0x67;
local_1d9 = 100;
local_1d8 = 0x62;
this is the password in hex, let's conver it to char: a#l67'gdb
but it will be incorrect cuz original password XORed (thunk_FUN_140017ad0(local_170,(longlong)&amp;local_1e0,9,0x55);)
u need unXOR a#l67'gdb to 4v9cbr217

Answer: 4v9cbr217
