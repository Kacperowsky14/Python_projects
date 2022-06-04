def category():
    numbers = (1,2,3,4,5,6,7,8,9,10,11,12)
    print("Select number from the following")
    list_of_categories = ("1.All 2.Sports 3.World 4.Politics 5.Technology 6.Startup 7.Entertainment 8.Miscellaneous 9.Hatke 10.Science 11.Automobile, 12.Business")
    print(list_of_categories)
    try:
        chose = int(input(""))
    except:
        print("There is no such category")
        error = 1
        return(error)
    if chose == 1:
        category = "all"
    if chose == 2:
        category = "sports"
    if chose == 3:
        category = "world"
    if chose == 4:
        category = "politics"
    if chose == 5:
        category = "technology"
    if chose == 6:
        category = "startup"
    if chose == 7:
        category = "entertainment"
    if chose == 8:
        category = "miscellaneous"
    if chose == 9:
        category = "hatke"
    if chose == 10:
        category = "science"
    if chose == 11:
        category = "automobile"
    if chose == 12:
        category = "business"
    if chose not in numbers:
        print("There is no such category")
        error = 1
        return(error)
    if chose in numbers:
        return(category)