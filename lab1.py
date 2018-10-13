def file_open(file):
    try:
        file = open(file, "w")

        """
        A note to self: 
            To open the file in unix, 
            type cat {file.name} into the cmdline
        """

    except IOError:
        print("file does not exist")
    return file


if __name__ == "__main__":

    # calling the file opening function
    f = file_open("WinnieJeng.txt")

    # list of my fav movies
    movies = ["Frozen", "Little Mermaid", "The Incredibles", "Lion King", "Tangled"]

    # list of my fav places
    places = ["Home", "Friend's house", "Cafe", "School", "Work"]

    # list of my fav python features
    features = ["Monty Python", "Garbage Collection", "Libraries", "GUI", "What is Your Name"]

    # loop through each item in the zip lists
    for (movie, place, feature) in zip(movies, places, features):
        # write items to the file with nice format
        f.write(movie.ljust(20)),
        f.write(place.center(20)),
        f.write(feature.rjust(20)),
        f.write("\n")

        """The commented out code also works!!"""
        # f.write("{0:<20}".format(movie)),
        # f.write("{0:^20}".format(place)),
        # f.write("{0:>20}\n".format(feature))

    # good practices
    f.flush()
    f.close()
