import sys, os, argparse, platform, logging, re

if __name__ == "__main__":
    LOG_FILENAME = "lab2.log"

    parser = argparse.ArgumentParser(

        # describe what this program does & how it works inside --help
        description='Search for the string passed in from command line '
                    'from inside the file passed in from the command line'
                    ' and log the whole process to learn import libraries')

    # create argument for a log file
    parser.add_argument("--log_file",
                        default="lab2.log",  # WinnieJeng.txt
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
                        required=True,
                        type=str,
                        action="store")

    try:
        args = parser.parse_args()
        # print(sys.argv)
    except argparse.ArgumentError:
        print("ERROR")
        sys.exit()

    # parse command line arguments
    # args = parser.parse_args()

    file_name = args.log_file.name
    # print(file_name)

    """The commented out section is an alternative way of finding the file name passed in from argparse"""
    # # convert args to string in order to search/extract the name of the passed-in file
    # args_into_str = str(args)

    # # if the log file is found, open the log file,
    # set the file to file_name. Otherwise terminate the program
    # name = re.search("name=\'(.+?)\'", args_into_str)
    # file_name = name.group(1)

    # if not os.path.exists(file_name):
    #     parser.error("Invalid file name")
    #     sys.exit()

    with args.log_file as file:

        # print(file_name)

        f = open(file_name, 'r')
        # for line in f:
        #     print(line)
        # # print(f)
        # # # this commented out snippet reads the file and prints out all of it
        # # print(file.read())
        #
        # parse the file into lines
        lines = f.readlines()
        # read file line by line
        for line in lines:
            # if command line argument string is found in file, print line
            if re.search(args.string, line):
                logging.info(" " + line)
                print(line)

        """this commented out snippet checks if my above code logic is correct"""
        # if args.string in open(file_name).read():
        #     print("true")
        # else:
        #     print("not true")

    logging.basicConfig(filename=file_name,
                        level=logging.INFO,
                        format='%(asctime)s,%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    try:
        file = open(file_name, "a")
    except IOError:
        print("File not found")

    logging.info(" Program has started")
    logging.info(" command line options: --help, --log_file, --parse, --string")
    platform_info = str(" "+platform.platform())
    logging.info(platform_info)
    login_id = str(" "+os.getlogin())
    logging.info(login_id)


