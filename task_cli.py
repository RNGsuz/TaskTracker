import argparse

def cmd_add(args):
    print("ADD aufgerufen mit:", args.description)

def cmd_list(args):
    print("LIST aufgerufen")

def build_parser():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add
    p_add = subparsers.add_parser("add", help="Neue Aufgabe hinzufügen")
    p_add.add_argument("description", type=str, help="Beschreibung der Aufgabe")
    p_add.set_defaults(func=cmd_add)

    # list
    p_list = subparsers.add_parser("list", help="Aufgaben anzeigen")
    p_list.set_defaults(func=cmd_list)

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
