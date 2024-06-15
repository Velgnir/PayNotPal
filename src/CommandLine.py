class arguments:
    @staticmethod
    def parse(argv):
        """
        Function for handling errors in script's initial arguments
        For errors or "--help" return None
        For "--help" prints out instruction message

        Parameters
        ----------
        argv: string
                script's initial arguments
        Returns
        -------
        args: dict or None
        """

        args = arguments.interpretate_args(argv)
        if args.get("--help", False):
            print("Arguments:\n\
                -f  - follows the name of the Function to be called\n\
                -i  - Input file containing a valid json\n\
                -o  - Output file containing the result (as json) of the function called\n\
                -ls - custom file for Logger Settings\n")
            return None
        if len(args["errors"]) != 0:
            errors = args["errors"]
            print(f"Error: {errors}\n")
            print(f"Incorrect arguments\n\
        try running --help\n")
            return None
        return args



    @staticmethod
    def interpretate_args(argv):
        """
        Function for parsing PNP's input arguments
        Returns dictionary, where
        each input of possible_command_options in argv is a key to
        it's value

        Parameters
        ----------
        argv: string
                script's initial arguments
        Returns
        -------
        args: dict
        """
        possible_command_options = {"-con","-base","-admin"}
        solo_command_options = {"--help","--fun"}


        arguments = argv[1:]
        args = {}

        # catching errors
        errors = ""

        i = 0
        while i < len(arguments) - 1:
            if arguments[i] in possible_command_options:
                if arguments[i + 1] not in possible_command_options and arguments[
                    i + 1] not in solo_command_options:
                    args[arguments[i]] = arguments[i + 1]
                    i += 1
                else:
                    errors += f"{arguments[i]} - argument missed;"
            elif arguments[i] in solo_command_options:
                args[arguments[i]] = True
            else:
                errors += f"{arguments[i]} - no such command option; "
            i += 1
        if i == len(arguments) - 1:
            if arguments[i] in possible_command_options:
                errors += f"{arguments[i]} - argument missed;"
            elif arguments[i] in solo_command_options:
                args[arguments[i]] = True
            else:
                errors += f"{arguments[i]} - no such command option; "
        args["errors"] = errors
        return args

    @staticmethod
    def order(argv):
        """
        Function for handling errors in script's initial arguments
        For errors or "--help" return None
        For "--help" prints out instruction message

        Parameters
        ----------
        argv: string
                script's initial arguments
        Returns
        -------
        args: dict or None
        """

        args = arguments.interpretate_args(argv)
        if args.get("--help", False):
            print("Arguments:\n\
                    delete - delete the following or sorted elements\n\
                    add - add the following object\n\
                    filter - actions"
                  )
            return None
        if len(args["errors"]) != 0:
            errors = args["errors"]
            print(f"Error: {errors}\n")
            print(f"Incorrect arguments\n\
            try running --help\n")
            return None
        return args
    @staticmethod
    def execute_table(argv):
        """
        Function for parsing PNP's command mode
        Returns dictionary, where
        each input of possible_command_options in argv is a key to
        it's value

        Parameters
        ----------
        argv: list of strings
                commands
        Returns
        -------
        args: dict
        """
        possible_command_options = {"filter", "delete", "add"}
        solo_command_options = {"--help"}

        arguments = argv[1:]
        args = {}

        # catching errors
        errors = ""

        i = 0
        while i < len(arguments) - 1:
            if arguments[i] in possible_command_options:
                if arguments[i + 1] not in possible_command_options and arguments[
                    i + 1] not in solo_command_options:
                    args[arguments[i]] = arguments[i + 1]
                    i += 1
                else:
                    errors += f"{arguments[i]} - argument missed;"
            elif arguments[i] in solo_command_options:
                args[arguments[i]] = True
            else:
                errors += f"{arguments[i]} - no such command option; "
            i += 1
        if i == len(arguments) - 1:
            if arguments[i] in possible_command_options:
                errors += f"{arguments[i]} - argument missed;"
            elif arguments[i] in solo_command_options:
                args[arguments[i]] = True
            else:
                errors += f"{arguments[i]} - no such command option; "
        args["errors"] = errors
        return args
