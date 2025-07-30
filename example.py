#!/usr/bin/env python3
\"\"\"
An example Python script created as part of the tinyzk GitHub API demonstration.
\"\"\"

def hello_tinyzk():
    \"\"\"
    A simple function that returns a greeting message.
    \"\"\"
    return \"Hello, TinyZK! This is an example script.\"

def main():
    \"\"\"
    Main function to execute the script.
    \"\"\"
    message = hello_tinyzk()
    print(message)

if __name__ == \"__main__\":
    main()