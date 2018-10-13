import sys, os, argparse, platform, logging, re

if __name__ == "__main__":
    LOG_FILENAME = 'WinnieJeng.txt'

    parser = argparse.ArgumentParser(
        # describe what this program does & how it works inside --help
        description='Search for the string passed in from command line '
                    'from inside the file passed in from the command line'
                    ' and log the whole process to learn import libraries')

    # create argument for a log file
    parser.add_argument("--log_file",
                        default=LOG_FILENAME,
                        help="Pass in the log file",
                        type=argparse.FileType("r"),
                        action="store")
    # create argument for parse file
    parser.add_argument("--parse",
                        help="Parse the argument",
                        required=True,
                        action="store")
    # create argument for string file
    parser.add_argument("--string",
                        help="Search the string in the file that's passed in",
                        # required=True,
                        type=str,
                        action="store")

    args = parser.parse_args()
    print(args)

    str22 = args.string
    # print(str)

    with args.log_file as file:
        print(LOG_FILENAME)
        # for str22 in file:
        #     print(str22)
        print(file.read())

    if str22 in open('WinnieJeng.txt').read():
        print("true")
    # do stuff
