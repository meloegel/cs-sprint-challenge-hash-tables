#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    route = [None] * length

    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    destination = cache['NONE']
    for flight in range(length):
        route[flight] = destination
        destination = cache[destination]
    return route
