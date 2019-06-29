# Title: vrs_classes.py
# Author: Aaron Chan (Chana030102) & Dustin Schnelle (schnelled)
# Date: 1/24/2019
#
# Classes for the Viking Robotics Society discord bot
# ==============================================================================
# Classes:
#           -> Session(object): Session objects represent individual meeting
#                               times during the current term. It stores the
#                               individual session's meeting day, start time,
#                               and end times.
#           -> Event(object):   The Event object is a method of managing all of
#                               the sessions during the current term.

import datetime, os, time

#-------------------------------------------------------------------------------
# Class:        Session
# Methods:
#               -> __init__ (initialize)
# Variables:
#               -> weekday: Day of the week which the session is occuring
#               -> startTime: Start time of the session
#               -> endTime: End time of the session
# Description:  Class to organize individual session times.
#-------------------------------------------------------------------------------
class Session(object):
    #---------------------------------------------------------------------------
    # Function:     initialize (__init__)
    # Input:        None
    # Output:       None
    # Definition:   Initialize the Session class object.
    #---------------------------------------------------------------------------
    def __init__(self, day, start, end):
        # Initialize the day of the week, start time, and end time
        self.weekday = day
        self.startTime = start
        self.endTime = end

#-------------------------------------------------------------------------------
# Class:        Event
# Methods:
#               -> __init__ (initialize)
#               -> add
#               -> remove
#               -> checkTime
#               -> update
# Variables:
#               -> file: The file where the tinker time data is stored.
#               -> sessions: An array of session class objects.
#               -> term: The current term for the tinkering sessions.
#               -> lastUpdated: The last time the tinker times file was updated.
# Description:  Class to add, remove, and modify events during a current term.
#               The event class is an array of independent session classes.
#-------------------------------------------------------------------------------
class Event(object):
    #---------------------------------------------------------------------------
    # Function:     initialize (__init__)
    # Input:        -> tinkerfile - file where the tinker time information is
    #                   stored.
    # Output:       None
    # Description:  Read the tinkering times from the tinker_times.txt file.
    #               Initialize the sessions array for storing session information.
    #               Initialize the information (weekday, startTime, & endtime)
    #               for the sessions.
    #---------------------------------------------------------------------------
    def __init__(self, tinkerfile):
        # Initialize the tinkering session file
        self.file = tinkerfile

        # Open the file (read only) with tinker time information
        with open(self.file, 'r') as f:
            # Read the tinker time information
            read_data = f.read()
        # Close the file with tinker time information
        f.close()

        # Initialize an empty sessions array to store Session objects
        self.sessions = []
        # Use the read tinker time information to initialize the term, time, and last updated date of the session
        self.term, times, self.lastUpdated, unused = read_data.split('\n')
        # Check for empty or single tinker time in the file
        if times != '' and times.find('|') != -1:
            # Spilt the times information for each session during the term
            times = times.split("|")

        # Check for existing tinker times in the file
        if times != '':
            # Loop for the number of sessions (tinker times)
            for i in range(0,len(times)):
                # Spilt the information for the session time
                data = times[i].split(",")
                # Create new instance of a Session object
                newSession = Session(data[0], data[1], data[2])
                # Append the current session into the sessions array
                self.sessions.append(newSession)

    #---------------------------------------------------------------------------
    # Function:     add
    # Input:        -> day - String representing the day of the week.
    #               -> start - Starting time of the tinkering session.
    #               -> end - Ending time of the tinkering session.
    # Output:       None
    # Description:  Add the new tinkering session into the event class.
    #---------------------------------------------------------------------------
    def add(self, day, start, end):
        # Open the file (read only) with tinker time information
        with open(self.file, 'r') as f:
            # Read the tinker time information
            read_data = f.read()
        # Close the tinker time text file
        f.close()

        # Use the read tinker time information to initialize the term, time, and last updated date of the session
        self.term, times, self.lastUpdated, unused = read_data.split('\n')
        # Check if there is an entry for a tinker time
        if times != '':
            # Spilt the times information for each session during the term
            times = times.split("|")

        # Check if this the first time entry
        if times == '':
            # Initialize the times variable with the first tinker time
            times = day + ',' + start + ',' + end
            # Display information about the added section
            print("Added {},{},{} to tinker_time.txt".format(day, start, end))
        # Otherwise session(s) already exist
        else:
            # Loop for the number of sessions (tinker times)
            for i in range(0,len(times)):
                # Spilt the information for the session time
                data = times[i].split(",")

                # Check if the new date is less than the current date in the times array
                if int(day) < int(data[0]):
                    # Insert the added entry to current location
                    times.insert(i, day + ',' + start + ',' + end)
                    # Add the session to the sessions list
                    self.addSession(day, start, end)
                    # Display information about the added section
                    print("Added {},{},{} to tinker_time.txt".format(day, start, end))
                    # Join the times array into a single times string
                    times = '|'.join(times)
                    break
                # Check if new date is equal to current date in times array
                elif int(data[0]) == int(day):
                    # Obtain start times and end times
                    oldStart = data[1]
                    oldStart = int(oldStart[0:2])
                    oldEnd = data[2]
                    oldEnd = int(oldEnd[0:2])
                    newStart = int(start[0:2])
                    newEnd = int(end[0:2])
                    # Check if the new entry is valid
                    if not self.checkTime(newStart, newEnd, oldStart, oldEnd):
                        # Insert the added entry to current location
                        times.insert(i, day + ',' + start + ',' + end)
                        # Add the session to the sessions list
                        self.addSession(day, start, end)
                        # Display information about the added section
                        print("Added {},{},{} to tinker_time.txt".format(day, start, end))
                        # Join the times array into a single times string
                        times = '|'.join(times)
                        break
                    # Otherwise the new entry is invalid
                    else:
                        # Display invalid entry
                        print("Error: {},{},{} is an invalid entry".format(day, start, end))
                        # Join the times array into a single times string
                        times = '|'.join(times)
                        break
                # Check if new date is the greatest of all dates in time array
                elif i == (len(times) - 1):
                    # Insert the added entry to current location
                    times.append(day + ',' + start + ',' + end)
                    # Display information about the added section
                    print("Added {},{},{} to tinker_time.txt".format(day, start, end))
                    # Add the session to the sessions list
                    self.addSession(day, start, end)
                    # Join the times array into a single times string
                    times = '|'.join(times)
                    break
                # Otherwise the new date is greater then the current date in the time array
                else:
                    pass

        # Update the last modification date and time
        self.lastUpdated = self.update()

        # Open the tinker time text file for writing
        with open(self.file, 'w+') as f:
            # Write to the tinker time text file
            f.write("{}\n{}\n{}\n".format(self.term, times, self.lastUpdated))
        # Close the tinker time text file
        f.close()

    #---------------------------------------------------------------------------
    # Function:     remove
    # Input:        -> day - The day of the session to be removed.
    #               -> start - The start time of the session to be removed.
    #               -> end - The end time of the session to be removed.
    # Output:       None
    # Description:  Removes a current tinkering session from the event class.
    #---------------------------------------------------------------------------
    def remove(self, day, start, end):
        # Session time to be removed
        toRemove = day + ',' + start + ',' + end

        # Open the file (read only) with tinker time information
        with open(self.file, 'r') as f:
            # Read the tinker time information
            read_data = f.read()
        # Close the tinker time text file
        f.close()

        # Use the read tinker time information to initialize the term, time, and
        # last updated date of the session
        self.term, times, self.lastUpdated, unused = read_data.split('\n')
        # Spilt the times information for each session during the term
        times = times.split("|")

        # Initialize the index
        i = 0
        # Loop for the number of sessions (tinker times) in the list of strings
        while i < len(times):
            # Check for the matching session string to be removed
            if times[i] == toRemove:
                # Display information about the deleted section
                print("Deleted {},{},{} from tinker_time.txt".format(day, start, end))
                # Remove the specified session from the list of session strings
                del times[i]
            else:
                # Increment the index
                i += 1

        # Loop for the number of sessions (tinker times) in the list of session objects
        for i, o in enumerate(self.sessions):
            # Check for matching session object to be removed
            if o.weekday == day and o.startTime == start and o.endTime == end:
                # Remove the specified session from the list of session objects
                del self.sessions[i]
                break

        # Transform the list of times into a times string
        times = '|'.join(times)

        # Open the tinker time text file for writing
        with open(self.file, 'w+') as f:
            # Write to the tinker time text file
            f.write("{}\n{}\n{}\n".format(self.term, times, self.lastUpdated))
        # Close the tinker time text file
        f.close()

    #---------------------------------------------------------------------------
    # Function:     addSession
    # Input:        -> day - The day of the added session time.
    #               -> start - The start time of the added session time.
    #               -> end - The end time of the added session time.
    # Output:       None
    # Description:  Creates new session instance and ddds the new session time
    #               to the sessions list.
    #---------------------------------------------------------------------------
    def addSession(self, day, start, end):
        # Create new instance of a Session object
        newSession = Session(day, start, end)

        # Loop for the number of sessions (tinker times) in the list of session objects
        for i, o in enumerate(self.sessions):
            # Check if the new session's meeting day is less than the current session in the list
            if o.weekday > day:
                # Insert the new session into the current index location
                self.sessions.insert(i, newSession)
                break
            # Check if the new session's meeting day is equal to the current session in the list
            elif o.weekday == day:
                # Obtain the new and old session times
                oldStart = o.startTime
                oldStart = int(oldStart[0:2])
                oldEnd = o.endTime
                oldEnd = int(o.endTime[0:2])
                newStart = start[0:2]
                newEnd = end[0:2]
                # Check if the new entry is valid
                if not self.checkTime(newStart, newEnd, oldStart, oldEnd):
                    # Insert the new session into the current index location
                    self.sessions.insert(i, newSession)
                    break
                # Otherwise the new entry is invalid
                else:
                    break
            # Check if the end of the session list has been reached
            elif i == (len(self.sessions) - 1):
                    # Append the new session into the list
                    self.sessions.append(newSession)
                    break
            # Otherwise the new session's meeting time is greater than the current session in the list
            else:
                pass

    #---------------------------------------------------------------------------
    # Function:     checkTime
    # Input:        -> newStart - Start time of the new tinker session.
    #               -> newEnd - End time of the tinker old tinker session.
    #               -> oldStart - Start time of the old tinker session.
    #               -> oldEnd - End time of the old tinker session.
    # Output:       If the new start time is valid.
    # Description:  Checks if the new tinker session time and the old tinker
    #               session time have conflicts. If a conflict is found then true
    #               will be returned otherwise false will be returned.
    #---------------------------------------------------------------------------
    def checkTime(self, newStart, newEnd, oldStart, oldEnd):
        # Check if the new start time is less than the old start time
        if newStart < oldStart:
            # Check if the new end time is less than the old end time
            if newEnd < oldEnd:
                # Check if the new end time is less than the old start time
                if newEnd < oldStart:
                    # Set the overlapping time error to false
                    overlapError = False
                # Check if the new end time is equal to the old start time
                elif newEnd == oldStart:
                    # Set the overlapping time error to false
                    overlapError = False
                # Otherwise the new end time is greater than the old start time
                else:
                    # Set the overlapping time error to true
                    overlapError = True
            # Check if the new end time is equal to the old end time
            elif newEnd == oldEnd:
                # Set the overlapping time error to true
                overlapError = True
            # Otherwise the new end time is greater than the old end time
            else:
                # Set the overlapping time error to true
                overlapError = True
        # Check if the new start time is equal to the old start time
        elif newStart == oldStart:
            # Check if the new end time is less than the old end time
            if newEnd < oldEnd:
                # Set the overlapping time error to true
                overlapError = True
            # Check if the new end time is equal to the old end time
            elif newEnd == oldEnd:
                # Set the overlapping time error to true
                overlapError = True
            # Otherwise the new end time is greater than the old end time
            else:
                # Set the overlapping time error to true
                overlapError = True
        # Otherwise the new start time is greater than the old start time
        else:
            # Check if the new end time is less than the old end time
            if newEnd < oldEnd:
                # Set the overlapping time error to true
                overlapError = True
            # Check if the new end time is equal to the old end time
            elif newEnd == oldEnd:
                # Set the overlapping time error to true
                overlapError = True
            # Otherwise the new end time is greater than the old end time
            else:
                # Check if the new start time is less than the old end time
                if newStart < oldEnd:
                    # Set the overlapping time error to true
                    overlapError = True
                # Check if the new start time is equal to the old start time
                elif newStart == oldStart:
                    # Set the overlapping time error to false
                    overlapError = False
                # Otherwise the new start time is greater than the old start time
                else:
                    # Set the overlapping time error to false
                    overlapError = False

        # Return the overlapping time error value
        return overlapError


    #---------------------------------------------------------------------------
    # Function:     update_file
    # Input:        None
    # Output:       String with current date and time.
    # Description:  Produce an updated date and time string to be written to the
    #               file.
    #---------------------------------------------------------------------------
    def update(self):
        # Update the last modification date and time
        year = datetime.datetime.today().year
        month = datetime.datetime.today().month
        date = datetime.datetime.today().day
        hour = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
        return str(year) + '-' + str(month) + '-' + str(date) + ' ' + str(hour) + ':' + str(min)

