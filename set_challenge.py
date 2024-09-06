python_workshop = {"Alice", "Bob", "Charlie"}
data_science_workshop = {"Diana", "Eve", "Bob"}


# Define a function to add an attendee to a workshop.
def add_attendee(workshop, attendee):
    workshop.add(attendee)


# Define a function to remove an attendee from a workshop.
def remove_attendee(workshop, attendee):
    if attendee in workshop:
        workshop.remove(attendee)


# Define a function to perform the following set operations:
# Find attendees who are attending both workshops (Intersection)
def find_common_attendees(workshop1, workshop2):
    return workshop1.intersection(workshop2)


# Find attendees who are attending only one workshop (Difference)
def find_unique_attendees(workshop1, workshop2):
    return workshop1.symmetric_difference(workshop2)


# Combine all attendees from both workshops (Union)
def combine_attendees(workshop1,workshop2):
    return workshop1.union(workshop2)


# Check if a specific person is attending either workshop (membership check)
def is_attended(workshop1, workshop2, participant):
    return participant in workshop1 or participant in workshop2


def display_attendees(workshop):
    print(f"Attendees: {', '.join(workshop)}")


print(display_attendees(python_workshop))
