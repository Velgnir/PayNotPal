from src.MindController import mind_controller
import sys

if __name__ == "__main__":
    script_name = sys.argv[0]
    arguments = sys.argv[1:]
    mind_controller(arguments)