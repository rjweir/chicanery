import argparse

parser = argparse.ArgumentParser(
    description="Backup tool based on duplicity"
    )
subparsers = parser.add_subparsers(title="subcommands")
parser_abc = subparsers.add_parser('genkeys', help="Generate GPG keys to be used by duplicity")
parser_abc = subparsers.add_parser('backup', help="Actually perform a backup")
parser_abc = subparsers.add_parser('restore', help="Restore a previously made backup")

def go(args):
    values = parser.parse_args(args)
    print "got", args
    print "parsed", values
