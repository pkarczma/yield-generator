class EventPool():
    # EventPool is a class for keeping a list of tracks
    # for event mixing procedure for correlation analysis
    def __init__(self, targeteventsize=0, targettracksize=0):
        # Event pool has:
        # - a size that must be reached before event mixing can start
        self.targeteventsize = targeteventsize
        self.targettracksize = targettracksize
        # - a pool of previous events
        self.eventpool = []
    
    # Method for checking if event pool is ready
    def is_ready(self):
        if len(self.eventpool) >= self.targeteventsize:
            print("Event pool - target event size reached: " + str(len(self.eventpool)))
            if sum([len(event) for event in self.eventpool]) >= self.targettracksize:
                print("Event pool - target track size reached: " + str(sum([len(event) for event in self.eventpool])))
                return True
        return False
    
    # Method for adding a new event to the pool
    def add(self, newevent):
        self.eventpool.append(newevent)
        if len(self.eventpool) > self.targeteventsize:
            if sum([len(event) for event in self.eventpool]) > self.targettracksize:
                self.eventpool.pop()

    # Method for getting a list of all tracks in event pool
    def trackpool(self):
        return [track for event in self.eventpool for track in event]
