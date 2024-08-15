"""
Amazon's software team utilizes several algorithms to maintain data integrity, one of which targets the encoding of symmetrical names. Symmetrical names are unique in that they read identically in both directions, similar to palindromes in language parlance.
The chief aim of the algorithm is to rearrange the characters in the original symmetrical name according to these criteria:
• The rearranged name is a reshuffled version of the original symmetrical name.
• The restructured name should be symmetrical as well.
• This restructured name should be lexicographically smallest among all its symmetric permutations.
Given an initial symmetrical name that contains only lowercase English characters, compute the encoded name.
A string s is considered to be lexicographally smaller than the string t of the same length if the first character in s that differs from that in t is smaller. For example,
"abcd" is lexicographically smaller than "abdc" but larger than "abad"
Note that the output encoded name could match the original name if it's already the smallest lexicographically.

Example
The original string is nameString = "babab".
This can be reversed to give "abbba", which is a symmetric rearrangement of the original symmetrical name and is the smallest possible reverse order.
It satisfies all the requirements so return the string abbba.
Function Description
Complete the function computeEncodedProductName in the editor below.
computeEncodedProductName has the following parameter:
string nameString: the initial symmetrical string name.
Returns
string: the encoded nameString
Constraints
• 1 ≤ /nameString/ ≤ 105
• nameString consists of lowercase English letters only.
• nameString is a palindrome.

Sample Input For Custom Testing
STDIN
FUNCTION
ухху
→
nameString = "yxxy"
Sample Output

хуух

Explanation
Rearrange the original nameString to generate "хуух",
which is a palindrome and also the smallest possible

• Sample Case 1
Sample Input For Custom Testing
STDIN
FUNCTION
ded
nameString = "ded"
Sample Output
ded

"""