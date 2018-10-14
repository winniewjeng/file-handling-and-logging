import sys, os, argparse, platform, logging, re

if __name__ == "__main__":

    """argument parser"""
    parser = argparse.ArgumentParser(

        # describe what this program does & how it works inside --help
        description='Search for the string passed in from command line '
                    'from inside the file passed in from the command line'
                    ' and log the whole process to learn import libraries')

    # create argument for a log file
    parser.add_argument("--log_file",
                        default="lab2.log",  # WinnieJeng.txt
                        help="Pass in the log file",
                        # type=argparse.FileType("r"), # crashes if arg != existing file
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

    """parsing begins"""
    # safely parse the command line arguments in a try/except block
    try:
        args = parser.parse_args()
        # print(sys.argv)
    except argparse.ArgumentError:
        print("Cannot parse the command line argument")
        sys.exit()

    """"set the three command line arguments to variables"""
    # extract the log file from command line argument
    log_name = args.log_file
    # extract the parsed file from command line argument
    file_name = args.parse
    # extract the string to be searched from command line argument
    search_string = args.string

    """The commented out section is an alternative way of finding the passed-in file's name
        # # convert args to string in order to search the passed-in file's name
        # args_into_str = str(args)

        # # if the log file is found, open the log file,
        # # set the file to file_name. Otherwise terminate the program
        # name = re.search("name=\'(.+?)\'", args_into_str)
        # file_name = name.group(1)

        # if not os.path.exists(file_name):
        #     parser.error("Invalid file name")
        #     sys.exit()
    """

    """logging module begins"""
    # safely start the log with BasicConfig method in a try/except block
    try:
        if log_name is not None:
            logging.basicConfig(filename=log_name,
                                level=logging.INFO,
                                # log should have date, time, logging level, and message
                                format='%(asctime)s, %(levelname)s, %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
    except ValueError:
        print("Cannot log to a non-existent file")
        logging.error("Cannot log to a non-existent file")
        sys.exit()

    logging.info(" =======================Log starts========================")
    logging.info(" command line options: --help, --log_file, --parse, --string")
    # store platform info and login id inside variables and convert them to strings
    platform_info = str(platform.platform())
    login_id = str(os.getlogin())
    platform_processor = str(platform.processor())
    platform_version = str(platform.version())
    # log the platform_info and login_id
    logging.info(" user {} on platform {}".format(login_id, platform_info))
    logging.info(" " + platform_version)
    logging.info(" Processor {}".format(platform_processor))
    # logging.info(login_id)

    """searching and logging the searched string begins"""
    # safely open the file
    try:
        # # create object file
        with open(file_name, 'r') as file:
            # # create file object f
            # file = open(file_name, 'r')

            # # this commented out snippet reads the file and prints out all of it
            # print(f.read())

            # parse the file object into lines
            lines = file.readlines()
            # read file object line by line
            for line in lines:
                # search for the command line argument string
                if re.search(search_string, line):
                    # # if found, log the entire line of where the string is found
                    # logging.info(line)
                    logging.info(" {} found on line: {} ".format(search_string, line))
            file.flush()
            file.close()
    # gracefully exit the program if no file is found
    except IOError:
        print("Cannot parse a non-existent file")
        logging.error("Cannot parse a non-existent file")
        logging.info(" =========================Log ends========================\n")
        sys.exit()

    logging.info(" =========================Log ends========================\n")
