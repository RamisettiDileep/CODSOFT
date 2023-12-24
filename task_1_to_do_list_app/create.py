import argparse

parser = argparse.ArgumentParser(description='Create your TODO list.')
parser.add_argument('--list', type=str, dest="todo",
                    help='Enter your todo list as a string')

args = parser.parse_args()
print("Your created todo list:")
print(args.todo)


