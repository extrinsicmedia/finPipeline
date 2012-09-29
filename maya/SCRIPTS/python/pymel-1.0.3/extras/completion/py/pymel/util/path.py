"""
Example:

from path import path
d = path('/home/guido/bin')
for f in d.files('*.py'):
    f.chmod(0755)

This module requires Python 2.2 or later.


URL:     http://www.jorendorff.com/articles/python/path
Author:  Jason Orendorff <jason.orendorff@gmail.com> (and others - see the url!)
Date:    7 Mar 2004
"""

import codecs
import fnmatch
import glob
import grp
import os
import pwd
import re
import shutil
import sys
import warnings

from posix import *

class path(str):
    """
    Represents a filesystem path.
    
    For documentation on individual methods, consult their
    counterparts in os.path.
    """
    
    
    
    def __add__(self, more):
        """
        # Adding a path and a string yields a path.
        """
    
        pass
    
    
    def __div__(self, rel):
        """
        fp.__div__(rel) == fp / rel == fp.joinpath(rel)
        
        Join two path components, adding a separator character if
        needed.
        """
    
        pass
    
    
    def __radd__(self, other):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def __truediv__(self, rel):
        """
        fp.__div__(rel) == fp / rel == fp.joinpath(rel)
        
        Join two path components, adding a separator character if
        needed.
        """
    
        pass
    
    
    def abspath(self):
        pass
    
    
    def access(self, mode):
        """
        Return true if current user has access to this path.
        
        mode - One of the constants os.F_OK, os.R_OK, os.W_OK, os.X_OK
        """
    
        pass
    
    
    def basename(p):
        """
        Returns the final component of a pathname
        """
    
        pass
    
    
    def bytes(self):
        """
        Open this file, read all bytes, return them as a string.
        """
    
        pass
    
    
    def canonicalpath(self):
        """
        Attempt to return a 'canonical' version of the path
        
        This will standardize for symbolic links, absolute/relative paths,
        case differences (if on a case-insensitive file system), and '..'
        usage (so paths such as A//B, A/./B and A/foo/../B will all compare equal).
        
        The intention is that string comparison of canonical paths will yield
        a reasonable guess as to whether two paths represent the same file.
        """
    
        pass
    
    
    def chgrp(self, group):
        pass
    
    
    def chmod(self, mode):
        pass
    
    
    def chown(self, uid, gid):
        pass
    
    
    def chroot(self):
        pass
    
    
    def copy(src, dst):
        """
        Copy data and mode bits ("cp src dst").
        
        The destination may be a directory.
        """
    
        pass
    
    
    def copy2(src, dst):
        """
        Copy data and all stat info ("cp -p src dst").
        
        The destination may be a directory.
        """
    
        pass
    
    
    def copyfile(src, dst):
        """
        Copy data from src to dst
        """
    
        pass
    
    
    def copymode(src, dst):
        """
        Copy mode bits from src to dst
        """
    
        pass
    
    
    def copystat(src, dst):
        """
        Copy all stat info (mode bits, atime, mtime, flags) from src to dst
        """
    
        pass
    
    
    def copytree(src, dst, symlinks=False, ignore=None):
        """
        Recursively copy a directory tree using copy2().
        
        The destination directory must not already exist.
        If exception(s) occur, an Error is raised with a list of reasons.
        
        If the optional symlinks flag is true, symbolic links in the
        source tree result in symbolic links in the destination tree; if
        it is false, the contents of the files pointed to by symbolic
        links are copied.
        
        The optional ignore argument is a callable. If given, it
        is called with the `src` parameter, which is the directory
        being visited by copytree(), and `names` which is the list of
        `src` contents, as returned by os.listdir():
        
            callable(src, names) -> ignored_names
        
        Since copytree() is called recursively, the callable will be
        called once for each directory that is copied. It returns a
        list of names relative to the `src` directory that should
        not be copied.
        
        XXX Consider this example code rather than the ultimate tool.
        """
    
        pass
    
    
    def dirname(self):
        pass
    
    
    def dirs(self, pattern=None, realpath=False):
        """
        D.dirs() -> List of this directory's subdirectories.
        
        The elements of the list are path objects.
        This does not walk recursively into subdirectories
        (but see path.walkdirs).
        
        With the optional 'pattern' argument, this only lists
        directories whose names match the given pattern.  For
        example, d.dirs('build-*').
        """
    
        pass
    
    
    def exists(path):
        """
        Test whether a path exists.  Returns False for broken symbolic links
        """
    
        pass
    
    
    def expand(self):
        """
        Clean up a filename by calling expandvars(),
        expanduser(), and normpath() on it.
        
        This is commonly everything needed to clean up a filename
        read from a configuration file, for example.
        """
    
        pass
    
    
    def expanduser(self):
        pass
    
    
    def expandvars(self):
        pass
    
    
    def files(self, pattern=None):
        """
        D.files() -> List of the files in this directory.
        
        The elements of the list are path objects.
        This does not walk into subdirectories (see path.walkfiles).
        
        With the optional 'pattern' argument, this only lists files
        whose names match the given pattern.  For example,
        d.files('*.pyc').
        """
    
        pass
    
    
    def fnmatch(self, pattern):
        """
        Return True if self.name matches the given pattern.
        
        pattern - A filename pattern with wildcards,
            for example '*.py'.
        """
    
        pass
    
    
    def get_groupname(self):
        """
        get the group name for this file
        """
    
        pass
    
    
    def get_owner(self):
        """
        Return the name of the owner of this file or directory.
        
        This follows symbolic links.
        
        On Windows, this returns a name of the form ur'DOMAIN\User Name'.
        On Windows, a group can own a file or directory.
        """
    
        pass
    
    
    def getatime(filename):
        """
        Return the last access time of a file, reported by os.stat().
        """
    
        pass
    
    
    def getctime(filename):
        """
        Return the metadata change time of a file, reported by os.stat().
        """
    
        pass
    
    
    def getmtime(filename):
        """
        Return the last modification time of a file, reported by os.stat().
        """
    
        pass
    
    
    def getsize(filename):
        """
        Return the size of a file, reported by os.stat().
        """
    
        pass
    
    
    def glob(self, pattern):
        """
        Return a list of path objects that match the pattern.
        
        pattern - a path relative to this directory, with wildcards.
        
        For example, path('/users').glob('*/bin/*') returns a list
        of all the files users have in their bin directories.
        """
    
        pass
    
    
    def isabs(s):
        """
        Test whether a path is absolute
        """
    
        pass
    
    
    def isdir(s):
        """
        Return true if the pathname refers to an existing directory.
        """
    
        pass
    
    
    def isfile(path):
        """
        Test whether a path is a regular file
        """
    
        pass
    
    
    def islink(path):
        """
        Test whether a path is a symbolic link
        """
    
        pass
    
    
    def ismount(path):
        """
        Test whether a path is a mount point
        """
    
        pass
    
    
    def joinpath(self, *args):
        """
        Join two or more path components, adding a separator
        character (os.sep) if needed.  Returns a new path
        object.
        """
    
        pass
    
    
    def lines(self, encoding=None, errors='strict', retain=True):
        """
        Open this file, read all lines, return them in a list.
        
        Optional arguments:
            encoding - The Unicode encoding (or character set) of
                the file.  The default is None, meaning the content
                of the file is read as 8-bit characters and returned
                as a list of (non-Unicode) str objects.
            errors - How to handle Unicode errors; see help(str.decode)
                for the options.  Default is 'strict'
            retain - If true, retain newline characters; but all newline
                character combinations ('\r', '\n', '\r\n') are
                translated to '\n'.  If false, newline characters are
                stripped off.  Default is True.
        
        This uses 'U' mode in Python 2.3 and later.
        """
    
        pass
    
    
    def link(self, newpath):
        """
        Create a hard link at 'newpath', pointing to this file.
        """
    
        pass
    
    
    def listdir(self, pattern=None):
        """
        D.listdir() -> List of items in this directory.
        
        Use D.files() or D.dirs() instead if you want a listing
        of just files or just subdirectories.
        
        The elements of the list are path objects.
        
        With the optional 'pattern' argument, this only lists
        items whose names match the given pattern.
        """
    
        pass
    
    
    def lstat(self):
        """
        Like path.stat(), but do not follow symbolic links.
        """
    
        pass
    
    
    def makedirs(self, mode=511):
        pass
    
    
    def mkdir(self, mode=511):
        pass
    
    
    def move(src, dst):
        """
        Recursively move a file or directory to another location. This is
        similar to the Unix "mv" command.
        
        If the destination is a directory or a symlink to a directory, the source
        is moved inside the directory. The destination path must not already
        exist.
        
        If the destination already exists but is not a directory, it may be
        overwritten depending on os.rename() semantics.
        
        If the destination is on our current filesystem, then rename() is used.
        Otherwise, src is copied to the destination and then removed.
        A lot more could be done here...  A look at a mv.c shows a lot of
        the issues this implementation glosses over.
        """
    
        pass
    
    
    def normcase(self):
        pass
    
    
    def normpath(self):
        pass
    
    
    def open(self, mode='r'):
        """
        Open this file.  Return a file object.
        """
    
        pass
    
    
    def pathconf(self, name):
        pass
    
    
    def read_md5(self):
        """
        Calculate the md5 hash for this file.
        
        This reads through the entire file.
        """
    
        pass
    
    
    def readlink(self):
        """
        Return the path to which this symbolic link points.
        
        The result may be an absolute or a relative path.
        """
    
        pass
    
    
    def readlinkabs(self):
        """
        Return the path to which this symbolic link points.
        
        The result is always an absolute path.
        """
    
        pass
    
    
    def realpath(self):
        pass
    
    
    def relpath(self):
        """
        Return this path as a relative path,
        based from the current working directory.
        """
    
        pass
    
    
    def relpathto(self, dest):
        """
        Return a relative path from self to dest.
        
        If there is no relative path from self to dest, for example if
        they reside on different drives in Windows, then this returns
        dest.abspath().
        """
    
        pass
    
    
    def remove(self):
        pass
    
    
    def removedirs(self):
        pass
    
    
    def rename(self, new):
        pass
    
    
    def renames(self, new):
        pass
    
    
    def rmdir(self):
        pass
    
    
    def rmtree(path, ignore_errors=False, onerror=None):
        """
        Recursively delete a directory tree.
        
        If ignore_errors is set, errors are ignored; otherwise, if onerror
        is set, it is called to handle the error with arguments (func,
        path, exc_info) where func is os.listdir, os.remove, or os.rmdir;
        path is the argument to that function that caused it to fail; and
        exc_info is a tuple returned by sys.exc_info().  If ignore_errors
        is false and onerror is None, an exception is raised.
        """
    
        pass
    
    
    def samefile(f1, f2):
        """
        Test whether two pathnames reference the same actual file
        """
    
        pass
    
    
    def samepath(self, otherpath):
        """
        Whether the other path represents the same path as this one.
        
        This will account for symbolic links, absolute/relative paths,
        case differences (if on a case-insensitive file system), and '..'
        usage (so paths such as A//B, A/./B and A/foo/../B will all compare equal).
        
        This will NOT account for hard links - use 'samefile' for this, if
        available on your os.
        
        Essentially just compares the self.canonicalpath() to other.canonicalpath()
        """
    
        pass
    
    
    def splitall(self):
        """
        Return a list of the path components in this path.
        
        The first item in the list will be a path.  Its value will be
        either os.curdir, os.pardir, empty, or the root directory of
        this path (for example, '/' or 'C:\\').  The other items in
        the list will be strings.
        
        path.path.joinpath(*result) will yield the original path.
        """
    
        pass
    
    
    def splitdrive(self):
        """
        p.splitdrive() -> Return (p.drive, <the rest of p>).
        
        Split the drive specifier from this path.  If there is
        no drive specifier, p.drive is empty, so the return value
        is simply (path(''), p).  This is always the case on Unix.
        """
    
        pass
    
    
    def splitext(self):
        """
        p.splitext() -> Return (p.stripext(), p.ext).
        
        Split the filename extension from this path and return
        the two parts.  Either part may be empty.
        
        The extension is everything from '.' to the end of the
        last path segment.  This has the property that if
        (a, b) == p.splitext(), then a + b == p.
        """
    
        pass
    
    
    def splitpath(self):
        """
        p.splitpath() -> Return (p.parent, p.name).
        """
    
        pass
    
    
    def stat(self):
        """
        Perform a stat() system call on this path.
        """
    
        pass
    
    
    def statvfs(self):
        """
        Perform a statvfs() system call on this path.
        """
    
        pass
    
    
    def stripext(self):
        """
        p.stripext() -> Remove one file extension from the path.
        
        For example, path('/home/guido/python.tar.gz').stripext()
        returns path('/home/guido/python.tar').
        """
    
        pass
    
    
    def symlink(self, newlink):
        """
        Create a symbolic link at 'newlink', pointing here.
        """
    
        pass
    
    
    def text(self, encoding=None, errors='strict'):
        """
        Open this file, read it in, return the content as a string.
        
        This uses 'U' mode in Python 2.3 and later, so '\r\n' and '\r'
        are automatically translated to '\n'.
        
        Optional arguments:
        
        encoding - The Unicode encoding (or character set) of
            the file.  If present, the content of the file is
            decoded and returned as a unicode object; otherwise
            it is returned as an 8-bit str.
        errors - How to handle Unicode errors; see help(str.decode)
            for the options.  Default is 'strict'.
        """
    
        pass
    
    
    def touch(self):
        """
        Set the access/modified times of this file to the current time.
        Create the file if it does not exist.
        """
    
        pass
    
    
    def unlink(self):
        pass
    
    
    def utime(self, times):
        """
        Set the access and modified times of this file.
        """
    
        pass
    
    
    def walk(self, pattern=None, errors='strict', regex=None):
        """
        D.walk() -> iterator over files and subdirs, recursively.
        
        The iterator yields path objects naming each child item of
        this directory and its descendants.  This requires that
        D.isdir().
        
        This performs a depth-first traversal of the directory tree.
        Each directory is returned just before all its children.
        
        The errors= keyword argument controls behavior when an
        error occurs.  The default is 'strict', which causes an
        exception.  The other allowed values are 'warn', which
        reports the error via warnings.warn(), and 'ignore'.
        """
    
        pass
    
    
    def walkdirs(self, pattern=None, errors='strict', realpath=False, regex=None):
        """
        D.walkdirs() -> iterator over subdirs, recursively.
        
        With the optional 'pattern' argument, this yields only
        directories whose names match the given pattern.  For
        example, mydir.walkdirs('*test') yields only directories
        with names ending in 'test'.
        
        The errors= keyword argument controls behavior when an
        error occurs.  The default is 'strict', which causes an
        exception.  The other allowed values are 'warn', which
        reports the error via warnings.warn(), and 'ignore'.
        """
    
        pass
    
    
    def walkfiles(self, pattern=None, errors='strict', regex=None):
        """
        D.walkfiles() -> iterator over files in D, recursively.
        
        The optional argument, pattern, limits the results to files
        with names that match the pattern.  For example,
        mydir.walkfiles('*.tmp') yields only files with the .tmp
        extension.
        """
    
        pass
    
    
    def write_bytes(self, bytes, append=False):
        """
        Open this file and write the given bytes to it.
        
        Default behavior is to overwrite any existing file.
        Call p.write_bytes(bytes, append=True) to append instead.
        """
    
        pass
    
    
    def write_lines(self, lines, encoding=None, errors='strict', linesep='\n', append=False):
        """
        Write the given lines of text to this file.
        
        By default this overwrites any existing file at this path.
        
        This puts a platform-specific newline sequence on every line.
        See 'linesep' below.
        
        lines - A list of strings.
        
        encoding - A Unicode encoding to use.  This applies only if
            'lines' contains any Unicode strings.
        
        errors - How to handle errors in Unicode encoding.  This
            also applies only to Unicode strings.
        
        linesep - The desired line-ending.  This line-ending is
            applied to every line.  If a line already has any
            standard line ending ('\r', '\n', '\r\n', u'\x85',
            u'\r\x85', u'\u2028'), that will be stripped off and
            this will be used instead.  The default is os.linesep,
            which is platform-dependent ('\r\n' on Windows, '\n' on
            Unix, etc.)  Specify None to write the lines as-is,
            like file.writelines().
        
        Use the keyword argument append=True to append lines to the
        file.  The default is to overwrite the file.  Warning:
        When you use this with Unicode data, if the encoding of the
        existing data in the file is different from the encoding
        you specify with the encoding= parameter, the result is
        mixed-encoding data, which can really confuse someone trying
        to read the file later.
        """
    
        pass
    
    
    def write_text(self, text, encoding=None, errors='strict', linesep='\n', append=False):
        """
        Write the given text to this file.
        
        The default behavior is to overwrite any existing file;
        to append instead, use the 'append=True' keyword argument.
        
        There are two differences between path.write_text() and
        path.write_bytes(): newline handling and Unicode handling.
        See below.
        
        Parameters:
        
          - text - str/unicode - The text to be written.
        
          - encoding - str - The Unicode encoding that will be used.
            This is ignored if 'text' isn't a Unicode string.
        
          - errors - str - How to handle Unicode encoding errors.
            Default is 'strict'.  See help(unicode.encode) for the
            options.  This is ignored if 'text' isn't a Unicode
            string.
        
          - linesep - keyword argument - str/unicode - The sequence of
            characters to be used to mark end-of-line.  The default is
            os.linesep.  You can also specify None; this means to
            leave all newlines as they are in 'text'.
        
          - append - keyword argument - bool - Specifies what to do if
            the file already exists (True: append to the end of it;
            False: overwrite it.)  The default is False.
        
        
        --- Newline handling.
        
        write_text() converts all standard end-of-line sequences
        ('\n', '\r', and '\r\n') to your platform's default end-of-line
        sequence (see os.linesep; on Windows, for example, the
        end-of-line marker is '\r\n').
        
        If you don't like your platform's default, you can override it
        using the 'linesep=' keyword argument.  If you specifically want
        write_text() to preserve the newlines as-is, use 'linesep=None'.
        
        This applies to Unicode text the same as to 8-bit text, except
        there are three additional standard Unicode end-of-line sequences:
        u'\x85', u'\r\x85', and u'\u2028'.
        
        (This is slightly different from when you open a file for
        writing with fopen(filename, "w") in C or file(filename, 'w')
        in Python.)
        
        
        --- Unicode
        
        If 'text' isn't Unicode, then apart from newline handling, the
        bytes are written verbatim to the file.  The 'encoding' and
        'errors' arguments are not used and must be omitted.
        
        If 'text' is Unicode, it is first converted to bytes using the
        specified 'encoding' (or the default encoding if 'encoding'
        isn't specified).  The 'errors' argument applies only to this
        conversion.
        """
    
        pass
    
    
    def getcwd(cls):
        """
        Return the current working directory as a path object.
        """
    
        pass
    
    
    __dict__ = None
    
    atime = None
    
    ctime = None
    
    drive = None
    
    ext = None
    
    groupname = None
    
    mtime = None
    
    name = None
    
    namebase = None
    
    owner = None
    
    parent = None
    
    size = None

__all__ = ['path']

__version__ = '2.1'
