# Safe
Keepsafe Application utilizing (my own) Pass5 key encryption. 

## Description 
A keepsafe application based on my own personal symmetric key encription (Pass5). The application works with a physical USB "key" that contains both keys needed to encrypt and decrypt (ID / IDOG as named on Pass5). When the USB "key" (which is also named key) is plugged in, the application is able to read in the information from the key and the front end reads the encrypted keepsafe information. 

## What does it do?
- You get to create a "safe", where you can store username/password combinations. 
- The program automatically re-encrypts all the informations if a certain amount of time has passed since the last time the program was used (and the key is correct, of course). This amount of time can be changed as desired.

## Furute updates
- Add graphics for a nicer user interface. 
- Add option to write, read and encrypt specific text files, not just the safe. 

## How to run
Download the code (Safe3.7) and run the python code. (You would need to download Pass5 as well, which is right now a private project. You may contact for more information).

## Logs
- Safe3.7 (Newst version)
- Safe3 (Similar version, added auto-recryption and new key generation, lots of bugs)
- Safe2 (Added ability to generate a new key and re-encrypt for that new key)
- Safe1 (Original project)
