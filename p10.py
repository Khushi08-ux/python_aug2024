#Program to check if the alphabet is Vowel or Consonant

character = input("Enter a character: ")  
 
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
   
if character in vowels:  
    print(f"The character '{character}' is a vowel!")  
else:  
    print(f"The character '{character}' is a consonant")