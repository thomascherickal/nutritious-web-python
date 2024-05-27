import argparse
import os
import sys
from nutritious import translate, translate_file


def main(args):
    parser = argparse.ArgumentParser(description='Translate .py files in app/ directory to .py in specified output directory')
    parser.add_argument('--write', action='store_true', help='Write output to specified directory')
    parser.add_argument('--appdir', type=str, default='app', help='Input directory (default: app/)')
    parser.add_argument('--outdir', type=str, default='dist', help='Output directory (default: dist/)')

    args = parser.parse_args(args)
    target_directory = args.appdir
    output_directory = args.outdir

    if args.write and not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for root, dirs, files in os.walk(target_directory):
        for filename in files:
            if filename.endswith('.py'):
                py_filename = filename
                full_pkd_path = os.path.join(root, filename)
                full_py_path = os.path.join(output_directory, py_filename) if args.write else None

                if args.write:
                    translate_file(full_pkd_path, full_py_path)
                else:
                    py_contents = translate(open(full_pkd_path, 'r').read())
                    print(f'--- {py_filename} ---\n{py_contents}\n')

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))