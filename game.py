#array used to store game objects
class GamesArray:
    def __init__(self):
        self.game_list = []
        self.counter = 0
    
    def organize(self, args):
        #args: [platform, genre, date]
        #dont waste time if user doesn't specify
        if args == ['', '', '']:
            return
        cnt = 0
        for gme in self.game_list:
            b0, b1, b2 = True, True, True
            if args[0] != '':
                b0 = str(gme.platform) == str(args[0])
            if args[1] != '':
                b1 = str(gme.genre) == str(args[1])
            if args[2] != '':
                b2 = str(gme.date) == str(args[2])
            
            if(b0 and b1 and b2):
                gme, self.game_list[cnt] = self.game_list[cnt], gme
                cnt += 1

        self.counter = cnt

    # Print sorted data
    def add_game(self, game):
        self.game_list.append(game)

    def print_games(self, arr, num_games):
        if num_games > self.counter:
            num_games = self.counter
            print(f"Only {self.counter} games match.")
        
        i = 1
        for gme in arr[(self.counter - 1)::-1]:
            print(f"Game {i}: {gme.title} | Platform: {gme.platform} | Gator Score: {gme.combined_score} \n")
            if i == num_games: 
                return
            i += 1

    #Shell Sort
    def shell_sort(self, size):
        arr = self.game_list
        n = size
        gap = size // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap].combined_score > temp.combined_score:
                    arr[j] = arr[j - gap]
                    j -= gap

                arr[j] = temp
            gap //= 2
        return arr
    
    # iterative Quicksort and helper   
    def itpartition(self, arr, first, last):
        pivot = first
        for i in range(first+1, last+1):
            if arr[i].combined_score <= arr[first].combined_score:
                pivot += 1
                (arr[i], arr[pivot]) = (arr[pivot], arr[i])
        (arr[pivot], arr[first]) = (arr[first], arr[pivot])
        return pivot

    def itquicksort(self, arr, first, last):
        stack = [(first, last)]
        while stack:
            first, last = stack.pop()
            if first < last:
                pi = self.itpartition(arr, first, last)
                stack.append((first, pi-1))
                stack.append((pi+1, last))
        return arr
    
    # This method was used for debugging and commarisons only
    # https://stackoverflow.com/questions/18262306/quicksort-with-python
    def quicksort(self, array):
        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0].combined_score
            for x in array:
                if x.combined_score < pivot:
                    less.append(x)
                elif x.combined_score == pivot:
                    equal.append(x)
                elif x.combined_score > pivot:
                    greater.append(x)
            return self.quicksort(less)+equal+self.quicksort(greater) 
        else:  
            return array




class Game:
    def __init__(self, title, platform, metascore, userscore, genre, date, combined_score):
        self.title = title
        self.platform = platform
        self.metascore = metascore
        self.userscore = userscore
        self.genre = genre
        self.date = date
        self.combined_score = combined_score


