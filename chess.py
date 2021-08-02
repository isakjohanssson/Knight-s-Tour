class Square():
    def __init__(self, pos_x, pos_y):
        self.pos = (pos_x, pos_y)
        self.is_occupied = False
        self.next = None
        self.prev = None
        self.possible_nexts = None
    
    def occupy(self):
        self.is_occupied = True
    
    def leave(self):
        self.is_occupied = False
    

class ChessBoard():
    def __init__(self, size, start_pos):
        self.squares = {(pos_x, pos_y): Square(pos_x, pos_y) for pos_x in range(size) for pos_y in range(size)}
        self.start = self.squares[start_pos]
        self.current = self.start
        self.allowed_steps = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,1), (2,-1)]

        #occupy starting pos and set the next possible steps
        self.current.occupy() 
        self.current.possible_nexts = self.order_nexts(self.find_nexts()) 

    def complete(self):
        return all([self.squares[square].is_occupied for square in self.squares])

    def take_step(self):
        if self.current.possible_nexts:
            self.go_fwd()
        else:
            self.go_back()
        return
    
    def go_fwd(self):
        nexts = self.current.possible_nexts
        ordered_nexts = self.order_nexts(nexts)

        next_square = ordered_nexts[0]
        self.current.next = next_square
        next_square.prev = self.current
        self.current = next_square
        self.current.occupy()
        self.current.possible_nexts = self.order_nexts(self.find_nexts(next_square.pos))
        return
        
    def go_back(self):
        self.current.leave()
        self.current = self.current.prev
        self.current.next = None
        if self.current.possible_nexts:
            self.current.possible_nexts.pop(0)
        return
    
    def find_nexts(self, regr_square=False):
        nexts = []
        for step in self.allowed_steps:

            if not regr_square:
                pos = tuple(map(sum, zip(self.current.pos, step)))
            else:
                pos = tuple(map(sum, zip(regr_square, step)))
            if (pos in self.squares and not self.squares[pos].is_occupied):
                if not pos == regr_square:
                    nexts.append(self.squares[pos])
        return nexts

    def order_nexts(self, nexts):
        d_next_to_next_nexts = {next: self.find_nexts(next.pos) for next in nexts}
        return sorted(d_next_to_next_nexts, key=lambda k: len(d_next_to_next_nexts[k]), reverse=False)

        
    def run(self):
        while not self.complete():
            self.take_step()
        return
        
    def get_run(self):
        run_list=[]
        square = self.start
        while square is not None:
            run_list.append(square.pos)
            square = square.next
        return run_list