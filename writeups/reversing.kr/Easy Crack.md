First Challenge from reversing.kr

1) Run the program and enter something, then i got a message box with "Incorrect Password" so then I summarise all information i have now
 1. It's WinAPI window
 2. There is no text in window
 3. Button have no text too
 4. When i enter something, messagebox with error appears
 5. Message box said "Incorrect Password"

2) I went to Ghidra and dissamble this binary, look thru the "Incorrect Password" string, and found password check system
  ```
  if (local_63 == 'a') {
    iVar3 = _strncmp(&local_62,&DAT_00406078,2);
    if (iVar3 == 0) {
      pcVar4 = s_AGR3versing_0040606a;
  ```
  and 
  ```
  if ((iVar3 == 0) && (local_64 == 'E')) {
        MessageBoxA(param_1,s_Congratulation_!!_00406044,s_EasyCrackMe_00406058,0x40);
  ```
  From these parts of decompiled code, we can see, that program checking our input, and as we can see, password starts from E, than a and 2 unknown symbols from DAT_00406078
  Hop on DAT_00406078, and see "5" and "y" then put it together and match with our past seachings => "Ea5y" Yay! We get first part of password

  But, as you can see pcVar4 is s_AGR3versing_0040606a; an then in code, we see operation with skipping first two symbols from AGR3versing => "R3versing" We found the second part

3) Matched first part of code "Ea5y" with "R3versing" and we get "Ea5yR3versing" that's final password, we did it!

Answer: Ea5yR3versing
