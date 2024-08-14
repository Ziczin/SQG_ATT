from argparse import ArgumentParser
from replace_string import replacing

if __name__ == "__main__":
    parcer = ArgumentParser()

    parcer.add_argument("cfg", help="The path to the configuration file")
    parcer.add_argument("text", help="The path to the file being processed")
    parcer.add_argument("--log", action="store_true", help="Enables the display of file contents")
    parcer.add_argument("--genconf", action="store_true", help="Generating configuration file")
    parcer.add_argument("--gentext", action="store_true", help="Generating text file")
    parcer.add_argument("--genall", action="store_true", help="Generating all files")
    parcer.add_argument("--showcount", action="store_true", help="show the number of substitutions")

    args = parcer.parse_args()

    log = lambda *x: 1
    if args.log:
        print("PREPARING")
        print("Initializing the logger")
        from log import Log
        log = Log()
        log.is_log = True
    
    if args.genconf or args.genall:
        from gen import generate_configuration_file
        log("Generating configuration file")
        generate_configuration_file()
        
    if args.gentext or args.genall:
        from gen import generate_text_file
        log("Generating text file")
        generate_text_file()
    
    log()
    log("INPUT DATA")
    with open(args.cfg, 'r') as file:
        config = file.readlines()
        log("Config: " + str(config))
        config = [line.strip() for line in config]

    with open(args.text, 'r') as file:
        text = file.readlines()
        log("Text: " + str(text))
        text = [line.strip() for line in text]

    log()
    log("PROCESSED DATA")
    log("Config: " + str(config))
    log("Text: " + str(text))

    log()
    log("PROCESSING")
    data = []
    for i, line in enumerate(text):
        log(str(i + 1) + ". Line: " + line)
        res = replacing(line, config)
        log("Count: " + str(res[1]) + " | Result: " + res[0] )
        data.append(res)

    log()
    log("SORTING")
    log("Raw data: " + str(data))
    data = sorted(data, key=lambda x: x[1], reverse=True)
    log("Sorted data: " + str(data))

    log()
    log("RESULT")
    for line in data:
        if args.showcount or args.log:
            print(str(line[1]) + " : ", end="")
        print(line[0])