#-------------------------------------------------------------------------------
# Function:     testClasses
# Input:        None
# Output:       None
# Description:  Test the functionality of the classes, so new methods can be
#               fully tested before being added to the VRS Discord server.
#-------------------------------------------------------------------------------
def testClasses():
    # Obtain current working directory
    testDir = os.getcwd()
    # Modify the directory
    testDir = testDir.replace("Include", "Test/tinker_times.txt")

    # Initialize instance for testings events
    testEvent = Event(testDir)

    # Initialize test sequence array for addition test
    # Wednesday, Monday, Friday, Tuesday, Saturday, Sunday, Thursday
    addSeq = ['3','1','5','2','6','0','4']
    # Initialize test sequence of start times for time conflict test
    startSeq = ['08:00','08:00','08:00', '08:00', '08:00', '12:00', '12:00', '12:00', '14:00', '14:00', '14:00', '16:00', '18:00']
    # Initialize test sequence of end times for the time conflict test
    endSeq = ['14:00', '12:00', '10:00', '16:00', '18:00', '14:00', '16:00', '18:00', '15:00', '16:00', '18:00', '20:00', '20:00']

    # Exaustively test the addition of tinker times
    for i in range(0,len(addSeq)):
        # Add a tinker time from test sequence
        testEvent.add(addSeq[i], '12:00', '16:00')
        # Sleep for 1 seconds
        time.sleep(1)

    # Exaustive test of the add/remove feature without time conflicts
    for i in range(0, 7):
        # Remove current indexed session
        testEvent.remove(str(i), '12:00', '16:00')
        # Sleep for 1 seconds
        time.sleep(1)
        # Add current indexed session
        testEvent.add(str(i), '12:00', '16:00')
        # Sleep for 1 seconds
        time.sleep(1)

    # Exaustively test the add feature with time conflicts
    for i in range(0,len(startSeq)):
        # Add current indexed session
        testEvent.add(str(3), startSeq[i], endSeq[i])
        # Sleep for 1 seconds
        time.sleep(1)
        # Remove the successful addition
        if i == 1 or i == 2 or i == 11 or i == 12:
            # Remove successful addition
            testEvent.remove(str(3), startSeq[i], endSeq[i])
            # Sleep for 1 seconds
            time.sleep(1)

    # Reset the test
    for i in range(0, 7):
        # Remove current indexed session
        testEvent.remove(str(i), '12:00', '16:00')


# If classes is run as a script then run the test case
if __name__ == '__main__':
    testClasses()
