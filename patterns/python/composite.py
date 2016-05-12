"""Composite design pattern (using filesystem example).

The Problem:

An application needs to manipulate a hierarchical collection of "primitive" and
"composite" objects. Processing a primitive object is handled one way, and
processing a composite object is handled another. Having to check the "type"
of each object before attempting to process it is not desirable.

Examples:
    - Directories and files in a filesystem
    - GUI Menu items, which themselves could have sub menus
    - Containers that contain items, each of which could be a container
"""

from abc import ABCMeta, abstractmethod


class FilesystemComponent(object):
    """Component."""

    __metaclass__ = ABCMeta

    def __init__(self, basename, parent=None):
        if isinstance(parent, File):
            raise ValueError("Parent cannot be a File")
        self.basename = basename
        self.parent = parent
        if self.parent:
            self.parent.contents[self.path] = self

    @abstractmethod
    def delete(self):
        pass

    @property
    def path(self):
        paths = [self.basename]
        parent = self.parent
        while parent:
            paths.insert(0, parent.basename)
            parent = parent.parent
        return "/".join(paths)

    def __repr__(self):
        return "{0}".format(self.path)


class Directory(FilesystemComponent):
    """Composite."""

    def __init__(self, basename, parent=None):
        super(Directory, self).__init__(basename, parent)
        self.contents = dict()

    def delete(self):
        """Delete this component and all sub components."""
        # Gather children paths to delete
        to_delete = [path for path in self.contents]
        # Remove children from this dirs contents
        for path in to_delete:
            self.contents[path].delete()
        # Delete this dir
        del self.parent.contents[self.path]
        self.parent = None


class File(FilesystemComponent):
    """Leaf."""

    def delete(self):
        """Delete only this component."""
        del self.parent.contents[self.path]
        self.parent = None


# Create filesystem tree and call delete() on component
root = Directory('home')
level1_dir1 = Directory('joe', root)
level1_file1 = File('foo.txt', root)
level2_dir1 = Directory('Documents', level1_dir1)
level2_file1 = File('.bashrc', level1_dir1)
level3_dir1 = Directory('Work', level2_dir1)
level3_file1 = File('work_file1.doc', level2_dir1)
level3_file2 = File('work_file2.doc', level2_dir1)
level4_file1 = File('work_file3.doc', level3_dir1)

# Path test
assert level4_file1.path == "home/joe/Documents/Work/work_file3.doc"

# Delete leve1 file -> only that component is deleted
assert level2_file1.parent == level1_dir1
assert level2_file1 in level1_dir1.contents.values()
level2_file1.delete()
assert level2_file1 not in level1_dir1.contents.values()
assert level2_file1.parent is None

# Delete level 2 directory -> deletes all level 3 & 4 components
assert level3_file1 in level2_dir1.contents.values()
assert level3_file1.parent == level2_dir1
assert level4_file1 in level3_dir1.contents.values()
assert level4_file1.parent == level3_dir1
level2_dir1.delete()
assert level3_file1 not in level2_dir1.contents.values()
assert level3_file1.parent is None
assert level4_file1 not in level3_dir1.contents.values()
assert level4_file1.parent is None
