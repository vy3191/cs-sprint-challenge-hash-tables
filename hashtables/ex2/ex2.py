#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Create a hash table as per hint in the README
    # We can hash each ticket such that the starting location is the key and
    # the destination is the value
    trip_table = {}     # dict = {start:destination}
    for i in range(0, length):
        starting_location = tickets[i].source
        destination = tickets[i].destination
        trip_table[starting_location] = destination

    # let us create a list which contains the starting point
    starting_source = trip_table['NONE']   # 'LAX'
    trip_list = [starting_source]
    print(trip_table)
    # let us loop through the tickets list now
    for i in range(1, length):
        # grab the starting point
        starting_point =  trip_list[i-1]   #the first item in the list
        # if the starting point is in the trip table then push its destination to the trip list
        if starting_point in trip_table:
            # get the destination from the trip table
            destination = trip_table[starting_point]
            # push that destination to the list
            trip_list.append(destination)
            print(trip_list)
    
    return trip_list

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

# expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
#             "SLC", "PIT", "ORD", "NONE"]
result = reconstruct_trip(tickets, 10)    
print(result)
