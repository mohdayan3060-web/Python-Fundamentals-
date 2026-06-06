# Q1. The Alternating Capitalizer (Medium)
# Write a function alternate_caps(text) that takes a string and returns a new string where every alternate alphabetic character is capitalized, starting with the first character. Spaces and punctuation should be ignored for the counting but preserved in the output.
# Example: "hello world!" ➔ "HeLlO wOrLd!"

# def alternate_caps(greet):
#     for item in greet[::2]:
#         greet=item.capitalize()
#         print(greet)

# alternate_caps("hello world")

# --------------------------------------------------------------------    --------------------------------        ------------------
#string compress 
# def string_compress(s):
#     result=""
#     n=len(s)
#     for i in range(n):
#         count =1
#         while i<n-1 and s[i]==s[i+1]:
#             count +=1
#             i+=1

#         result +=s[i]
#         result +=str(count)
    
#     return result            

# text="aabbccddd"
# print(string_compress(text))

# -------------------------------------------------------------------------------------------------------
# Q3. The Word Length Grouping (Medium)
# Write a function group_by_length(words_list) that takes a list of strings and returns a dictionary. The keys should be the length of the words (integers), and the values should be a list of words that have that length.
# Example: ["apple", "bat", "cat", "banana", "dog"] ➔ {5: ["apple"], 3: ["bat", "cat", "dog"], 6: ["banana"]}
grp = ["apple", "bat", "cat", "banana", "dog"]
for item in grp:
    print(item)

def group_lenght(grp):
    my_dict={}
        

import pickle

with open('person.pkl','rb') as f:
    obj=pickle.load(f)
    