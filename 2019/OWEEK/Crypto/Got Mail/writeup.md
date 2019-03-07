***Got Mail (100pts)***  
_Description_: Some french guy sent me a message and i have no clue what it is (I don't even speak French!). Can anyone give me a language lesson?  
  
TIWZJ EUD YOTPUYI EC HC SOXOTL YUQAZZ ZPGGXMEK OLLZGIUGG! SAA'Z FLTG AYU? APIENE, TICS DW FOWB JRGGXTTPP MLCQ WJKQO{UI5O_R3LD_OI_S3L}  
  
_Solutions_  
* Notice the string with '{' and '}', it might be the flag.  
* ```WJKQO``` would be the flag format ```OWEEK```, but the double Es are changed to JK => Not substitution cipher  
* From description => French cipher => Vigenere  
* Need to find the key to decrypt the cipher, keep cracking the key with known text such as flag format OWEEK, words follow ```'```, question words, etc.  
  
_Key__: MELOVEHACKING  
_Flag_: OWEEK{JU5T_N3ED_MY_K3Y}  
_Notes_: Ignore whitespace (and special characters lile _) while encrypting/decrypting
