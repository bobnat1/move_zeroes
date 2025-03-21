# Move Zeroes 
The objective of the Move Zeroes problem is to take a list and filter out all the zeroes by moving them to the back of the list.

## Real World use cases
### Filtering Data
This algorithim can be used as a simple solution to do a basic data cleanse. For example, you imported a spreadsheet in Python and you need to filter out redundant data that is only convoluting the main data. At the same time, you need to retain all of the data and avoid data loss. Instead of deleting the redundant data, you could use a method like Move Zeroes to move the elements to the back of your list  -  which would effectively retain the data. Please refer to the move_element.py file for reference.

##  My Approach
My approach is very simple with this problem - here is the psuedo code in order:
1) start a loop to iterate over the provided array
2) if the current element in the array is equal to the provided element parameter-
3) then copy the current element and add it to the end of the array
4) afterwards, remove the current element you just copied to the back from it's orginal spot in the array

please refer to `move_zeroes.js` to see an example

## Extra
- Per the **Real World use cases** section from above - I re-wrote the problem in Python to show a real world example of filtering out a requested value from a list. In this example, I generated a random list of key value pairs to signify data extracted from an excel sheet. I use the same process as I did with the zeroes, and the end result is being able to filer out the `None` values and adding them to the end of the list. Please refer to `move_element.py` 
- I also have have the `move_element.js` written in JS to filter out elements in an integer list.
