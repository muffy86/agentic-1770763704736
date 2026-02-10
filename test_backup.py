import unittest
import os
import shutil
import tempfile
from backup import create_backup  # Import the function from your script

class TestBackupScript(unittest.TestCase):

    def setUp(self):
        # Create temporary directories for source and backup
        self.source_dir = tempfile.mkdtemp()
        self.backup_dir = tempfile.mkdtemp()

        # Create a dummy file in the source directory
        self.dummy_file_path = os.path.join(self.source_dir, 'dummy_file.txt')
        with open(self.dummy_file_path, 'w') as f:
            f.write('This is a test file.')

    def tearDown(self):
        # Clean up the temporary directories after each test
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.backup_dir)

    def test_create_backup_success(self):
        # Call the create_backup function
        create_backup(self.source_dir, self.backup_dir)

        # Check if a zip file was created in the backup directory
        backup_files = os.listdir(self.backup_dir)
        self.assertEqual(len(backup_files), 1)
        self.assertTrue(backup_files[0].endswith('.zip'))

    def test_create_backup_source_not_found(self):
        # Test the case where the source directory does not exist
        with self.assertRaises(FileNotFoundError):
            create_backup('nonexistent_dir', self.backup_dir)


if __name__ == '__main__':
    unittest.main()
