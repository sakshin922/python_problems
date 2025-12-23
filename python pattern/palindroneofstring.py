def is_palindrome(s):
 
  s = s.lower() 
  return s == s[::-1]


string1 = "Madam"
string2 = "hello"
string3 = "Racecar"

print(f"'{string1}' is a palindrome: {is_palindrome(string1)}")
print(f"'{string2}' is a palindrome: {is_palindrome(string2)}")
print(f"'{string3}' is a palindrome: {is_palindrome(string3)}")