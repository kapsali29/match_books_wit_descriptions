# match_books_wit_descriptions
A project that matches book titles to descriptions

## Explanation

**Explaining the Input** 
The first line indicates that the test case contains the names and descriptions of five popular books listed on Flipkart. 
The next five lines are the names of the books (i.e, Set A). After that, we have a separator. That is followed by five lines, each containing description fragments from Set B.

**Explaining how we arrived at the Output**
The first description, is visibly most closely related to the second book (Embedded / Real-Time Systems 1st Edition (Paperback)). 
The second description, is clearly about the Merchant of Venice - which is the third book name in Set-A. 
The third description is about Baking - and so, it corresponds to the first of the book names, in Set-A. Similarly, the fourth and fifth descriptions match best with the fourth and fifth book names (i.e, it so happens that they are already in order).

So, the expected output is 2, 3, 1, 4, 5 respectively.
