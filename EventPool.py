class EventPool():
    # EventPool is a class for keeping a list of tracks
    # for event mixing procedure for correlation analysis
    def __init__(self, targettracksize=0):
        # Event pool has:
        # - a size that must be reached before event mixing can start
        self.targettracksize = targettracksize
        # - a pool of previous events
        self.eventpool = []
    
    # Method for checking if event pool is ready
    def is_ready(self):
        if sum([len(event) for event in self.eventpool]) >= self.targettracksize:
            print("Event pool - target track size reached: " + str(sum([len(event) for event in self.eventpool])))
            return True
        return False
    
    # Method for adding a new event to the pool
    def add(self, newevent):
        self.eventpool.append(newevent)
        if sum([len(event) for event in self.eventpool]) - len(self.eventpool[0]) > self.targettracksize:
            self.eventpool.pop(0)

    # Method for getting a list of all tracks in event pool
    def trackpool(self):
        return [track for event in self.eventpool for track in event]
