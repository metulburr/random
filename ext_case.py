
'''
convert file extensions to uppercase or lowercase, recurisve, path, and extionsion type changable options
purpose: to easily allow adaptable change of peoples programs that program in windows not knowing that linux is case sensitive

#help
python ext_case.py -h

#default settings, change to file extensions to lowercase in this files current directory
python ext_case.py

#recusively change only jpg file extensions in path /home to uppercase
python ext_case.py -r -e ['jpg'] -p /home -u

#recursively change default file extensions to lowercase
python ext_case.py -r
./Images/Tiles/Magma.PNG -> ./Images/Tiles/Magma.png
./Images/Tiles/l.JPG -> ./Images/Tiles/l.jpg
./Images/Tiles/User/Ur.PNG -> ./Images/Tiles/User/Ur.png

'''



import argparse
import os

class Control:
    def __init__(self):
        
        self.extensions = ['png', 'jpg', 'jpeg', 'gif', 'pdf']
        self.parser = argparse.ArgumentParser(description='Convert Arguments')
        self.parser.add_argument(
            '-l','--lowercase', 
            action='store_true', 
            help='Convert file extensions in path to lowercase'
        )
        self.parser.add_argument(
            '-u','--uppercase', 
            action='store_true', 
            help='Convert file extensions in path to uppercase'
        )
        self.parser.add_argument(
            '-p', '--path', 
            default='.',
            help='Specify root path, default is current directory'
        )
        self.parser.add_argument(
            '-r', '--recursive', 
            action='store_true',
            help='Change files in recursive directories'
        )
        self.parser.add_argument(
            '-e', '--extensions', 
            default=self.extensions,
            help='Specify extensions to convert as a list of strings, default is {}, arguments take ext in lowercase format'.format(self.extensions)
        )
        self.parser.add_argument(
            '-f', '--filename', 
            action='store_true',
            help='Modify filenames to match image string used to load'
        )

        self.args = vars(self.parser.parse_args())

        self.path = self.args['path']
        self.case = None #true for upper, false/none for lower
        self.rec = self.args['recursive']
        self.ext = self.args['extensions']
        
        if self.args['uppercase']:
            self.case = True
        elif self.args['lowercase']:
            self.case = False
        
        self.print_info()
        self.handle_extensions()
        self.handle_filenames()
    
    def print_info(self):
        if self.case:
            c = 'Uppercase'
        else:
            c = 'Lowercase'
        print('Path: "{}"\nCase: {}\nRecursive: {}\nExtensions: {}\n'.format(self.path, c, self.rec, self.ext))
        
    def handle_filenames(self):
        pass
        
    def handle_extensions(self):
        if self.rec:
            for root, dirs, files in os.walk(self.path):
                for name in files:
                    self.change_file_ext(root, name)
        else:
            for f in os.listdir(self.path):
                self.change_file_ext(self.path, f)
                        
    def change_file_ext(self, root, f):
        base, ext = os.path.splitext(f)
        if ext[1:].lower() in self.ext:
            old = os.path.join(root, f)
            new = None
            if self.case: #convert to upper
                if ext[1:].islower():
                    new = os.path.join(root, base + ext.upper())
            else:
                if ext[1:].isupper():
                    new = os.path.join(root, base + ext.lower())
            if new:
                print('{} -> {}'.format(old, new))
                os.rename(old, new)


app = Control()
