import pandas as pd
import numpy as np
import game
import math
import time
#update recursion limit
data = pd.read_csv("dataset.csv")

#User Interations
def user_input():
    print("Welcome to the Game Recommendation Find!")
    #User selects specfic filters if desired    
    sortChoice = ["","","","10"]
    # Choose platform
    platforms = data['platforms'].unique()
    while True:
        print("Platforms:\n1. PC   2. PS4\n3. Switch   4. Xbox 1\n5. Xbox X   6. PS5\n7. Apple Arcade   8. iOS\n9. Stadia   10. 3DS\n"
            "11.PS Vita   12.Wii u\n13. PS3   14. Xbox 360\n15. PSP   16. DS\n17. Wii   18. PS2\n19. Gameboy Advanced   20. GameCube\n"
            "21. Xbox   22. PlayStation\n23. Dreamcast   24. Nintendo 64\n25. Skip")  
        c =  int(input("Please Choose Platform: "))
        if c>0 and c< 25:
            sortChoice[0] = platforms[c-1]
            break
        elif c == 25:
            break
        else:
            print("Try Again!")
    # Choose Genre
    genres = data['genre'].unique()
    while True:
        print("Genres:\n1.Sports   2. Turn-based\n3. Wargame   4. Role-playing\n5.First Person   6.Real-time\n7.Strategy    8. Fighting\n9. Adventure   10. Action\n"
            "11. Wrestling   12. Platformer\n13. Racing   14. Simulation\n15. Flight   16. Third-Person\n17. Puzzle   18. Party\n19. Skip")
        c =  int(input("Please Choose Platform: "))
        if c>0 and c<19:
            sortChoice[1] = genres[c-1]        
            break
        elif c == 19:
            break
        else:
            print("Try Again!")
    # Choose year 
    c = input("Would you like to choose a year? Y or N ")
    if c == "N" or c == "n":
        pass
    elif c == "Y" or c == "y":
        while True:
            date = int(input("Please select date between 1994-2021: "))
            if date < 2022 and date > 1993:
                sortChoice[2] = str(date) 
                break
            else:
                print("Try Again!")
    else:
        print("Error. Please type Y or N.")
    # Choose number of games to reccommend
    num = int(input("How many games would you like to see? "))
    sortChoice[3] = str(num)
    print()
    # return selections ("" if skipped)    
    return sortChoice

def main():
    #instantiate a large data structure to hold all games
    test_all_games = game.GamesArray()
    #instantiate a game object for each game title
    for row in data.iterrows():
        #set empty metascore to be 0
        
        if math.isnan(row[1]['metascore']):
            temp_meta = 0.0
        else:
            temp_meta = float(row[1]["metascore"])
        #set empty userscore to 0
        
        
        if row[1]['userscore'] == 'tbd' or row[1]['userscore'] == '':
            temp_user = 0.0
        else:
            temp_user = float(row[1]["userscore"])

        #normalize values
        temp_user *= 10
        if temp_meta == 0.0:
            temp_meta = temp_user

        if temp_user == 0.0:
            temp_user = temp_meta
        
        
        temp_combined = (temp_user + temp_meta) / 2

        if math.isnan(temp_combined):
            temp_combined = 50
        temp_date = int(row[1]['date'][-4::])
    

        #instantiate game object with a single row of data
        temp = game.Game(row[1]["titles"], row[1]["platforms"], temp_meta, temp_user, row[1]["genre"], temp_date, temp_combined)
        #add game object to array
        test_all_games.add_game(temp)
    
    #returns arr[platform, genre, date, num_games]
    choices = user_input()
    #organaize return num items being sorted then pass int into parameter for sort
    organize_begin = time.perf_counter_ns()
    test_all_games.organize(choices)
    organize_time = time.perf_counter_ns() - organize_begin
    
    quickarr = test_all_games.game_list

    shellTime_begin = time.perf_counter()
    #CALL WITH COUNTER INSTEAD OF LEN OF LIST
    sorted2 = test_all_games.shell_sort(test_all_games.counter)
    shellTime_end = time.perf_counter_ns()
    print("Shell Sort Games")
    test_all_games.print_games(sorted2, int(choices[3]))

    quicksortTime_begin = time.perf_counter_ns()
    #CALL WITH COUNTER INSTEAD OF LEN OF LIST
    sorted = test_all_games.quicksort(quickarr)
    #sorted = test_all_games.itquicksort(quickarr, 0, test_all_games.counter - 1)
    quicksortTime_end = time.perf_counter_ns()  
    print("Quick Sort Games")
    test_all_games.print_games(sorted, int(choices[3]))

    print()
    print(f"The time it took with quicksort was  + {round(quicksortTime_end - quicksortTime_begin + organize_time, 2)}" + " nano seconds")
    print(f"The time it took with shellsort was  + {round(shellTime_end - shellTime_begin + organize_time, 2)}" + " nano seconds")
    print(organize_time)


if __name__ == "__main__":
    main()


