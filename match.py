# Instead of writing many if else statements, use the match statement instead
numbers = 5
print("Simple use of match statement:")
match numbers:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3: 
        print("Three")
    case 4:
        print("Four")
    case 5: 
        print("Five")
    case 6:
        print("Six")
    case 7:
        print("Seven")

# Use the underscore character _ as the last case value if you want to execute a code block when there are no other matches:
day = 3
print("Using underscore character in a match statement:")
match day:
    case 1:
        print("Today is Thursday")
    case 2:
        print("Today is Friday")
    case _:
        print("Looking Forward to Christmas Break")

# Use the pipeline | as an or operator in the case evaluation to check for more than one value match in one case
day = 4
print("Pipeline as an operator:")
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today I am working onsite!")
  case 6 | 7:
    print("Today I am working from home!")

# if statement in case evaluation as an extra condition-check
print("if statement as an extra condition-check:")
month = 12
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 11:
        print("A weekday in November")
    case 1 | 2 | 3 | 4 | 5 if month == 12:
        print("A weekday in December")
    case _:
        print("No match")


