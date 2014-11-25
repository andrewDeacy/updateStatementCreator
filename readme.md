Really simple way to create an update statement in MS SQL if you have the rows you want to update in a seperate txt file. 

For example if I wanted to update all the columns in testData.txt, I'd input the table, column, and where column name and then it would output the folloing:

Update tblTest
Set Value1 =  2
Where TestData = 1111
or TestData = 3333
or TestData = 4444
or TestData = 5555
or TestData = 6666