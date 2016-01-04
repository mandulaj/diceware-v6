# diceware-v6
Next generation diceware password generator - randomness guaranteed!!!

####WTF is this???
Diceware is a popular and fun way of generating military grade passwords that are **money-back-guaranteed** to be to be random!!! Most diceware password list only provide 7776 words of which many are short or contain special characters (yikes). `diceware-v6` brings a revolution by introducing the extended **46656** word-list with words up to 10 characters long.

####How to generate a secure random password

Diceware is very easy to use. All you need is a die. It can help to get hold of 6 dice in order to speed up the RNG (1 die runs out of entropy very quickly).

1. Download and verify the signed diceware file from [`https://raw.githubusercontent.com/zpiman/diceware-v6/master/diceware-v6.txt.asc`](https://raw.githubusercontent.com/zpiman/diceware-v6/master/diceware-v6.txt.asc) - *You can also download the 6pg PDF and print it out in font-size 2* 
2. Roll the die 6 times and record numbers eg. `131512` - *alternatively you can roll 6 dice at once*
3. Look up the word corresponding to the number in the diceware file.
4. This is the first word of your password eg.`131512 awesome`
5. Repeat the steps 2-4 until you have a password of the desired length. 6 or more words are going to provide a better-than-good password. Check the section below for information on security.

####Security

46656 words might seam like a very small number to be considered secure. However the power of diceware comes from the number of words. There are 46656 was to choose 1 word, however 2176782336 ways to choose 2 words. The more words are added, the more secure the password.

#####This table shows the security of different password lengths. Anything in *bold* is imo overkill....

| # of Words | Password permutations                                 | Time to brute force (100B/s) |
|:----------:|:------------------------------------------------------| -----------------------------|
| 1          | `46656`                                               | light travels about 100 m    |
| 2          | `2176782336`                                          | 0.02 seconds                 |
| 3          | `101559956668416`                                     | 16 minutes                   |
| 4          | `4738381338321616896`                                 | 1.5 years                    |
| 5          | `221073919720733357899776`                            | 70 millennia                 |
| 6          | `10314424798490535546171949056`                       | 3.3 billion years            |
| 7          | `481229803398374426442198455156736`                   | 150 trillion years           |
| **8**      | **`22452257707354557240087211123792674816`**          | **7.1 quintillion years**    |
| **9**      | **`1047532535594334222593508922191671036215296`**     | **330 sextillion years**     |
| **10**     | **`48873677980689257489322752273774603865660850176`** | **something-crazyllion**     |
